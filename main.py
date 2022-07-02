# flask, scikit-learn, pandas, pickle-mixin

import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
data = pd.read_csv("Clean_Houses_Data.csv")
pipeline = pickle.load(open("LR_model.pkl", "rb"))


@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)


@app.route("/predict", methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')
    # print(location, bhk, bath, sqft)

    # the order of columns in below new dataframe should be same as that of original dataframe
    inp = pd.DataFrame([[location, sqft, float(bath), float(bhk)]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = pipeline.predict(inp)[0] * 1e5
    # return str(np.round(("{:,}".format(prediction)), 0))
    return "{:,}".format(round(prediction))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
