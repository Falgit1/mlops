import base64
import os

import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from segmentation.pipeline.prediction import Prediction
from segmentation.utils.common import decode_image

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "background_image.jpg"
        self.classifier = Prediction(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template(r"index.html")


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def train_route():
    os.system("python main.py")
    return "Training done successfully!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predict_route():
    image_data = request.json['image']
    decode_image(image_data, "input_image.jpg")

    # Load image with PIL and convert to numpy
    input_img = Image.open("input_image.jpg").convert("RGB")
    input_img = np.array(input_img)

    result_img = clApp.classifier.predict(input_img)

    # Convert result image to base64
    from io import BytesIO
    buffered = BytesIO()
    Image.fromarray(result_img.astype(np.uint8)).save(buffered, format="JPEG")
    result_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return jsonify({"result_image": result_base64})


#
# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     image = request.json['image']
#     decode_image(image, clApp.filename)
#     result = clApp.classifier.predict()
#     return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    # app.run(host='0.0.0.0', port=8080) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    app.run(host='0.0.0.0', port=8080)  # for AZURE
