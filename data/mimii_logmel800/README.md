# MIMII Log-Mel Teaching Dataset

This course-derived dataset contains unstandardized log-mel inputs from 800 normal
MIMII public 1.0 recordings: fan, pump, slider and valve, four local IDs per type,
50 recordings per type/ID. Each ten-second parent yields ten nonoverlapping
one-second segments. This is machine-type classification, not fault diagnosis
or the original MIMII anomalous-sound benchmark.

## Source, transformations and license

Original authors: Harsh Purohit, Ryo Tanabe, Kenji Ichige, Takashi Endo, Yuki Nikaido,
Kaori Suefusa and Yohei Kawaguchi (Hitachi, Ltd.), 2019.
[MIMII public 1.0](https://zenodo.org/records/3384388), DOI10.5281/zenodo.3384388;
[dataset paper](https://arxiv.org/abs/1909.09347). Source/license reviewed October29,2026.
The source is CC BY-SA4.0; retain LICENSE_DATA.txt, attribution and ShareAlike terms.
The data license is separate from the repository software license.

Course changes: normal-recording selection, Channel1 retention, segmentation,
fixed-reference log-mel extraction and added labels/lineage/partitions. Source
WAVs are not included. Source paths and hashes are retained in recordings.csv.
The exact frozen selection is the list of source_file entries in recordings.csv;
use those entries to reproduce this cohort rather than drawing a new random
sample. Original filenames are preserved in those paths. Within each type/ID,
the supplied partition column is authoritative; it must not be recreated by a
segment-level random split.

Each source is 16kHz PCM16, ten seconds, from the 0dB factory-background mixture.
The exact feature recipe is frame512, periodic Hann, hop256, no padding, squared
rFFT magnitude, 32 Slaney area-normalized mel filters over0-8000Hz, then
10*log10(max(mel_power,1e-12)/1.0). Values are relative digital log-power, not dB SPL.
See FEATURE_DICTIONARY.md. Do not substitute generic library defaults.

## Files and observation units

- logmel.npz: X(8000,32,61), float32; y(8000,), integer class targets0-3;
  recording_index(8000,), recording_id(800,), machine_id(800,), class_names(4,).
- recordings.csv: one row per parent, original source path/checksums, type/ID,
  audio properties and the fixed partition. ID labels are local within type.
- baseline32_summary.csv: matched32-unit model results for the stated teaching
  configuration; no weights or executable Homework solution are included.
- FEATURE_DICTIONARY.md and LICENSE_DATA.txt: exact representation and provenance.
- checksums.json: integrity evidence for release tooling; students do not implement
  SHA checks as part of their learning tasks.

Labels are0 fan,1 pump,2 slider,3 valve. Identifiers, targets and partition names
are metadata, not model inputs. recording_index maps each segment to its parent row.

## Split, scaling and interpretation

The fixed seed20261026 manifest has30/10/10 parents per type/ID, totaling480/160/160
parents and4800/1600/1600 segments. All siblings remain together. Fit one mean and
population SD on all training elements, and reuse them on validation/test. The
NPZ is not standardized; do not fit a transform to the full X array.

The baseline has one32-ReLU hidden layer, four softmax outputs, Adam0.001, batch32,
40epochs, seed9 and minimum-validation-loss checkpoint selection. Its results
are illustrative, not score targets. This is same-ID evaluation on reused course
data, not unseen-ID or untouched external testing.

The compressed NPZ is about54.2MB; all other files are small. The provided notebook
setup caches the files so repeated runs do not repeatedly download them.
