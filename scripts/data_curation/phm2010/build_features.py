"""Reproduce the course scalar table from user-supplied PHM source records."""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import csv
import hashlib
import io
from pathlib import Path
import numpy as np

FS = 50_000.0
CUTTERS = ('c1', 'c4', 'c6')
CHANNELS = ('force_x', 'force_y', 'force_z', 'vibration_x',
            'vibration_y', 'vibration_z', 'ae_rms')
FEATURE_MAP = {'mean': 'mean', 'sd': 'sample_std', 'rms': 'rms',
               'peak_to_peak': 'peak_to_peak', 'crest_factor': 'crest_factor',
               'kurtosis': 'kurtosis_pearson'}
METADATA = ['cutter_id', 'cut_number', 'source_file', 'source_sha256',
            'n_samples', 'sample_rate_hz', 'duration_s', 'last_sample_time_s']
ORIGINAL = [f'wear_flute_{i}_um' for i in (1, 2, 3)]
COLUMNS = (METADATA + ORIGINAL + ['wear_mean_um', 'wear_max_um', 'wear_level']
           + [f'{channel}_{feature}' for channel in CHANNELS for feature in FEATURE_MAP])


def checked(x):
    """Reject invalid data rather than silently dropping or imputing samples."""
    x = np.asarray(x, dtype=np.float64)
    if x.ndim != 1 or x.size < 2 or not np.isfinite(x).all():
        raise ValueError('Expected at least two finite samples in one channel.')
    return x

def time_features(x):
    """Use raw RMS/crest and Pearson central-moment kurtosis, bias=True."""
    x = checked(x)
    mean = x.mean()
    centered = x - mean
    scale = np.max(np.abs(x))
    rms = scale * np.sqrt(np.mean((x / scale)**2)) if scale else 0.0
    ac_scale = np.max(np.abs(centered))
    if ac_scale:
        z = centered / ac_scale
        m2 = np.mean(z*z)
        kurt = np.mean(z**4) / m2**2
    else:
        kurt = np.nan
    return {'mean': float(mean), 'sample_std': float(x.std(ddof=1)),
            'rms': float(rms), 'peak_to_peak': float(np.ptp(x)),
            'crest_factor': float(scale/rms) if rms else np.nan,
            'kurtosis_pearson': float(kurt)}

def wear_level(mean):
    if not np.isfinite(mean):
        raise ValueError('Wear must be finite; no target imputation.')
    return 0 if mean <= 50 else 1 if mean < 150 else 2


def inventory(source):
    """Require exactly one signal/wear match for each approved cutter/cut."""
    jobs = []
    for cutter in CUTTERS:
        wear_path = source / cutter / f'{cutter}_wear.csv'
        with wear_path.open(encoding='utf-8-sig', newline='') as handle:
            wear = list(csv.DictReader(handle))
        ids = [int(row['cut']) for row in wear]
        if len(ids) != 315 or set(ids) != set(range(1, 316)):
            raise ValueError(f'{cutter}: wear must contain unique cuts 1..315')
        by_cut = {int(row['cut']): row for row in wear}
        signals = sorted((source / cutter).rglob('c_*.csv'))
        expected = {source / cutter / cutter / f'c_{cutter[1]}_{cut:03d}.csv'
                    for cut in range(1, 316)}
        if set(signals) != expected:
            raise ValueError(f'{cutter}: expected exactly 315 signals in the documented layout')
        for cut in range(1, 316):
            target = [float(by_cut[cut][f'flute_{i}']) for i in (1, 2, 3)]
            if not np.isfinite(target).all():
                raise ValueError(f'{cutter}/{cut}: nonfinite wear')
            relative = f'{cutter}/{cutter}/c_{cutter[1]}_{cut:03d}.csv'
            jobs.append((str(source / relative), relative, cutter, cut, target))
    return jobs


def process(job):
    """Read every sample; no filtering, clipping, cropping or imputation."""
    filename, relative, cutter, cut, target = job
    try:
        payload = Path(filename).read_bytes()
        x = np.loadtxt(io.BytesIO(payload), delimiter=',', dtype=np.float64, ndmin=2)
        n = len(x)
        if x.shape[1] != 7 or n < 2 or n != sum(bool(line.strip()) for line in payload.splitlines()):
            raise ValueError(f'invalid shape or source line count: {x.shape}')
        if not np.isfinite(x).all():
            raise ValueError('NaN/Inf samples; no automatic replacement')
        wear = np.asarray(target, dtype=np.float64)
        row = dict(cutter_id=cutter, cut_number=cut, source_file=relative,
                   source_sha256=hashlib.sha256(payload).hexdigest(), n_samples=n,
                   sample_rate_hz=int(FS), duration_s=n/FS, last_sample_time_s=(n-1)/FS)
        row.update({name: float(value) for name, value in zip(ORIGINAL, wear)})
        row.update(wear_mean_um=float(wear.mean()), wear_max_um=float(wear.max()),
                   wear_level=wear_level(float(wear.mean())))
        for index, channel in enumerate(CHANNELS):
            values = time_features(x[:, index])
            if not np.isfinite(list(values.values())).all():
                raise ValueError(f'{channel}: undefined feature (e.g. constant signal)')
            row.update({f'{channel}_{name}': values[key] for name, key in FEATURE_MAP.items()})
        return row
    except Exception as exc:
        raise ValueError(f'{cutter}/cut {cut}: {exc}') from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path,
                        help='Root containing extracted c1, c4 and c6 source directories')
    parser.add_argument('--output', required=True, type=Path, help='New output CSV path')
    parser.add_argument('--workers', type=int, default=4, choices=range(1, 5))
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    if output == source or source in output.parents:
        raise ValueError('Write output outside the source directory')
    partial = output.with_name(output.name + '.partial')
    if output.exists() or partial.exists():
        raise FileExistsError('Choose a fresh output path; existing files are preserved')
    jobs = inventory(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    # A failure identifies cutter/cut, stops the build and leaves only a partial file.
    with partial.open('x', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, COLUMNS, lineterminator='\n')
        writer.writeheader()
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            for count, row in enumerate(pool.map(process, jobs), 1):
                writer.writerow(row)
                if count % 105 == 0:
                    print(f'{count}/945 cuts processed', flush=True)
    partial.rename(output)
    print(f'Complete: {count} rows, {len(COLUMNS)} columns; {output}')


if __name__ == '__main__':
    main()
