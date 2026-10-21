# Lab 7 Feature Dictionary: Frozen v1

Derived teaching features, built and verified on 2026-10-20.
One row is one existing MIMII fan id_06 recording. No new source audio selection.

## Spectral convention

PCM16 samples are converted to float64 by division by 32768.0. No per-recording normalization.
All 160000 samples are used. A periodic Hann window (fftbins=True) and full-record
one-sided density periodogram use fs=16000, nfft=160000 and detrend=False.
Each PSD bin is included once, with df=0.1 Hz. Band power is sum(PSD bins)*df.
Each feature is 10*log10(max(band_power,1e-12)/1.0). Reference: one squared digital
full-scale unit. Features are log digital band power in dB relative to this reference,
not Pa or dB SPL. Standardization for modeling is fitted separately on normal training only.

| Feature column | Lower Hz | Upper Hz | Interval |
|---|---:|---:|---|
| log_power_0000_0500 | 0 | 500 | lower <= f < upper |
| log_power_0500_1000 | 500 | 1000 | lower <= f < upper |
| log_power_1000_1500 | 1000 | 1500 | lower <= f < upper |
| log_power_1500_2000 | 1500 | 2000 | lower <= f < upper |
| log_power_2000_2500 | 2000 | 2500 | lower <= f < upper |
| log_power_2500_3000 | 2500 | 3000 | lower <= f < upper |
| log_power_3000_3500 | 3000 | 3500 | lower <= f < upper |
| log_power_3500_4000 | 3500 | 4000 | lower <= f < upper |
| log_power_4000_4500 | 4000 | 4500 | lower <= f < upper |
| log_power_4500_5000 | 4500 | 5000 | lower <= f < upper |
| log_power_5000_5500 | 5000 | 5500 | lower <= f < upper |
| log_power_5500_6000 | 5500 | 6000 | lower <= f < upper |
| log_power_6000_6500 | 6000 | 6500 | lower <= f < upper |
| log_power_6500_7000 | 6500 | 7000 | lower <= f < upper |
| log_power_7000_7500 | 7000 | 7500 | lower <= f < upper |
| log_power_7500_8000 | 7500 | 8000 | lower <= f <= upper |

## Metadata columns: excluded from model inputs

Only the 16 columns above are predictors. recording_id and source_file link provenance;
condition and label encode file-level normal=0/anomaly=1; machine_type, machine_id and
snr_db identify source conditions; split gives the frozen partition; source_sha256
checks the exact curated WAV bytes. IDs/labels/splits must never enter the feature matrix.

## Provenance, attribution and license

Original source: MIMII public 1.0, DOI https://doi.org/10.5281/zenodo.3384388 .
Purohit et al., Sound Dataset for Malfunctioning Industrial Machine Investigation and
Inspection, 2019, https://arxiv.org/abs/1909.09347 .
Original authors: Harsh Purohit, Ryo Tanabe, Kenji Ichige, Takashi Endo, Yuki Nikaido,
Kaori Suefusa and Yohei Kawaguchi (Hitachi, Ltd.).
Existing course conversion: source microphone Channel 1 only, mono PCM16, no amplitude
normalization/cropping/resampling; source abnormal directory is mapped to anomaly.
Course-derived changes: deterministic 16-band feature extraction and course-specific split.
Full source filenames and curated-file SHA-256 are retained per row in CSV/manifest.
The derived dataset retains CC BY-SA 4.0 attribution/ShareAlike requirements.
See [LICENSE_DATA.txt](LICENSE_DATA.txt). The general software license does not replace data terms.
The original source was not newly downloaded; local course subset and metadata were checked.

This teaching table is shared under CC BY-SA 4.0; it is not an official benchmark split.
