import pandas as pd
import numpy as np

# Load the data
file_name = '20240712.csv'  # Assuming the data is in a CSV file
df = pd.read_csv(file_name, parse_dates=['BeginDate'])

# Split the data into forecast and actual
forecast_df = df[df['Type'] == 'forecast'].copy()
actual_df = df[df['Type'] == 'actual'].copy()

# Ensure the BeginDate column is in the correct datetime format and set it as the index
forecast_df['BeginDate'] = pd.to_datetime(forecast_df['BeginDate'])
forecast_df.set_index('BeginDate', inplace=True)

# Ensure the BeginDate column is in the correct datetime format and set it as the index
actual_df['BeginDate'] = pd.to_datetime(actual_df['BeginDate'])
actual_df.set_index('BeginDate', inplace=True)

# Resample the actual data to hourly intervals, calculating additional statistics
resampled_actual = actual_df.resample('h').agg({
    'Mw': ['mean', 'max', 'min', 'std', 'count']
})

# Flatten MultiIndex columns
resampled_actual.columns = ['_'.join(col).strip() for col in resampled_actual.columns.values]

# Not exactly an elegant solution but adding 30 minutes for index alignment
resampled_actual.index = resampled_actual.index + pd.to_timedelta(30, unit='m')

# Merge the resampled actual data with the forecast data
merged_df = forecast_df.merge(resampled_actual, left_index=True, right_index=True, how='inner')

# Prepare Data for Modeling
# Reset the index to turn the timestamp back into a column
final_df = merged_df.reset_index()

# Drop rows with missing values if any
final_df.dropna(inplace=True)

# Rename columns using a dictionary
final_df.rename(columns={
    'Mw': 'forecast',
    'Mw_mean': 'actual_mean',
    'Mw_max': 'actual_max',
    'Mw_min': 'actual_min',
    'Mw_std': 'actual_std'
}, inplace=True)
final_df.drop(columns=['Type'], inplace=True, errors='ignore')
final_df.drop(columns=['Mw_count'], inplace=True, errors='ignore')

# Display the cleaned and prepared data
print("Final DataFrame:")
print(final_df)
