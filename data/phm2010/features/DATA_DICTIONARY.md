# PHM 2010 feature data dictionary

[Feature dataset and default predictors](README.md) · [CSV](phm2010_features.csv)

One row is one full recorded cut. There are 56 columns; 42 are sensor-derived
features. Roles below are disjoint; the approved 11 default predictors are marked
Yes. All features are available for learning, but are not automatically model
inputs. The defaults use physical interpretation and known redundancy, not
full-dataset performance optimization.

For one channel, let `x_i` be sample i, `n` the sample count, `m` its raw mean,
and `fs = 50000 Hz`. Force XYZ uses N, Vibration XYZ uses g, and AE-RMS uses V.
A unit of 1 denotes a dimensionless scalar; identifiers have no physical unit.
AE-RMS is the recorded channel, so its `rms` feature summarizes that channel.

| Feature | Definition | Convention |
|---|---|---|
| mean | `sum(x_i)/n` | Raw arithmetic mean |
| sd | `sqrt(sum((x_i-m)^2)/(n-1))` | Sample SD, `ddof=1` |
| rms | `sqrt(sum(x_i^2)/n)` | No mean removal |
| peak_to_peak | `max(x_i)-min(x_i)` | Full-record range |
| crest_factor | `max(abs(x_i))/rms` | Raw crest factor |
| kurtosis | `mean((x_i-m)^4)/mean((x_i-m)^2)^2` | Pearson; `fisher=False, bias=True` |

Known redundancy: `rms^2 = mean^2 + (n-1)/n * sd^2`. Redundant educational
columns are retained. Crest factor requires nonzero RMS; kurtosis requires
nonzero variance. The supplied table contains no missing or nonfinite values.

## Metadata

| Column | Role | Engineering meaning and definition | Unit | Default predictor |
|---|---|---|---|---|
| `cutter_id` | metadata | Physical cutter identity, c1/c4/c6; grouping metadata | 1 | No |
| `cut_number` | metadata | Original cut sequence 1..315; not a default predictor | 1 | No |
| `source_file` | metadata | Original path relative to the original PHM archive layout; source files are not included here | 1 | No |
| `source_sha256` | metadata | SHA-256 of the exact original signal bytes read | 1 | No |
| `n_samples` | metadata | Full-record samples in each of seven channels | samples | No |
| `sample_rate_hz` | metadata | Documented 50000 per channel; not independently measured from CSV | Hz | No |
| `duration_s` | metadata | n/fs; record coverage duration | s | No |
| `last_sample_time_s` | metadata | (n-1)/fs; timestamp of final sample | s | No |

## Core sensor features (28)

| Column | Role | Engineering meaning and definition | Unit | Default predictor |
|---|---|---|---|---|
| `force_x_mean` | core_educational_features | Force X mean; sum(x)/n | N | Yes |
| `force_x_sd` | core_educational_features | Force X sd; sqrt(sum((x-mean)^2)/(n-1)); ddof=1 | N | Yes |
| `force_x_rms` | core_educational_features | Force X rms; sqrt(sum(x^2)/n); raw, no mean removal | N | No |
| `force_x_peak_to_peak` | core_educational_features | Force X peak to peak; max(x)-min(x) | N | No |
| `force_y_mean` | core_educational_features | Force Y mean; sum(x)/n | N | Yes |
| `force_y_sd` | core_educational_features | Force Y sd; sqrt(sum((x-mean)^2)/(n-1)); ddof=1 | N | Yes |
| `force_y_rms` | core_educational_features | Force Y rms; sqrt(sum(x^2)/n); raw, no mean removal | N | No |
| `force_y_peak_to_peak` | core_educational_features | Force Y peak to peak; max(x)-min(x) | N | No |
| `force_z_mean` | core_educational_features | Force Z mean; sum(x)/n | N | Yes |
| `force_z_sd` | core_educational_features | Force Z sd; sqrt(sum((x-mean)^2)/(n-1)); ddof=1 | N | Yes |
| `force_z_rms` | core_educational_features | Force Z rms; sqrt(sum(x^2)/n); raw, no mean removal | N | No |
| `force_z_peak_to_peak` | core_educational_features | Force Z peak to peak; max(x)-min(x) | N | No |
| `vibration_x_mean` | core_educational_features | Vibration X mean; sum(x)/n | g | No |
| `vibration_x_sd` | core_educational_features | Vibration X sd; sqrt(sum((x-mean)^2)/(n-1)); ddof=1 | g | Yes |
| `vibration_x_rms` | core_educational_features | Vibration X rms; sqrt(sum(x^2)/n); raw, no mean removal | g | No |
| `vibration_x_peak_to_peak` | core_educational_features | Vibration X peak to peak; max(x)-min(x) | g | No |
| `vibration_y_mean` | core_educational_features | Vibration Y mean; sum(x)/n | g | No |
| `vibration_y_sd` | core_educational_features | Vibration Y sd; sqrt(sum((x-mean)^2)/(n-1)); ddof=1 | g | Yes |
| `vibration_y_rms` | core_educational_features | Vibration Y rms; sqrt(sum(x^2)/n); raw, no mean removal | g | No |
| `vibration_y_peak_to_peak` | core_educational_features | Vibration Y peak to peak; max(x)-min(x) | g | No |
| `vibration_z_mean` | core_educational_features | Vibration Z mean; sum(x)/n | g | No |
| `vibration_z_sd` | core_educational_features | Vibration Z sd; sqrt(sum((x-mean)^2)/(n-1)); ddof=1 | g | Yes |
| `vibration_z_rms` | core_educational_features | Vibration Z rms; sqrt(sum(x^2)/n); raw, no mean removal | g | No |
| `vibration_z_peak_to_peak` | core_educational_features | Vibration Z peak to peak; max(x)-min(x) | g | No |
| `ae_rms_mean` | core_educational_features | AE-RMS mean; sum(x)/n | V | Yes |
| `ae_rms_sd` | core_educational_features | AE-RMS sd; sqrt(sum((x-mean)^2)/(n-1)); ddof=1 | V | Yes |
| `ae_rms_rms` | core_educational_features | AE-RMS rms; sqrt(sum(x^2)/n); raw, no mean removal | V | No |
| `ae_rms_peak_to_peak` | core_educational_features | AE-RMS peak to peak; max(x)-min(x) | V | No |

