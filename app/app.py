from base64 import b64decode
from flask import Flask, render_template, request
import io
from keras.preprocessing.image import img_to_array
import model
import numpy as np
from PIL import Image

app = Flask(__name__)
HOST="0.0.0.0"
PORT=3000

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shape_model")
def shape_model():
    encoded_img = request.args["img"]
    encoded_img = encoded_img.replace("data:image/png;base64,", "", 1)
    img = b64decode(encoded_img)
    img = Image.open(io.BytesIO(img))
    img = img.convert("L")
    img = img_to_array(img)
    prediction = model.run_model(img)
    return prediction

if __name__ == "__main__":
    app.run(HOST, port=PORT)