from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('venv\model.pkl', 'rb') as f:
    model = pickle.load(f)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    # Mendapatkan data dari form input
    data = [float(request.form.get(f'price-day{i}')) for i in range(1, 11)]
    final_input = np.array(data).reshape(1, -1)
    
    # Membuat prediksi
    prediction = model.predict(final_input)
    # Mengirim hasil prediksi
    return jsonify({'prediction': round(prediction[0], 6)})

if __name__ == "__main__":
    app.run(debug=True)
