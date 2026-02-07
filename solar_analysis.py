import pandas as pd

# 1. Load Data
try:
    df = pd.read_csv('weather_data.csv')
    
    print("--- MERSIN SOLAR DATA ANALYSIS ---")
    print(df.head())
    print("\n--------------------------------")

    # 2. Basic Analysis
    # Calculate Average Maximum Temperature
    avg_temp = df['Max_Temp_C'].mean()
    print(f"Average Max Temp: {avg_temp:.2f} C")

    # Calculate Total Sun Hours
    total_sun = df['Sun_Hours'].sum()
    print(f"Total Sun Hours (1 Week): {total_sun} hours")

    # 3. Efficiency Check
    # Identify days where efficiency loss is high (> 15%)
    critical_days = df[df['Efficiency_Loss'] > 0.15]

    print("\n--- CRITICAL DAYS (High Efficiency Loss) ---")
    if not critical_days.empty:
        print(critical_days[['Date', 'Max_Temp_C', 'Efficiency_Loss']])
    else:
        print("System is stable.")

    print("\n--------------------------------")
    print("Analysis Complete.")

except Exception as e:
    print(f"Error: {e}")
