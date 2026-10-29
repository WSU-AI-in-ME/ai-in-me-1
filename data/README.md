# Course Datasets

This directory contains compact datasets prepared for ME 5995 course
activities. These subsets support instruction and are not replacements for the
complete source datasets or their original benchmark definitions.

| Dataset | Course use | Included material | Documentation and license |
|---|---|---|---|
| PHM Data Challenge 2010 | Signals, features, regression/classification, validation, trees and PCA | Selected c1 raw records and [945-cut derived feature table](phm2010/features/README.md) | [PHM 2010 README](phm2010/README.md): official provenance and third-party mirror rights note |
| MIMII | Machine-sound classification and anomaly detection | Compact mono WAV subset, recording metadata and [Lab 7 spectral features](mimii/features/lab07/README.md) | [MIMII README](mimii/README.md) and [CC BY-SA 4.0 notice](mimii/LICENSE_DATA.txt) |

## Use and redistribution

- Read the dataset-specific README before using a subset.
- Preserve the original attribution and license requirements.
- Do not interpret a course-specific task or split as the original benchmark.
- Split recordings at the documented physical grouping level to avoid data
  leakage.

The repository [MIT license](../LICENSE) covers course-authored software and
documentation. It does not replace the licenses or terms associated with
third-party datasets.


## MIMII precomputed log-mel features

[MIMII Log-Mel Teaching Dataset](mimii_logmel800/README.md): 800 normal recordings, 8000 one-second inputs and a fixed recording-level training/validation/test manifest for Lab 8/9, Practice 10 and Homework 5. The four-type classification task is course-derived. Features are supplied unstandardized; retain the documented CC BY-SA 4.0 attribution and terms.
