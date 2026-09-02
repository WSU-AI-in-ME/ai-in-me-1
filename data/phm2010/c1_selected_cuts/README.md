# PHM 2010 Cutter C1 Selected Cuts

This directory contains a course-curated subset of the PHM Data Challenge
2010 cutter `c1` record. It includes the first, midpoint, and final cuts in the
315-cut sequence, together with the complete cutter `c1` wear table.

## Files

| File | Description | Data rows | Last sample time |
|---|---|---:|---:|
| `c1_cut001.csv` | Complete signal record for cut 1 | 127,399 | 2.54796 s |
| `c1_cut158.csv` | Complete signal record for cut 158 | 219,691 | 4.39380 s |
| `c1_cut315.csv` | Complete signal record for cut 315 | 252,492 | 5.04982 s |
| `c1_wear.csv` | Wear measurements for all 315 cutter `c1` cuts | 315 | Not applicable |
| `MANIFEST.csv` | Source and output checksums and transformation record | 4 | Not applicable |

The signal sampling rate is 50,000 samples per second per channel. The last
sample time is calculated as `(number_of_samples - 1) / 50_000`.

## Signal columns

```text
force_x_N
force_y_N
force_z_N
vibration_x_g
vibration_y_g
vibration_z_g
ae_rms_V
```

The original source values and row order are unchanged. The curation process
adds descriptive column names and normalizes line endings to LF.

## Wear columns

```text
cut_id
wear_flute_1_um
wear_flute_2_um
wear_flute_3_um
```

The official source reports the wear values in `10^-3 mm`, which is
numerically equal to micrometers. The curation process changes the column names
to state the units explicitly but does not scale or otherwise change the
numeric values.

## Important interpretation limit

Cuts 1, 158, and 315 are sequence positions, not organizer-defined wear
classes. Differences among three records from one cutter do not establish that
wear alone caused the signal differences, and this subset is not sufficient
for wear prediction or cutter-level generalization.

## Curation provenance

The course source is Kaggle Version 1 of
[`rabahba/phm-data-challenge-2010`](https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010).
The four selected source files were independently downloaded from Kaggle and
matched the retained local source files byte-for-byte by SHA-256. The original
PHM Society challenge page is preserved in `../DATA_CARD.md` as the primary
technical reference.

The complete PHM 2010 dataset and maintainer curation script are not included
in this public repository. Students do not need either item to complete Lab 2.
The deterministic selection rule and transformations are documented in
`../DATA_CARD.md`, and `MANIFEST.csv` records file-level source and output
checksums.

## License and redistribution

Kaggle identifies Version 1 of the course source as **CC0: Public Domain**. The
course relies on that `CC0 1.0` designation to redistribute this small curated
subset. The subset was curated for ME 5995 and its inclusion does not imply
endorsement by Kaggle, the uploader, or the PHM Society.

The repository's MIT license covers course-authored software and documentation;
the data files use the Kaggle Version 1 CC0 basis documented in
`../DATA_CARD.md`.
