import matplotlib.pyplot as plt
import pandas as pd
import os

class PredictionVisualizer:
    def __init__(self, model, scaler):
        self.model = model
        self.scaler = scaler

    def visualize(self, X_test, y_test, start_date, freq='H', save_dir=None):
        """Visualizes the predicted vs actual values."""
        # Get predictions from the model
        predictions = self.model.predict(X_test)

        # Inverse transform the scaled predictions and actual values
        predictions_inverse = self.scaler.inverse_transform(predictions)
        y_test_inverse = self.scaler.inverse_transform(y_test.reshape(-1, 1))

        # Create a time index for plotting
        time_index = pd.date_range(start=start_date, periods=len(y_test_inverse), freq=freq)

        # Plotting
        fig, ax = plt.subplots(figsize=(18, 6))
        ax.plot(time_index, y_test_inverse, label='Actual', color='blue')
        ax.plot(time_index, predictions_inverse, label='Predicted', color='red', linestyle='--')
        ax.set_title('Actual vs Predicted Electricity Demand')
        ax.set_xlabel('Date and Time')
        ax.set_ylabel('Electricity Demand (Mw)')
        ax.legend()
        ax.grid()

        # Save the plot if a save directory is provided
        if save_dir:
            os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist
            plt.savefig(os.path.join(save_dir, 'predictions_plot.png'))
            plt.close()  # Close the figure to free up memory
            print(f"Plot saved to {os.path.join(save_dir, 'predictions_plot.png')}")
        else:
            plt.show()  # Always display the plot interactively
 