import pandas as pd

class DataProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.forecast_df = None
        self.actual_df = None
        self.final_df = None

    def load_data(self):
        """Load the data from the CSV file."""
        df = pd.read_csv(self.file_name, parse_dates=['BeginDate'])
        self.forecast_df = df[df['Type'] == 'forecast'].copy()
        self.actual_df = df[df['Type'] == 'actual'].copy()

    def preprocess_data(self):
        """Preprocess the forecast and actual data."""
        # Set 'BeginDate' as the index for both dataframes
        for df in [self.forecast_df, self.actual_df]:
            df['BeginDate'] = pd.to_datetime(df['BeginDate'])
            df.set_index('BeginDate', inplace=True)

    def resample_actual_data(self):
        """Resample the actual data to hourly intervals and calculate statistics."""
        resampled_actual = self.actual_df.resample('h').agg({
            'Mw': ['mean', 'max', 'min', 'std', 'count']
        })
        
        # Flatten MultiIndex columns
        resampled_actual.columns = ['_'.join(col).strip() for col in resampled_actual.columns.values]
        
        # Align indices
        resampled_actual.index = resampled_actual.index + pd.to_timedelta(30, unit='m')

        # Merge with forecast data
        self.final_df = self.forecast_df.merge(resampled_actual, left_index=True, right_index=True, how='inner')

    def clean_final_data(self):
        """Clean the final DataFrame."""
        self.final_df.reset_index(inplace=True)
        self.final_df.dropna(inplace=True)

        # Rename columns
        self.final_df.rename(columns={
            'Mw': 'forecast',
            'Mw_mean': 'actual_mean',
            'Mw_max': 'actual_max',
            'Mw_min': 'actual_min',
            'Mw_std': 'actual_std'
        }, inplace=True)

        # Drop unnecessary columns
        self.final_df.drop(columns=['Type'], inplace=True, errors='ignore')
        self.final_df.drop(columns=['Mw_count'], inplace=True, errors='ignore')

    def process(self):
        """Process the data pipeline."""
        self.load_data()
        self.preprocess_data()
        self.resample_actual_data()
        self.clean_final_data()

    def display_final_data(self):
        """Display the cleaned and prepared data."""
        print("Final DataFrame:")
        print(self.final_df)


# Example of how to use the DataProcessor class
if __name__ == "__main__":
    # Replace 'your_file.csv' with the actual filename
    processor = DataProcessor('20240710.csv')
    processor.process()
    processor.display_final_data()
