# PHM 2010 Lab 2 Data Card

**Status:** Course subset prepared for public redistribution; instructor review required before commit or publication  
**Course:** ME 5995 — AI in Mechanical Engineering I: Fundamentals of Manufacturing Data Science  
**Lab:** Lab 2 — Scientific Computing with Manufacturing Data  
**Curation date:** 2026-09-01

## Dataset and source

- Original dataset: 2010 PHM Society Conference Data Challenge
- Original challenge source: <https://phmsociety.org/phm_competition/2010-phm-society-conference-data-challenge/>
- Original challenge source access date: 2026-09-01
- Course data source: Kaggle mirror, `rabahba/phm-data-challenge-2010`
- Kaggle page: <https://www.kaggle.com/datasets/rabahba/phm-data-challenge-2010>
- Kaggle dataset version: Version 1
- Kaggle version date: 2021-11-21
- Kaggle access and verification date: 2026-09-01
- License displayed by Kaggle: CC0: Public Domain
- License reference: <https://creativecommons.org/publicdomain/zero/1.0/>
- Original challenge purpose: Remaining-useful-life estimation for high-speed
  CNC milling cutters using dynamometer, accelerometer, and acoustic-emission
  data
- Local source archive: `c1.zip`
- Source archive SHA-256:
  `542B0D3EC78B322FEEC3C74B701143F730E9BBFDD00BB24B10CC8817CA1198C9`
- Original record: `c1/c1/c_1_158.csv`
- Source record SHA-256:
  `2B512667A3C6264A1480A60174192F01B790003FF7F9095A8D34D474713C04E8`

The Kaggle Version 1 file `c1/c1/c_1_158.csv` was downloaded independently
and compared with the inspected local source record. Their SHA-256 checksums
match exactly, establishing byte-level identity for the Lab 2 source file.

The official page identifies cutter records `c1`, `c4`, and `c6` as training
records with wear measurements. Lab 2 uses one complete record from cutter
`c1`; it does not use the wear table.

## Lab 2 selection

| Field | Value |
|---|---|
| Curated file | `c1_selected_cuts/c1_cut158.csv` |
| Cutter | `c1` |
| Cut identifier | 158 |
| Selection | Complete data-acquisition record; all rows and all seven channels |
| Data rows | 219,691 |
| Sensor columns | 7 |
| Sampling rate | 50,000 samples/s per channel |
| Last sample time | 4.39380 s, calculated as `(N - 1) / fs` |
| Missing values | 0 |
| Output size | 9,885,212 bytes |
| Output SHA-256 | `DB3BC81DA91991AE0A631C7F63E2B89C077B8EBC6A996EDC4BCCDB701EAB639F` |

Cut 158 is the midpoint sequence position among cuts 1 through 315. It is not
an organizer-defined wear class and is not described as a representative,
normal, faulty, low-wear, or high-wear record.

## Channels

| Column | Physical quantity | Unit |
|---|---|---|
| `force_x_N` | Force in the X direction | N |
| `force_y_N` | Force in the Y direction | N |
| `force_z_N` | Force in the Z direction | N |
| `vibration_x_g` | Vibration in the X direction | g |
| `vibration_y_g` | Vibration in the Y direction | g |
| `vibration_z_g` | Vibration in the Z direction | g |
| `ae_rms_V` | Acoustic-emission RMS signal | V |

The channel order, units, and sampling rate are taken from the official
challenge page.

## Transformations

- Added the descriptive column header shown above.
- Normalized line endings to LF.
- Preserved all numeric text values and original row order.
- Applied no filtering, resampling, segmentation, scaling, normalization,
  interpolation, missing-value treatment, or rounding.
- Excluded wear measurements from the Lab 2 workflow because they are not
  needed for the learning objectives.

## Intended use

This file supports introductory CSV loading, table inspection, time-vector
construction, descriptive statistics, RMS calculation, time-domain plotting,
and evidence-based engineering interpretation in Lab 2.

This single record is not sufficient for tool-wear prediction,
remaining-useful-life estimation, fault diagnosis, or cutter-to-cutter
generalization. A waveform appearance alone does not establish wear, chatter,
anomaly, or failure.

## License and redistribution status

Kaggle identifies Version 1 of the course data source as **CC0: Public Domain**.
The course relies on that `CC0 1.0` designation for use, modification, and
redistribution of this curated subset. The subset remains subject to instructor
review before repository commit or publication.

Although CC0 does not require attribution, this data card preserves the Kaggle
mirror and original PHM Society challenge source for scholarly provenance. The
subset was curated independently for ME 5995. Its inclusion does not imply
endorsement by Kaggle, the Kaggle uploader, or the PHM Society. The repository's
MIT license applies to course-authored code and documentation; the data subset
is distributed under the stated Kaggle Version 1 CC0 basis.

## Related records

The broader course-curated `c1_selected_cuts` directory also contains complete
cuts 1 and 315 plus the cutter `c1` wear table. Those files are not required by
the core Lab 2 workflow. Their provenance and checksums are recorded in
`c1_selected_cuts/MANIFEST.csv` and the parent `DATA_CARD.md`.
