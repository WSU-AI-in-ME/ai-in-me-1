# Reproduce PHM 2010 scalar features

This utility reproduces the [course feature table](../../../data/phm2010/features/README.md)
from PHM source records that you obtain separately under applicable terms.
It does not download data, train models, assign splits or produce spectral features.

Use Python 3.12 (validated with 3.12.14) and the pinned NumPy version:

```bash
python -m pip install -r scripts/data_curation/phm2010/requirements.txt
```

Extract the source training cutters into this layout. Signals have seven numeric
columns without a header; wear files have `cut,flute_1,flute_2,flute_3` headers.
The selected public c1 subset alone cannot reproduce the 945-row table.

```text
PHM_SOURCE/
  c1/
    c1_wear.csv
    c1/c_1_001.csv ... c_1_315.csv
  c4/
    c4_wear.csv
    c4/c_4_001.csv ... c_4_315.csv
  c6/
    c6_wear.csv
    c6/c_6_001.csv ... c_6_315.csv
```

Run from the repository root, replacing `PHM_SOURCE` with your extracted directory:

```bash
python scripts/data_curation/phm2010/build_features.py --source PHM_SOURCE --output output/phm2010_features.csv --workers 4
```

Choose a new output path outside the source directory. The program preserves source
files and refuses to overwrite an existing output or `.partial` file. Invalid
records fail explicitly with cutter/cut context; an incomplete output is never
renamed to the final filename. Inventory errors identify the affected cutter.

Each row uses all samples of one cut at the documented 50 kHz/channel. Mean,
sample SD (`ddof=1`), raw RMS, peak-to-peak, raw crest factor and Pearson kurtosis
(`fisher=False, bias=True`) follow the [dictionary](../../../data/phm2010/features/DATA_DICTIONARY.md).
Stable scaling in RMS and kurtosis preserves the mathematical definitions.
Wear mean/max and the 50/150 µm class boundaries use the original three flute
measurements. There is no cropping, sample replacement or QC-based exclusion.

The expected result is 945 rows and 56 columns, sorted by c1/c4/c6 and cut.
Class 0/1/2 counts are 20/762/163 (c1: 6/280/29; c4: 11/258/46; c6: 3/224/88).
The source hash depends on exact source bytes, including line endings; different
source copies may not give the same hash even when their numeric values agree.
Exact CSV reproducibility was checked with the documented source bytes and pinned
runtime. Other platforms or numerical-library versions may differ in final digits.

See the [PHM source and rights note](../../../data/phm2010/README.md). The code's
[MIT license](../../../LICENSE) does not grant rights to underlying PHM data.
