import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

print("Slope (coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

x_test = np.array([[7]])
prediction = model.predict(x_test)
print("Prediction for x=7:", prediction[0])

joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")
