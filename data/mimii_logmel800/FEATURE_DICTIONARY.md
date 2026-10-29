# MIMII neural-network teaching features

Course-derived dataset: 800 normal recordings selected for manufacturing-sound classification.
MIMII public 1.0: https://zenodo.org/records/3384388, DOI 10.5281/zenodo.3384388.
Normal-sound four-type classification is course-derived, not the original anomaly benchmark.
Source: 0 dB factory-background mixture, microphone Channel 1, PCM16 / 32768,
16 kHz, 10 seconds. Machine IDs are local within machine type.

Each recording gives ten nonoverlapping one-second segments. For each segment:
512-sample periodic Hann STFT, 256-sample hop, no padding, squared rFFT magnitude,
32 Slaney area-normalized mel filters over 0-8000 Hz, then
10*log10(max(mel_power,1e-12)/1.0). This is not dB SPL. Output shape is 32 mel
bands by 61 frames; flatten in C order. Frame centers are 0.016 + k*0.016 seconds.

NPZ keys: X (8000,32,61), y (8000,), recording_index (8000,), recording_id (800,),
machine_id (800,), class_names (4,). Labels: 0 fan, 1 pump, 2 slider, 3 valve.
recording_index maps each segment to its parent row in recordings.csv.
Identifiers and labels are not model inputs. CSV paths are provenance, not files
students must load. The NPZ contains no waveform audio.

The supplied manifest uses seed 20261026 after sorting IDs within each type/ID:
30 train, 10 validation, 10 test per group, hence 480/160/160 recordings and
4800/1600/1600 segments. No parent or decoded content crosses partitions.
Fit one scalar mean and population SD on all training log-mel elements.
Apply the same affine transform to validation/test. No per-segment z-score or
coordinate-wise StandardScaler is applied. Prior course/pilot exposure means
this is not an untouched external generalization test.

Retain original-source attribution and CC BY-SA 4.0 terms in LICENSE_DATA.txt.
Redistribution of these derived data follows the attribution and CC BY-SA 4.0 terms above.
