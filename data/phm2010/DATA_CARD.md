# Data Card: PHM Data Challenge 2010 C1 Selected Cuts

**Status:** Course subset prepared for public redistribution; instructor review required before commit or publication  
**Course:** ME 5995 — AI in Mechanical Engineering I: Fundamentals of Manufacturing Data Science  
**Subset version:** 1.0 candidate  
**Curation date:** 2026-09-01

## Dataset title

PHM Data Challenge 2010 — Cutter C1 Selected Cuts (course-curated subset)

## Sources and provenance

- Official title: 2010 PHM Society Conference Data Challenge
- Original challenge page: <https://phmsociety.org/phm_competition/2010-phm-society-conference-data-challenge/>
- Original data release date stated by the official page: 2010-06-02
- Original challenge page access date: 2026-09-01
- DOI: No DOI was identified on the official challenge page.
- Official dataset version: No explicit version identifier was identified on
  the official challenge page.
- Course data source: Kaggle mirror, `rabahba/phm-data-challenge-2010`
- Kaggle page: <https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010>
- Kaggle dataset version: Version 1
- Kaggle version date: 2021-11-21
- Kaggle access and verification date: 2026-09-01
- License displayed by Kaggle: CC0: Public Domain
- License reference: <https://creativecommons.org/publicdomain/zero/1.0/>

The working source snapshot was extracted from a locally retained `c1.zip`.
The local archive SHA-256 is recorded for internal traceability:

```text
542B0D3EC78B322FEEC3C74B701143F730E9BBFDD00BB24B10CC8817CA1198C9
```

The three selected signal records and the wear table were independently
downloaded from Kaggle Version 1 on 2026-09-01. Each downloaded file matched
the corresponding local source file byte-for-byte by SHA-256. The verified
Kaggle paths are:

```text
c1/c1/c_1_001.csv
c1/c1/c_1_158.csv
c1/c1/c_1_315.csv
c1/c1_wear.csv
```

This comparison establishes Kaggle Version 1 provenance for every source file
used in this curated subset. It does not establish byte-level identity of the
entire local archive with an organizer archive.

## Original challenge purpose

The original challenge focused on remaining-useful-life estimation for
high-speed CNC milling cutters using dynamometer, accelerometer, and acoustic
emission data. The original dataset contained cutter records `c1` through `c6`.
The official page identifies `c1`, `c4`, and `c6` as training records with wear
measurements and `c2`, `c3`, and `c5` as test records.

This course subset is not the original benchmark and must not be described as
a conventional random-split regression dataset.

## Course-specific purpose

This subset supports introductory work with manufacturing data, including:

- loading CSV files in Python;
- inspecting dimensions, columns, data types, and missing values;
- connecting sample index, sampling rate, and physical time;
- computing descriptive statistics and RMS;
- creating labeled time-domain plots;
- comparing direct observations across selected sequence positions; and
- distinguishing signal observations from unsupported diagnostic conclusions.

The subset is not intended for machine-learning training, wear prediction, or
remaining-useful-life estimation in Week 1.

## Source records and filenames

| Curated file | Original file | Selection role |
|---|---|---|
| `c1_selected_cuts/c1_cut001.csv` | `c1/c1/c_1_001.csv` | First cut in the recorded sequence |
| `c1_selected_cuts/c1_cut158.csv` | `c1/c1/c_1_158.csv` | Midpoint cut of cuts 1 through 315 |
| `c1_selected_cuts/c1_cut315.csv` | `c1/c1/c_1_315.csv` | Final cut in the recorded sequence |
| `c1_selected_cuts/c1_wear.csv` | `c1/c1_wear.csv` | Complete cutter `c1` wear table |

Cuts 1, 158, and 315 are deterministic sequence positions. They were not
randomly sampled and are not organizer-defined low-, medium-, or high-wear
classes.

## Sampling rate and record dimensions

The official challenge page documents a sampling rate of 50 kHz per channel.

| File | Samples | Columns | Last sample time |
|---|---:|---:|---:|
| `c1_cut001.csv` | 127,399 | 7 | 2.54796 s |
| `c1_cut158.csv` | 219,691 | 7 | 4.39380 s |
| `c1_cut315.csv` | 252,492 | 7 | 5.04982 s |

The last sample time is `(N - 1) / 50,000`. The corresponding nominal sample
span is `N / 50,000`; these two quantities should not be conflated.

## Channel definitions and units

| Column | Physical quantity | Unit | Basis |
|---|---|---|---|
| `force_x_N` | Force in the X direction | N | Official challenge description |
| `force_y_N` | Force in the Y direction | N | Official challenge description |
| `force_z_N` | Force in the Z direction | N | Official challenge description |
| `vibration_x_g` | Vibration in the X direction | g | Official challenge description |
| `vibration_y_g` | Vibration in the Y direction | g | Official challenge description |
| `vibration_z_g` | Vibration in the Z direction | g | Official challenge description |
| `ae_rms_V` | Acoustic-emission RMS signal | V | Official challenge description |

