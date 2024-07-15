import pandas as pd
from data_processor import DataProcessor  # Adjust the import according to your structure

def main():
    # Process the first file
    processor1 = DataProcessor('20240712.csv')
    processor1.process()
    df1 = processor1.final_df

    # Process the second file
    processor2 = DataProcessor('20240711.csv')
    processor2.process()
    df2 = processor2.final_df

    # Concatenate the two DataFrames
    merged_df = pd.concat([df1, df2]).sort_values(by='BeginDate').reset_index(drop=True)

    # Display the merged DataFrame
    print("Merged DataFrame:")
    print(merged_df)

if __name__ == "__main__":
    main()
