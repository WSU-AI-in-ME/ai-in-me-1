# MIMII Course Teaching Subset

This directory contains a derived teaching subset of **MIMII public 1.0:
Sound Dataset for Malfunctioning Industrial Machine Investigation and
Inspection**. It is intended for ME 5995 course activities and is not an
official MIMII benchmark split.

The subset contains **220 unique WAV files**. Use [metadata.csv](metadata.csv)
to select task memberships; shared recordings are stored only once.

## Original Sources

- Dataset and license: https://zenodo.org/records/3384388
- Dataset DOI: https://doi.org/10.5281/zenodo.3384388
- Paper: https://arxiv.org/abs/1909.09347
- Version: MIMII public 1.0
- Source files used: `0_dB_fan`, `0_dB_pump`, `0_dB_slider`, and `0_dB_valve`
- Source reviewed for this subset: 2026-09-01

Purohit et al. describe MIMII as an industrial-machine sound dataset containing
normal and anomalous operating conditions for valves, pumps, fans, and slide
rails. The original WAV files contain eight microphone channels recorded at
16 kHz with 16 bits per sample in 10-second segments.

## Important 0 dB Interpretation

The `0 dB` recordings are **not noise-free**. Factory background noise was
mixed with the target machine sound at an SNR of 0 dB. In the source paper's
mixing definition, the average machine-sound power and adjusted noise power are
equal at 0 dB.

## Course-Specific Audio Processing

- Only microphone Channel 1 is retained (source channel index `0` in Python).
- Every output is mono, uncompressed 16-bit PCM WAV at 16 kHz.
- Every recording retains all 160,000 samples and remains 10 seconds long.
- Amplitude is not normalized.
- Audio is not cropped, sliced, resampled, compressed, or converted to a
  spectrogram.
- The source directory label `abnormal` is normalized to `anomaly` in this
  subset.
- Each original recording has exactly one physical output WAV file.

`metadata.csv` records task membership, original source paths, audio properties,
and a SHA-256 checksum for every physical WAV file.

## Selection Rule

Selection is deterministic and course-specific. The expansion preserves all
145 previously selected recordings and adds 75 normal recordings. It retains
all original IDs, WAV bytes, source mappings and existing task memberships.

For the additions, an independent Python random generator with seed `42` visits
`fan`, `pump`, `slider`, `valve`, and then `id_00`, `id_02`, `id_04`, `id_06`
within each type. It samples five sorted eligible normal source paths per group,
without replacement. Previously selected files are excluded, except for fan
`id_06`: five additional classification recordings are reused from its existing
anomaly-normal pool. Selection does not depend on waveform appearance, features
or model performance. Exact source selections are recorded in `metadata.csv`.

## Classification Teaching Task

The course-specific classification subset contains only normal recordings:

- Machine types: `fan`, `pump`, `slider`, `valve`
- IDs for each type: `id_00`, `id_02`, `id_04`, `id_06`
- 10 normal recordings per machine-type × machine-ID group
- 160 classification memberships

Machine-type classification is a course-derived task, not the original MIMII
benchmark definition.

## Anomaly-Detection Teaching Task

The anomaly-detection subset uses only fan `id_06`:

- 50 normal recordings
- 20 anomaly recordings
- 70 recordings total

Ten normal fan `id_06` files are shared with the classification task. They
have both task-inclusion flags in `metadata.csv` and are physically stored only
once.

The two tasks share 10 recordings, so `160 + 70 - 10 = 220` physical WAV files.

Task definitions are adapted for instruction. Machine-type classification and
any supervised normal/anomaly exercise are not the original MIMII benchmark
protocol. The original benchmark focuses on anomalous sound detection, commonly
using normal-only training data.

Anomaly labels are file-level labels. A short window from an anomalous
recording is not guaranteed to contain an obvious anomaly.

## Split and Leakage Policy

No train, validation, or test split is predefined. Split the original
10-second recordings **before** creating shorter windows. Windows with the same
`recording_id` must never cross train, validation, and test sets.

ML splits are defined in the relevant course activity; this dataset does not
assign a fixed split. Use the 10-normal-per-group classification pool according
to that activity's instructions. Fit learned transformations on training data
only. Use machine/model ID separation when evaluating unseen-ID generalization.
For normal-only anomaly-detection activities, keep anomalous recordings out of
training. Do not infer a benchmark protocol from these task membership flags.

## Limitations

This compact subset is intended for teaching. Results must not be interpreted
as official MIMII benchmark performance. The subset is small, uses one
microphone channel and one SNR condition, and supports course-specific tasks.

## Citation and Attribution

Harsh Purohit, Ryo Tanabe, Kenji Ichige, Takashi Endo, Yuki Nikaido, Kaori
Suefusa, and Yohei Kawaguchi, “MIMII Dataset: Sound Dataset for Malfunctioning
Industrial Machine Investigation and Inspection,” arXiv:1909.09347, 2019.

The original dataset was created by the listed authors at Hitachi, Ltd. and is
available from Zenodo under CC BY-SA 4.0. See [LICENSE_DATA.txt](LICENSE_DATA.txt) for the data
license notice. The repository [software license](../../LICENSE) does not override third-party
dataset rights. This derived audio subset remains governed by CC BY-SA 4.0;
preserve attribution, indicate changes and follow its ShareAlike requirements.
