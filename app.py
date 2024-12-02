from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/', methods=['GET'])
def home():
    """Homepage route"""
    return jsonify({"message": "Welcome to the ML model API!"})

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to make predictions.
    Expects JSON payload with 'inputs', a list of input features.
    """
    try:
        data = request.get_json()
        inputs = data.get('inputs')

        if not inputs or not isinstance(inputs, list):
            return jsonify({"error": "Invalid input format. Provide 'inputs' as a list."}), 400

        inputs = np.array(inputs).reshape(1, -1)
        predictions = model.predict(inputs)

        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
