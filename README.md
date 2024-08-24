# Climate Extreme Prediction

This project predicts `Extreme cold` values using a linear regression model based on other climate-related features such as `Moderate cold`, `Moderate heat`, and `Extreme heat`.

## Dataset
The dataset is in CSV format and contains climate data for various countries from the year 2015. The features used in the model include:
- Moderate cold
- Moderate heat
- Extreme heat

The target variable is:
- Extreme cold

## Project Structure
- **climate_data.csv**: The dataset containing climate data for various countries.
- **climate_extreme_prediction.py**: The Python script that trains the model and makes predictions.

## Installation

1. Ensure you have Python installed 
2. Install the required libraries:
   ```bash
   pip install pandas scikit-learn
