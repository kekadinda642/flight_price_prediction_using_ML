from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
<<<<<<< HEAD
CORS(app)  # This allows your React frontend to talk to this Python backend

# 1. Load the trained model
=======
CORS(app)  

>>>>>>> 7c842bfa8d33d8ba2bf4ad83a6155892e6c9f2d9
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Model loaded successfully!")

<<<<<<< HEAD
# --- MAPPING DICTIONARIES ---
# These translate the text from the website into numbers for the model.
# (Based on standard alphabetical encoding. We can adjust if needed).
=======

>>>>>>> 7c842bfa8d33d8ba2bf4ad83a6155892e6c9f2d9

airline_map = {
    'AirAsia': 0, 'Air_India': 1, 'GO_FIRST': 2, 'Indigo': 3, 
    'SpiceJet': 4, 'Vistara': 5
}

city_map = {
    'Bangalore': 0, 'Chennai': 1, 'Delhi': 2, 'Hyderabad': 3, 
    'Kolkata': 4, 'Mumbai': 5
}

<<<<<<< HEAD
# Departure/Arrival times usually follow this specific order in this dataset
=======

>>>>>>> 7c842bfa8d33d8ba2bf4ad83a6155892e6c9f2d9
time_map = {
    'Early_Morning': 1, 'Morning': 4, 'Afternoon': 0, 
    'Evening': 2, 'Night': 5, 'Late_Night': 3
} 
<<<<<<< HEAD
# Note: If this mapping is wrong, your predictions will just be slightly off. 
# We can fix it by checking your notebook later.
=======

>>>>>>> 7c842bfa8d33d8ba2bf4ad83a6155892e6c9f2d9

stops_map = {
    'zero': 0, 'one': 1, 'two_or_more': 2
}

class_map = {
    'Economy': 0, 'Business': 1
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
<<<<<<< HEAD
        # 1. Get data from the frontend
        data = request.json
        print("Received Data:", data) # Print what we got for debugging

        # 2. Extract and Convert (The Translation Step)
=======
        
        data = request.json
        print("Received Data:", data) 

        
>>>>>>> 7c842bfa8d33d8ba2bf4ad83a6155892e6c9f2d9
        airline = airline_map[data['airline']]
        source_city = city_map[data['source']]
        destination_city = city_map[data['destination']]
        departure_time = time_map[data['departure_time']]
        arrival_time = time_map[data['arrival_time']]
        stops = stops_map[data['stops']]
        class_type = class_map[data['class_type']]
        days_left = int(data['days_left'])

<<<<<<< HEAD
        # 3. Create the row of data exactly how the model expects it
        # Column order: ['airline', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'class', 'days_left']
=======
        
>>>>>>> 7c842bfa8d33d8ba2bf4ad83a6155892e6c9f2d9
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

<<<<<<< HEAD
        # 4. Make Prediction
        prediction = model.predict(features)
        
        # 5. Send back the result
=======
        
        prediction = model.predict(features)
        
        
>>>>>>> 7c842bfa8d33d8ba2bf4ad83a6155892e6c9f2d9
        predicted_price = round(prediction[0], 2)
        return jsonify({'price': predicted_price})

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)