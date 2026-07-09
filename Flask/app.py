from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prediction')
def prediction():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    try:
        life = float(request.form['life'])
        expected = float(request.form['expected'])
        mean = float(request.form['mean'])
        income = float(request.form['income'])

        features = np.array([[life,
                              expected,
                              mean,
                              income]])

        prediction = model.predict(features)[0]

        return render_template(
            'index.html',
            prediction_text=f'Predicted Human Development Index (HDI): {prediction:.3f}'
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)