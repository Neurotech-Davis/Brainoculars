## Stage II Raw Data
This directory stores the data conducted from Stage II Training.

The sampling rate of the OpenBCI Cyton board is 250Hz. This means there are 250 samples every second. Eight eeg channels are used.

File Format:
* File Name: Year-Month-Day_Hour-Minute-Second
* First line is a comma-seperated list of 32 indices
* Each preceeding line is a comma-separated list of one sample for all 8 channels
    - There should be 48,000 samples (48,001 lines total)