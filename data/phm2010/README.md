# PHM Data Challenge 2010: C1 Selected Cuts

This directory contains a compact, course-curated subset of the 2010 PHM
Society Conference Data Challenge for ME 5995. It includes three complete
machining records from cutter `c1` and the complete `c1` wear table. It is not
the original benchmark dataset or a predefined machine-learning split.

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

The course relies on the Kaggle Version 1 CC0 designation for redistribution
of this subset. The repository MIT license applies to course-authored code and
documentation, not as a replacement for the data-source license.

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

Lab 2 uses the complete `c1_cut158.csv` record for CSV loading, table
inspection, time-vector construction, descriptive statistics, RMS calculation,
plotting, and engineering interpretation. That file contains 219,691 rows,
seven channels, and no missing values. Its output SHA-256 is:

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

> rabah ba, “PHM data challenge 2010,” Kaggle, Version 1, CC0: Public Domain.
> <https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010>
