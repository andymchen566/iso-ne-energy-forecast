import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

class LSTMModel:
    def __init__(self, data):
        self.data = data
        self.model = None
        self.scaler = MinMaxScaler()

    def preprocess_data(self):
        """Prepares the data for LSTM training."""
        features = self.data[['forecast', 'actual_mean', 'actual_max', 'actual_min', 'actual_std']].values
        target = self.data['actual_mean'].values  # Assuming we want to predict actual_mean

        # Scale the features and target
        features_scaled = self.scaler.fit_transform(features)
        target_scaled = self.scaler.fit_transform(target.reshape(-1, 1)).flatten()

        # Create sequences for LSTM
        X, y = [], []
        sequence_length = 24  # Example: Use the past 24 hours to predict the next hour
        for i in range(len(features_scaled) - sequence_length):
            X.append(features_scaled[i:i + sequence_length])
            y.append(target_scaled[i + sequence_length])
        
        return np.array(X), np.array(y)

    def build_model(self, input_shape):
        """Builds the LSTM model."""
        self.model = Sequential()
        self.model.add(LSTM(64, return_sequences=True, input_shape=input_shape))
        # self.model.add(Dropout(0.2)) 
        self.model.add(LSTM(64, return_sequences=True))
        # self.model.add(Dropout(0.2))
        self.model.add(LSTM(64))
        # self.model.add(Dropout(0.2))
        self.model.add(Dense(32))
        self.model.add(Dense(1))

        self.model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    def train_model(self, X_train, y_train):
        """Trains the LSTM model."""
        early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
        self.model.fit(X_train, y_train, batch_size=1, epochs=25, validation_split=0.1, callbacks=[early_stopping])

    def evaluate_model(self, X_test, y_test):
        """Evaluates the model."""
        loss, mae = self.model.evaluate(X_test, y_test)
        print(f"Model Loss: {loss}, Model MAE: {mae}")



