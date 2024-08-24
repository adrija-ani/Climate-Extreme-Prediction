import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r"climate_data.csv")

X = df[['Moderate cold', 'Moderate heat', 'Extreme heat']]
y = df['Extreme cold']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

new_data = [[7.0, 0.5, 0.3]]
predicted_cold = model.predict(new_data)
print(f"Predicted 'Extreme cold': {predicted_cold[0]:.2f}")
