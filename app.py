from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model once (VERY IMPORTANT)
model = joblib.load('model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_values', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        form = request.form

        # Collect inputs in correct order
        features = [
            float(form['aluminium']),
            float(form['ammonia']),
            float(form['arsenic']),
            float(form['barium']),
            float(form['cadmium']),
            float(form['chloramine']),
            float(form['chromium']),
            float(form['copper']),
            float(form['flouride']),
            float(form['bacteria']),
            float(form['viruses']),
            float(form['lead']),
            float(form['nitrates']),
            float(form['nitrites']),
            float(form['mercury']),
            float(form['perchlorate']),
            float(form['radium']),
            float(form['selenium']),
            float(form['silver']),
            float(form['uranium'])
        ]

        # Prediction (2D input required)
        prediction = model.predict([features])[0] 

        return render_template(
            'get_details.html',
            result=int(prediction))

    return render_template('get_details.html')