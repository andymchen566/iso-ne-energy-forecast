# ISO-NE Energy Forecast

## Description
This library harnesses data from ISO New England (ISO-NE) and alternative data sources to provide real-time forecasts of electricity demand, supply, and clearing price. By leveraging historical data and employing machine learning techniques, this project aims to deliver precise and actionable trading signals when potential market mispricing occurs. These insights are crucial for energy traders in optimizing their intraday market-making and position management, for both delta-one and non-linear products. 

## Features
- Uses LSTM for Temporal Dependency Solving

## Next Steps
[2024-07-14] The current state only accounts for temporal dependency and is limited in predictive power. 
[2024-07-20] The model should ultimately allow a power trader to forecast the price of electricity based on a stack model, determined by the price-setting resource. 
### To-Do's: 
[2024-07-14] DEMAND SIDE
- Feature extraction (Temperature, humidity, precipitation, etc.)
- Hyperparameter tuning (# hidden layers, # neurons per layer, search techniques; activation and loss optimization)
- Investigate other algorithms and compare (RNN, GRU)
- Investigate classical statistics (Generalized Linear Models; ARMA and GARCH Models)
[2024-07-20] SUPPLY SIDE 
- Create forecasting for each resource (solar, wind, geothermal, etc)
- Combine forecasted demand with forecasted supply from each resource, as well as offers submitted by each resource provider, to predict the clearing price
[2024-07-21] PRICING TAIL RISK
- Investigate tail risk events (hurricanes warnings & occurences; droughts; heat waves; etc.) including forecasts (ISO-NE; alt data) and actual impact
- Service disruptions from specific resources, either due idiosyncratic (malfunctions) or systemic factors (hurricane warning leading to evacuation of a plant); Ability to accurately forecast the tightening of energy markets due to supply disruptions or demand surge (and vice versa)


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

## Stack Pricing Model
The `ElectricityPricingModel` class provides methods for adding resource types, offer prices, and capacities. This attempts to simulate ISO-NE's price-setting model based on final demand. 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
