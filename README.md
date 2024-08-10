# ISO-NE Energy Forecast

## Overview
This repository provides a sophisticated toolkit for forecasting electricity demand, supply, and clearing prices in the ISO New England (ISO-NE) energy market. By integrating data from ISO-NE with other relevant sources and leveraging advanced machine learning techniques, this project delivers high-precision trading signals. These signals are invaluable for energy traders seeking to optimize their market-making strategies and manage positions in both delta-1 and nonlinear products.

## Key Features
- **Advanced Time Series Modeling**: Utilizes Long Short-Term Memory (LSTM) networks to capture temporal dependencies in electricity demand.
- **Comprehensive Data Processing**: Streamlined data loading, preprocessing, and resampling to ensure high-quality inputs.
- **Actionable Insights**: Generates trading signals by detecting market mispricing, enabling more informed intraday trading decisions.
- **Flexible Stack Pricing Simulation**: Models ISO-NE's price-setting mechanism, allowing users to predict clearing prices based on resource offers and demand forecasts.
- **Visual Analysis Tools**: Built-in visualization to compare predicted versus actual demand, facilitating quick assessment of model performance.

## Installation

To get started with the project, follow the steps below:

### Prerequisites
- Python 3.7 or higher
- Git
- Virtual Environment (recommended)

## Usage

### Data Preparation
Place your historical electricity demand data in CSV format in the `data/` directory. Ensure your files contain the necessary columns such as `BeginDate`, `Type`, and `Mw`.

### Running the Project
To process the data, train the model, and visualize the forecasts, run:

python main.py

### Customization
- **Data Processing**: The `DataProcessor` class manages data loading, preprocessing, and resampling tasks.
- **Model Training**: The `LSTMModel` class handles the definition, training, and evaluation of the LSTM model. Adjust hyperparameters directly within the class to optimize performance.
- **Visualization**: Use the `PredictionVisualizer` class to generate and save plots that compare predicted demand against actual values.

## Advanced Modeling

### Stack Pricing Model
The `ElectricityPricingModel` class provides a robust framework for simulating ISO-NE's price-setting model. By incorporating forecasted demand, supply from each resource type (e.g., solar, wind, geothermal), and submitted offers, this model predicts the clearing price.

### Tail Risk Analysis
An essential feature under development is the modeling of pricing tail risks, such as those caused by extreme weather events (hurricanes, heat waves, etc.). Accurate forecasting of such risks will enhance the ability to predict market tightness due to supply disruptions or demand surges.

## Future Enhancements

The current model focuses primarily on temporal dependencies in electricity demand forecasting. Future developments will expand its scope and predictive power, particularly in supply forecasting and pricing dynamics.

### Demand-Side Improvements
- **Feature Engineering**: Incorporate additional features such as temperature, humidity, and precipitation.
- **Hyperparameter Optimization**: Refine the model by tuning hyperparameters, experimenting with hidden layers, neuron counts, and optimization algorithms.
- **Model Comparison**: Explore alternative algorithms (e.g., RNN, GRU) and classical statistical methods (e.g., Generalized Linear Models, ARMA, GARCH).

### Supply-Side Forecasting
- **Resource-Specific Forecasts**: Develop models for each energy resource type (solar, wind, geothermal, etc.).
- **Integrated Supply-Demand Modeling**: Combine demand forecasts with resource-specific supply predictions to estimate clearing prices more accurately.

### Pricing Tail Risk
- **Extreme Event Analysis**: Study the impact of extreme events like hurricanes and droughts on electricity prices, incorporating both forecast data and historical occurrences.
- **Supply Disruption Modeling**: Enhance the model's ability to predict the effects of idiosyncratic and systemic disruptions on market prices.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

By focusing on these advanced features and future enhancements, this project is positioned as a powerful tool for energy market participants, providing actionable insights and robust forecasting capabilities tailored to the complexities of the ISO-NE market.
