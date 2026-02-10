from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # allow React frontend to talk to backend

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Model loaded successfully!")

# --- MAPPING DICTIONARIES ---

airline_map = {
    'AirAsia': 0,
    'Air_India': 1,
    'GO_FIRST': 2,
    'Indigo': 3,
    'SpiceJet': 4,
    'Vistara': 5
}

city_map = {
    'Bangalore': 0,
    'Chennai': 1,
    'Delhi': 2,
    'Hyderabad': 3,
    'Kolkata': 4,
    'Mumbai': 5
}

time_map = {
    'Early_Morning': 1,
    'Morning': 4,
    'Afternoon': 0,
    'Evening': 2,
    'Night': 5,
    'Late_Night': 3
}

stops_map = {
    'zero': 0,
    'one': 1,
    'two_or_more': 2
}

class_map = {
    'Economy': 0,
    'Business': 1
}


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print("Received Data:", data)

        airline = airline_map[data['airline']]
        source_city = city_map[data['source']]
        destination_city = city_map[data['destination']]
        departure_time = time_map[data['departure_time']]
        arrival_time = time_map[data['arrival_time']]
        stops = stops_map[data['stops']]
        class_type = class_map[data['class_type']]
        days_left = int(data['days_left'])

        features = np.array([[
            airline,
            source_city,
            departure_time,
            stops,
            arrival_time,
            destination_city,
            class_type,
            days_left
        ]])

        prediction = model.predict(features)
        predicted_price = round(float(prediction[0]), 2)

        return jsonify({'price': predicted_price})

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
