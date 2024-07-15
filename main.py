import pandas as pd
import os
from data.data_processor import DataProcessor
from engine.forecast import LSTMModel
from engine.visualizer import PredictionVisualizer  # Import the visualizer

def process_iso_data():
    # Get the current directory
    directory = os.getcwd()  # or specify the path
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    all_dfs = []  # List to store DataFrames

    # Process each CSV file
    for csv_file in csv_files:
        print(f"Processing {csv_file}...")
        processor = DataProcessor(csv_file)
        processor.process()
        all_dfs.append(processor.final_df)

    # Concatenate all DataFrames
    merged_df = pd.concat(all_dfs).sort_values(by='BeginDate').reset_index(drop=True)

    return merged_df  # Return the merged DataFrame

if __name__ == "__main__":
    # Process and merge the ISO data
    merged_df = process_iso_data()
    
    # Initialize and train the LSTM model
    lstm_model = LSTMModel(merged_df)
    
    # Preprocess data
    X, y = lstm_model.preprocess_data()
    
    # Split the data into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)
    
    # Build the model
    lstm_model.build_model(input_shape=(X_train.shape[1], X_train.shape[2]))
    
    # Train the model
    lstm_model.train_model(X_train, y_train)
    
    # Evaluate the model
    lstm_model.evaluate_model(X_test, y_test)
    
    # Visualize predictions
    visualizer = PredictionVisualizer(lstm_model.model, lstm_model.scaler)
    visualizer.visualize(X_test, y_test, start_date='2024-07-10', save_dir='plots')  # Specify save directory