The official page uses the term “Vibration (g)” for columns 4–6. This data card
does not replace that source terminology with an unqualified acceleration
label.

## Wear labels

The complete cutter `c1` wear table contains cut IDs 1 through 315 and three
flute-level wear measurements per cut. The official source reports these
values in `10^-3 mm`, which is numerically equal to micrometers.

The curated columns are:

```text
cut_id,wear_flute_1_um,wear_flute_2_um,wear_flute_3_um
```

No mean-wear, maximum-wear, wear-class, or remaining-useful-life target is
included. Any such variable would be a course-derived target and would require
a separate definition and justification.

## Selection procedure

1. Use the four source files verified byte-for-byte against Kaggle Version 1.
2. Verify each selected source file against the source SHA-256 value recorded
   in `c1_selected_cuts/MANIFEST.csv`.
3. Select complete cuts 1, 158, and 315 without removing any rows or channels.
4. Retain the complete 315-row cutter `c1` wear table.
5. Validate column count, numeric parseability, wear-table cut IDs, and row
   ordering.
6. Add descriptive headers, write UTF-8 CSV files with LF line endings, and
   calculate output SHA-256 checksums.

The maintainer curation script is retained in the private course-development
workspace and is not distributed in this public repository. The deterministic
selection procedure, transformations, and checksums required to audit the
public subset are documented in this data card and the manifest.

## Transformations

Signal files:

- added descriptive column names;
- normalized line endings to LF;
- preserved all seven channels;
- preserved all samples and original row order; and
- applied no filtering, resampling, segmentation, scaling, normalization, or
  numeric rounding.

Wear file:

- renamed columns to state the quantity and unit explicitly;
- represented the source unit `10^-3 mm` as the equivalent unit `um`;
- left all numeric values unchanged;
- retained all 315 rows; and
- normalized line endings to LF.

## Train, validation, and test grouping policy

This subset contains only cutter `c1` and is not sufficient for a credible
train/validation/test evaluation. If PHM 2010 data are later used for modeling,
records from the same cutter must not be randomly divided across training and
evaluation sets as though they were independent cutters. Cutter- or run-level
grouping must be used, and the limited number of labeled cutters must be
reported as a validation limitation.

## Checksums

`c1_selected_cuts/MANIFEST.csv` records, for every curated data file:

- original relative filename;
- source SHA-256;
- curated output filename;
- output SHA-256;
- data-row and column counts; and
- documented transformations.

The manifest is generated by the curation script and should be regenerated and
reviewed whenever the curated files change.

## License and redistribution status

Kaggle identifies Version 1 of `rabahba/phm-data-challenge-2010` as **CC0:
Public Domain**. The course relies on that `CC0 1.0` designation for use,
modification, and redistribution of this small curated subset. The exact source
files used here were verified byte-for-byte against Kaggle Version 1.

The subset is prepared for public course use but must still be reviewed by the
instructor before commit or publication. Although CC0 does not require
attribution, both the Kaggle mirror and original PHM Society challenge source
are retained for scholarly provenance. This course curation does not imply
endorsement by Kaggle, the uploader, or the PHM Society.

The repository's MIT license applies to course-authored software and
documentation. The curated data files are distributed under the stated Kaggle
Version 1 CC0 basis.

## Known limitations

- The subset contains three records from only one cutter.
- Sequence position is confounded with elapsed cutting history and other
  uncontrolled or undocumented changes.
- Differences among the selected signals do not demonstrate that wear caused
  those differences.
- The three selected records do not define wear classes or a degradation
  benchmark.
- Record durations differ across the selected cuts.
- The subset excludes cutters `c4` and `c6`, so it cannot evaluate
  cutter-to-cutter generalization.
- Exact measurement uncertainty for the wear values is not stated on the
  official challenge page.
- The Kaggle mirror is a third-party mirror rather than an organizer-operated
  source. The course relies on Kaggle's Version 1 CC0 designation.
- Byte-level identity of the complete local archive with an organizer archive
  was not evaluated; verification covered every source file used in this
  subset.
- No workpiece material is stated here because conflicting secondary
  descriptions have not been resolved from the original experimental source.

## Citation

When using this subset, preserve both sources and identify the data as a
course-curated subset rather than as the complete original benchmark:

> PHM Society, “2010 PHM Society Conference Data Challenge,” 2010. Available:
> <https://phmsociety.org/phm_competition/2010-phm-society-conference-data-challenge/>.

> rabah ba, “PHM data challenge 2010,” Kaggle, Version 1, CC0: Public Domain.
> Available: <https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010>.
