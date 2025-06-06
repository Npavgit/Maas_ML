from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('app/model.pkl')  # Pre-trained ML model

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('features')
    prediction = model.predict([np.array(data)])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)