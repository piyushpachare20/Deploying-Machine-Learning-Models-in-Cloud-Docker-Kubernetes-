import joblib
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generate sample data
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")
