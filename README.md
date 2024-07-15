# ISO-NE Energy Forecast

## Description
This project harnesses data from ISO New England (ISO-NE) to provide real-time forecasts of electricity demand. By leveraging historical consumption data and employing advanced machine learning algorithms, this project aims to deliver precise and actionable demand forecasts. These insights are crucial for grid operators, energy traders, and stakeholders in optimizing electricity distribution, managing energy portfolios, and mitigating operational risks.

## Features
- Real-time forecasting of electricity demand based on historical data.
- Utilization of machine learning models such as LSTM for improved accuracy.
- Data processing pipeline to clean and prepare data for analysis.
- Visualization tools to display forecasted vs. actual demand.
- Support for handling multiple CSV files containing historical demand data.

## Installation
Follow the steps below to install and configure the project environment.

### Prerequisites
- Python 3.7 or higher
- Git
- Virtual Environment (recommended)

### Clone the Repository
Execute the following command to clone the repository to your local machine:

```bash
git clone https://github.com/andymchen566/iso-ne-energy-forecast.git
cd iso-ne-energy-forecast
```

### Set Up Virtual Environment
It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage
To run the project, follow these steps:

1. Prepare your CSV files containing historical electricity demand data and place them in the `data/` directory.
2. Execute the main script to process the data, train the model, and visualize the forecasts:

```bash
python main.py
```

## Data Processing
The project includes a `DataProcessor` class that handles data loading, preprocessing, and resampling. Ensure your CSV files include the necessary columns such as `BeginDate`, `Type`, and `Mw`.

## Model Training
The `LSTMModel` class is used to define, train, and evaluate the LSTM model for demand forecasting. Adjust hyperparameters as needed within the class to fine-tune model performance.

## Visualization
The `PredictionVisualizer` class provides tools to visualize the predicted vs. actual demand. This includes options for saving plots to specified directories.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
