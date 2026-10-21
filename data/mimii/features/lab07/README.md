# Lab 7: Recording-Level MIMII Features

[lab07_features.csv](lab07_features.csv) provides 70 recording-level rows and 16
fixed log band-power input features for Lab 7. It reuses the existing course fan
`id_06` anomaly-detection pool: 50 normal and 20 anomaly recordings.
Labels, source paths, checksums and split names are metadata, not
model inputs. No raw-audio download is needed for this Lab.

## Provenance and feature definition

Original dataset: MIMII public 1.0, Purohit et al. (Hitachi, Ltd.), 2019,
[Zenodo record](https://zenodo.org/records/3384388),
[DOI](https://doi.org/10.5281/zenodo.3384388),
[paper](https://arxiv.org/abs/1909.09347). Source/license rechecked October 20, 2026;
feature table created and verified on that date from the existing course subset.
See the [course audio provenance](../../README.md) for deterministic audio
selection and conversion. This is a course-derived activity, not the official
MIMII benchmark protocol.

Each source course WAV is a complete 10-second mono PCM16 recording at 16 kHz,
retaining source microphone Channel 1 from the 0 dB background-mixture condition.
Samples are converted to float64 by division by 32768, without per-recording
normalization. A periodic Hann-window full-record density periodogram supplies
16 adjacent 500-Hz bands over 0 to 8000 Hz. Band power is the sum of PSD bins
times 0.1 Hz; features use `10*log10(max(band_power,1e-12)/1.0)`.
Values use a fixed digital reference, not Pa or dB SPL. The
[feature dictionary](LAB07_FEATURE_DICTIONARY.md) specifies boundaries, metadata
and extraction conventions. Original filenames and curated-WAV SHA-256 checksums
are retained per row. There is one row per whole recording and no segmentation.

## Fixed teaching split

| Partition | Normal | Anomaly | Purpose |
|---|---:|---:|---|
| training | 30 | 0 | Fit scaler/PCA on normal recordings only |
| validation | 10 | 10 | Compare fixed training-percentile threshold candidates |
| test | 10 | 10 | Evaluate the frozen choice |

Within each class, sort recording IDs and permute indices with NumPy
`default_rng`: seed 42 for normal, seed 43 for anomaly. Take the first 30 normals
for training, next 10 for validation, last 10 for test; take the first 10 anomalies
for validation and last 10 for test. CSV `split` preserves these fixed assignments.
No recording crosses partitions. Validation rows are ordered normal then anomaly.
Fit preprocessing on training only. This is a small same-ID teaching evaluation;
it does not evaluate unseen-machine generalization. Some recordings were available
in earlier course activities, and the test's 50% anomaly fraction is artificial.

## Integrity and license

CSV SHA-256:
`55d899f437884f8964193117c30760717cc0f62bc45ce5b021cf5bf350f63891`.

The derived CSV is shared under **CC BY-SA 4.0**. Preserve the original authors,
source, change notice and ShareAlike conditions. See
[LICENSE_DATA.txt](LICENSE_DATA.txt). The repository software license does not
replace these data terms. Changes comprise the existing mono conversion plus
fixed frequency-band extraction and a course-specific recording-level split.
