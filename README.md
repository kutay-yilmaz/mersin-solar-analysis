# Mersin Solar Data Analysis

Simple data analysis script using **Python** and **Pandas**.

I created this to analyze sample weather data (CSV) for Mersin and calculate efficiency losses in Solar PV systems due to high temperatures.

## Dependencies
You need the `pandas` library to run this script.
```bash
pip install pandas
How It Works
Reads Data: Loads weather_data.csv containing temperature and sun hours.

Calculates Stats: Computes average temperature and total sun duration.

Detects Efficiency Loss: Identifies days where temperature exceeds the threshold.

Sample Output
Plaintext

--- MERSIN SOLAR DATA ANALYSIS ---
Average Max Temp: 33.30 C
Total Sun Hours (1 Week): 66.4 hours

--- CRITICAL DAYS (High Efficiency Loss) ---
         Date  Max_Temp_C  Efficiency_Loss
6  2025-06-07        36.0             0.16
Author: Kutay Yilmaz

Electrical & Electronics Engineering Student
