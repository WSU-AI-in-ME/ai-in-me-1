# PHM 2010 derived features

[Download the feature table](phm2010_features.csv) · [Data dictionary](DATA_DICTIONARY.md) · [PHM data overview](../README.md)

This compact ME 5995 dataset supports feature exploration, correlation, tool-wear
regression, wear-level classification, validation/generalization, tree/ensemble
models and PCA. **One row is one machining cut:** 315 cuts from each of `c1`,
`c4` and `c6`, totaling **945 rows and 56 columns**.

## Two data layers

- [Selected raw records](../c1_selected_cuts/): three complete c1 signals and the
  c1 wear table for waveform handling, feature extraction, FFT and STFT.
- [Derived feature table](phm2010_features.csv): scalar summaries of all 945
  labeled c1/c4/c6 cuts. The full raw corpus is not included in this repository.

## Features and targets

The table contains 8 metadata columns, 3 original flute-wear measurements,
2 derived continuous targets, 1 instructional class and **42 sensor features**:
28 core features (mean, sample SD, raw RMS and peak-to-peak on seven channels)
and 14 exploratory features (raw crest factor and Pearson kurtosis).

All 42 features are provided for learning; do not automatically use all columns
as model inputs. The course's initial **11 default predictors** are:

```python
default_features = [
    "force_x_mean", "force_x_sd", "force_y_mean", "force_y_sd",
    "force_z_mean", "force_z_sd", "vibration_x_sd", "vibration_y_sd",
    "vibration_z_sd", "ae_rms_mean", "ae_rms_sd",
]
```

This subset reflects physical interpretation and known redundancy, not predictive
performance optimization on the full dataset. Metadata (including `cut_number`)
and all wear measurements/targets are excluded from predictor inputs.
`wear_mean_um` is the primary regression target; `wear_max_um` is also provided.

| `wear_level` | Mean wear (µm) | c1 | c4 | c6 | Total |
|---|---|---:|---:|---:|---:|
| 0 | ≤75 | 27 | 75 | 17 | 119 |
| 1 | >75 and <150 | 259 | 194 | 210 | 663 |
| 2 | ≥150 | 29 | 46 | 88 | 163 |

These are course-defined instructional categories, **not official PHM benchmark
severity classes or universal tool-wear limits**.

## Processing and limitations

Deterministic processing used every sample of each full recorded signal, joined
to wear by cutter and cut. No inferred active-cut interval, filtering, clipping,
resampling or sample replacement was applied. Sample SD uses `ddof=1`; RMS
retains the mean; kurtosis is Pearson with `fisher=False, bias=True`. Equations,
units, source identifiers and all 56 column roles are in the dictionary.
Independent full builds reproduced the original table. The lower class boundary
was revised from 50 to 75 µm on September 22, 2026; 99 labels changed
from 1 to 0. Sensor features and continuous wear values are unchanged.
If you saved an earlier copy, download the current CSV before using `wear_level`
for classification. Each source signal's SHA-256
is retained; `source_file` is an original archive-relative identifier, not a link
to a file shipped with this table.

No train/validation/test split is provided. Define the evaluation goal before
splitting: unseen-cutter evaluation requires cutter separation. Keep windows of
one recording together and fit scaling, feature selection and PCA on training
data only. Three cutters are only three physical groups, not 945 independent
experiments. Wear levels are strongly imbalanced. Cut sequence can act as a wear
shortcut. Whole-record features mix unannotated acquisition/engagement states;
correlations do not establish causation. These course tasks do not reproduce the
original challenge benchmark.

## Source, attribution and rights

Primary source: PHM Society, [2010 PHM Society Conference Data Challenge](https://phmsociety.org/phm_competition/2010-phm-society-conference-data-challenge/).
The official challenge identifies c1/c4/c6 as training cutters. It documents Force
X/Y/Z in N, Vibration X/Y/Z in g, AE-RMS in V and acquisition at 50 kHz/channel.
Original wear is in 10^-3 mm, numerically equal to µm.

This course feature table is a derived instructional dataset computed from the
PHM Society 2010 Data Challenge records. Original data provenance remains with
the PHM Society Data Challenge source. The course repository does not claim
ownership of the underlying PHM source data.

The official PHM Society challenge page does not provide an explicit
dataset-specific license statement in the source documentation reviewed for this
release. The [third-party Kaggle mirror](https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010)
labels its hosted copy **CC0: Public Domain**. This is mirror metadata, not an
official PHM Society license declaration or proof of rights for every source copy.
The repository's [MIT license](../../../LICENSE) covers original course code and
documentation; it does not override third-party dataset rights or relicense the
underlying PHM data. No redistribution permission should be inferred from that
repository license.

## Reproducible processing

The scalar feature definitions and transformations are documented in the
[feature dictionary](DATA_DICTIONARY.md). Students use the supplied
feature table; running the instructor's private curation utility is not required.
The full raw corpus is not included. This feature table contains scalar features and wear labels/targets
derived from the PHM 2010 challenge records, not the complete raw c1/c4/c6 signals.

Users should consult the original source and applicable terms when obtaining or
redistributing the underlying raw data.

These wear levels are course-defined instructional categories and are not
official PHM Society benchmark classes or universal industrial wear-severity
limits.
