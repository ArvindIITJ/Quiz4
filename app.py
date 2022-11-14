from flask import Flask
from flask import request
from joblib import load

app = Flask(__name__)
model_path = "svm_gamma=0.0005_C=2.joblib"
model = load(model_path)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sum", methods=['POST'])
def sum():
    x = request.json['x']
    y = request.json['y']
    z = x + y 
    return {'sum':z}

@app.route("/predict", methods=['POST'])
def predict_digit():
    image1 = request.json['image1']
    image2 = request.json['image2']
    print("done loading")
    predicted1 = model.predict([image1])
    predicted2 = model.predict([image2])
    if int(predicted1[0])==int(predicted2[0]):
        return {"Result":True}
    else:
        return {"Result":False}

    