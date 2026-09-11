# PHM Data Challenge 2010: course data

ME 5995 uses two complementary layers of PHM course data:

| Layer | Included material | Use |
|---|---|---|
| [Selected raw records](c1_selected_cuts/) | Three complete c1 signal records and 315-row c1 wear table | Waveforms, time-domain features, FFT, STFT and introductory signal analysis |
| [Derived features](features/README.md) | [945-row, 56-column table](features/phm2010_features.csv), c1/c4/c6, 315 cuts each | Feature exploration, correlation, regression, wear-level classification, validation/generalization, trees/ensembles and PCA |

Each derived row is one cut, computed deterministically from its full recorded
signal. The full raw c1/c4/c6 corpus is not included. These course datasets are
not the original challenge benchmark or a predefined ML split.

The sections below describe the selected raw subset. For all 42 derived sensor
features, target definitions and the 11 default predictors, see the
[feature README](features/README.md) and [dictionary](features/DATA_DICTIONARY.md).

## Files

| File | Description | Data rows |
|---|---|---:|
| `c1_selected_cuts/c1_cut001.csv` | Complete signal record for cut 1 | 127,399 |
| `c1_selected_cuts/c1_cut158.csv` | Complete signal record for cut 158 | 219,691 |
| `c1_selected_cuts/c1_cut315.csv` | Complete signal record for cut 315 | 252,492 |
| `c1_selected_cuts/c1_wear.csv` | Flute-level wear measurements for cuts 1–315 | 315 |
| `c1_selected_cuts/MANIFEST.csv` | Source paths, checksums, dimensions, and transformations | 4 |

Cuts 1, 158, and 315 are the first, midpoint, and final sequence positions.
They are not organizer-defined low-, medium-, or high-wear classes.

## Source and license

- Official source: [2010 PHM Society Conference Data Challenge](https://phmsociety.org/phm_competition/2010-phm-society-conference-data-challenge/)
- Course data source: [Kaggle mirror, Version 1](https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010)
- Kaggle version date: 2021-11-21
- Source access and verification date: 2026-09-01
- License displayed by Kaggle: [CC0 1.0 Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
- Subset version: 1.0

The four source files used here were independently downloaded from Kaggle
Version 1 and matched the retained local source files byte-for-byte by SHA-256.
`MANIFEST.csv` records each original filename and source checksum. The retained
local `c1.zip` archive had SHA-256:

```text
542B0D3EC78B322FEEC3C74B701143F730E9BBFDD00BB24B10CC8817CA1198C9
```

The official PHM Society challenge page does not provide an explicit
dataset-specific license statement in the source documentation reviewed for this
release. The [third-party Kaggle mirror](https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010)
labels its hosted copy **CC0: Public Domain**. This is mirror metadata, not an
official PHM Society license declaration or proof of rights for every source copy.
The repository's [MIT license](../../LICENSE) covers original course code and
documentation; it does not override third-party dataset rights or relicense the
underlying PHM data. No redistribution permission should be inferred from that
repository license.

This course feature table is a derived instructional dataset computed from the
PHM Society 2010 Data Challenge records. Original data provenance remains with
the PHM Society Data Challenge source. The course repository does not claim
ownership of the underlying PHM source data.

## Signal data

The official challenge documentation specifies seven channels sampled at
50,000 samples/s per channel.

| Column | Quantity | Unit |
|---|---|---|
| `force_x_N` | Force in the X direction | N |
| `force_y_N` | Force in the Y direction | N |
| `force_z_N` | Force in the Z direction | N |
| `vibration_x_g` | Vibration in the X direction | g |
| `vibration_y_g` | Vibration in the Y direction | g |
| `vibration_z_g` | Vibration in the Z direction | g |
| `ae_rms_V` | Acoustic-emission RMS signal | V |

The last sample timestamp is `(N - 1) / 50,000`. Record durations differ
because the three files contain different numbers of samples.

## Wear data

The wear table contains three flute-level measurements per cut:

```text
cut_id,wear_flute_1_um,wear_flute_2_um,wear_flute_3_um
```

The source unit `10^-3 mm` is numerically equal to micrometers. No mean wear,
maximum wear, wear class, or remaining-useful-life target is included.

## Selection and transformations

The subset was created deterministically by selecting complete cuts 1, 158,
and 315 and retaining the full 315-row `c1` wear table.

Signal files:

- descriptive headers were added;
- line endings were normalized to LF; and
- all samples, seven channels, numeric values, and row order were preserved.

Wear file:

- columns were renamed to state the quantity and unit;
- all 315 rows and numeric values were preserved; and
- line endings were normalized to LF.

No filtering, resampling, segmentation, scaling, normalization, interpolation,
missing-value treatment, or numeric rounding was applied. File-level source
and output SHA-256 checksums are recorded in `MANIFEST.csv`.

## Course use and limitations

Lab 2 uses `c1_wear.csv` to inspect and plot the three original flute-wear
curves, then compares the complete `c1_cut001.csv` and `c1_cut315.csv` records.
Force X is the guided example; Vibration X is the required application.
Students construct each record's own time vector and calculate whole-record
mean and sample standard deviation (`ddof=1`), using common axes without
padding or time stretching. These statistics are not cutting-only statistics;
the records are not aligned to the same cutting phase. Cut 1 is not an
established unworn or stable-cutting baseline.

The unchanged `c1_cut158.csv` remains available for other demonstrations. It
contains 219,691 rows, seven channels, and no missing values. Its output SHA-256 is:

```text
DB3BC81DA91991AE0A631C7F63E2B89C077B8EBC6A996EDC4BCCDB701EAB639F
```

This subset contains only three records from one cutter. It is not sufficient
for wear prediction, remaining-useful-life estimation, fault diagnosis, or
cutter-to-cutter generalization. Differences among the records do not
establish that wear caused the observed signal differences.

No train, validation, or test split is provided. Future modeling activities
must split at the cutter or run level rather than placing records from the same
cutter into nominally independent training and evaluation sets.

The workpiece material is intentionally not stated because conflicting
secondary descriptions have not been resolved from the original experimental
source.

## Citation

When using this subset, cite the original challenge and identify these files as
a course-curated subset:

> PHM Society, “2010 PHM Society Conference Data Challenge,” 2010.
> <https://phmsociety.org/phm_competition/2010-phm-society-conference-data-challenge/>

> rabah ba, “PHM data challenge 2010,” Kaggle, Version 1 (mirror metadata: CC0: Public Domain; not an official PHM license statement).
> <https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010>