## Exploratory sensor features (14)

| Column | Role | Engineering meaning and definition | Unit | Default predictor |
|---|---|---|---|---|
| `force_x_crest_factor` | exploratory_features | Force X crest factor; max(abs(x))/raw_RMS | 1 | No |
| `force_x_kurtosis` | exploratory_features | Force X kurtosis; mean((x-mean)^4)/mean((x-mean)^2)^2; Pearson, fisher=False, bias=True | 1 | No |
| `force_y_crest_factor` | exploratory_features | Force Y crest factor; max(abs(x))/raw_RMS | 1 | No |
| `force_y_kurtosis` | exploratory_features | Force Y kurtosis; mean((x-mean)^4)/mean((x-mean)^2)^2; Pearson, fisher=False, bias=True | 1 | No |
| `force_z_crest_factor` | exploratory_features | Force Z crest factor; max(abs(x))/raw_RMS | 1 | No |
| `force_z_kurtosis` | exploratory_features | Force Z kurtosis; mean((x-mean)^4)/mean((x-mean)^2)^2; Pearson, fisher=False, bias=True | 1 | No |
| `vibration_x_crest_factor` | exploratory_features | Vibration X crest factor; max(abs(x))/raw_RMS | 1 | No |
| `vibration_x_kurtosis` | exploratory_features | Vibration X kurtosis; mean((x-mean)^4)/mean((x-mean)^2)^2; Pearson, fisher=False, bias=True | 1 | No |
| `vibration_y_crest_factor` | exploratory_features | Vibration Y crest factor; max(abs(x))/raw_RMS | 1 | No |
| `vibration_y_kurtosis` | exploratory_features | Vibration Y kurtosis; mean((x-mean)^4)/mean((x-mean)^2)^2; Pearson, fisher=False, bias=True | 1 | No |
| `vibration_z_crest_factor` | exploratory_features | Vibration Z crest factor; max(abs(x))/raw_RMS | 1 | No |
| `vibration_z_kurtosis` | exploratory_features | Vibration Z kurtosis; mean((x-mean)^4)/mean((x-mean)^2)^2; Pearson, fisher=False, bias=True | 1 | No |
| `ae_rms_crest_factor` | exploratory_features | AE-RMS crest factor; max(abs(x))/raw_RMS | 1 | No |
| `ae_rms_kurtosis` | exploratory_features | AE-RMS kurtosis; mean((x-mean)^4)/mean((x-mean)^2)^2; Pearson, fisher=False, bias=True | 1 | No |

## Original wear measurements

| Column | Role | Engineering meaning and definition | Unit | Default predictor |
|---|---|---|---|---|
| `wear_flute_1_um` | original_targets | Original flute wear after the cut; source 10^-3 mm equals µm numerically; not a predictor | µm | No |
| `wear_flute_2_um` | original_targets | Original flute wear after the cut; source 10^-3 mm equals µm numerically; not a predictor | µm | No |
| `wear_flute_3_um` | original_targets | Original flute wear after the cut; source 10^-3 mm equals µm numerically; not a predictor | µm | No |

## Derived continuous targets

| Column | Role | Engineering meaning and definition | Unit | Default predictor |
|---|---|---|---|---|
| `wear_mean_um` | continuous_targets | Arithmetic mean of three original flute measurements | µm | No |
| `wear_max_um` | continuous_targets | Maximum of three original flute measurements | µm | No |

## Course-defined categorical target

| Column | Role | Engineering meaning and definition | Unit | Default predictor |
|---|---|---|---|---|
| `wear_level` | categorical_targets | 0: mean<=50 µm; 1: 50<mean<150 µm; 2: mean>=150 µm; instructional only | 1 | No |

Wear levels are instructional categories, not official PHM severity labels.
The [README](README.md) provides source attribution, rights notes and grouping limitations.
