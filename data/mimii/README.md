# MIMII Compact Teaching Subset

This directory contains a derived teaching subset of **MIMII public 1.0:
Sound Dataset for Malfunctioning Industrial Machine Investigation and
Inspection**. It is intended for ME 5995 course activities and is not an
official MIMII benchmark split.

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

Selection is deterministic with random seed `42`. Candidate paths are sorted,
then one seeded Python random generator is used in this fixed order:

1. Machine types: `fan`, `pump`, `slider`, `valve`
2. Machine IDs within each type: `id_00`, `id_02`, `id_04`, `id_06`
3. Five normal files per machine-type and machine-ID group
4. Forty-five additional normal fan `id_06` files
5. Twenty anomalous fan `id_06` files

The exact selected source files are recorded in `metadata.csv`.

## Classification Teaching Task

The course-specific classification subset contains only normal recordings:

- 4 machine types
- 4 machine IDs per type
- 5 recordings per machine type and ID
- 80 recordings total

Machine-type classification is a course-derived task, not the original MIMII
benchmark definition.

## Anomaly-Detection Teaching Task

The anomaly-detection subset uses only fan `id_06`:

- 50 normal recordings
- 20 anomaly recordings
- 70 recordings total

Five normal fan `id_06` files are shared with the classification task. They
have both task-inclusion flags in `metadata.csv` and are physically stored only
once.

Anomaly labels are file-level labels. A short window from an anomalous
recording is not guaranteed to contain an obvious anomaly.

## Split and Leakage Policy

No train, validation, or test split is predefined. Split the original
10-second recordings **before** creating shorter windows. Windows with the same
`recording_id` must never cross train, validation, and test sets.

Suggested deterministic course splits using `random_state=42`:

- Classification: within each machine-type and machine-ID group, use 3 files
  for training, 1 for validation, and 1 for testing.
- Anomaly detection: use 35 normal files for training, 5 normal files for
  validation, and a test set containing 10 normal and 20 anomaly files.

The anomaly-detection training and validation sets must contain only normal
recordings. Split logic belongs in the course notebook, not in this prepared
dataset.

## Limitations

This compact subset is intended for teaching. Results must not be interpreted
as official MIMII benchmark performance. The subset is small, uses one
microphone channel and one SNR condition, and supports course-specific tasks.

## Citation and Attribution

Harsh Purohit, Ryo Tanabe, Kenji Ichige, Takashi Endo, Yuki Nikaido, Kaori
Suefusa, and Yohei Kawaguchi, “MIMII Dataset: Sound Dataset for Malfunctioning
Industrial Machine Investigation and Inspection,” arXiv:1909.09347, 2019.

The original dataset was created by the listed authors at Hitachi, Ltd. and is
available from Zenodo under CC BY-SA 4.0. See `LICENSE_DATA.txt` for the data
license notice. The repository software license does not replace the dataset
license.
