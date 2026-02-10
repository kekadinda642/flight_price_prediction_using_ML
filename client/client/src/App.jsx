import React, { useState } from 'react';
import axios from 'axios';
import './index.css';

function App() {
  const [formData, setFormData] = useState({
    airline: 'Indigo',
    source: 'Delhi',
    destination: 'Mumbai',
    departure_time: 'Morning',
    arrival_time: 'Evening',
    stops: 'zero',
    class_type: 'Economy',
    days_left: 1
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    setPrediction(null);
    setError('');
  };

  const handlePredict = async () => {
    setLoading(true);
    setError('');
    try {
      // const response = await axios.post('http://127.0.0.1:5000/predict', formData);    this is for localhost
      const response = await axios.post('https://flight-price-prediction-using-ml-xo2z.onrender.com/predict', formData);
      setPrediction(response.data.price);
    } catch (err) {
      console.error("Error:", err);
      setError("Failed to connect to the server. Is it running?");
    }
    setLoading(false);
  };

  return (
    <>
      <div className="container">
        <h1>✈️ Flight Price Predictor</h1>
        
        {/* Row 1: Source & Destination */}
        <div className="form-row">
          <div className="form-group">
            <label>From (Source)</label>
            <select name="source" value={formData.source} onChange={handleChange}>
              <option value="Delhi">Delhi</option>
              <option value="Mumbai">Mumbai</option>
              <option value="Bangalore">Bangalore</option>
              <option value="Kolkata">Kolkata</option>
              <option value="Hyderabad">Hyderabad</option>
              <option value="Chennai">Chennai</option>
            </select>
          </div>

          <div className="form-group">
            <label>To (Destination)</label>
            <select name="destination" value={formData.destination} onChange={handleChange}>
              <option value="Mumbai">Mumbai</option>
              <option value="Delhi">Delhi</option>
              <option value="Bangalore">Bangalore</option>
              <option value="Kolkata">Kolkata</option>
              <option value="Hyderabad">Hyderabad</option>
              <option value="Chennai">Chennai</option>
            </select>
          </div>
        </div>

        {/* Row 2: Departure & Arrival Time */}
        <div className="form-row">
          <div className="form-group">
            <label>Departure Time</label>
            <select name="departure_time" value={formData.departure_time} onChange={handleChange}>
               {['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night'].map(t => <option key={t} value={t}>{t.replace('_', ' ')}</option>)}
            </select>
          </div>

          <div className="form-group">
            <label>Arrival Time</label>
            <select name="arrival_time" value={formData.arrival_time} onChange={handleChange}>
               {['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night'].map(t => <option key={t} value={t}>{t.replace('_', ' ')}</option>)}
            </select>
          </div>
        </div>

        {/* Row 3: Airline & Class */}
        <div className="form-row">
          <div className="form-group">
            <label>Airline</label>
            <select name="airline" value={formData.airline} onChange={handleChange}>
              <option value="Indigo">Indigo</option>
              <option value="Vistara">Vistara</option>
              <option value="Air_India">Air India</option>
              <option value="AirAsia">AirAsia</option>
              <option value="GO_FIRST">Go First</option>
              <option value="SpiceJet">SpiceJet</option>
            </select>
          </div>

          <div className="form-group">
             <label>Class</label>
             <select name="class_type" value={formData.class_type} onChange={handleChange}>
               <option value="Economy">Economy</option>
               <option value="Business">Business</option>
             </select>
          </div>
        </div>

        {/* Row 4: Stops & Days Left */}
        <div className="form-row">
          <div className="form-group">
            <label>Stops</label>
            <select name="stops" value={formData.stops} onChange={handleChange}>
              <option value="zero">Non-Stop</option>
              <option value="one">1 Stop</option>
              <option value="two_or_more">2+ Stops</option>
            </select>
          </div>

          <div className="form-group">
            <label>Days Left</label>
            <input 
              type="number" 
              name="days_left" 
              value={formData.days_left} 
              onChange={handleChange} 
              min="1" 
              max="50" 
            />
          </div>
        </div>

        <button onClick={handlePredict} disabled={loading}>
          {loading ? "Calculating Price..." : "Predict Price"}
        </button>

        {error && <div style={{color: '#ef4444', marginTop: '1rem', textAlign: 'center'}}>{error}</div>}

        {prediction && (
          <div className="result">
             Estimated: ₹{prediction.toLocaleString('en-IN')}
          </div>
        )}
      </div>

      <div className="signature-badge">Built by Keka</div>
    </>
  );
}

export default App;