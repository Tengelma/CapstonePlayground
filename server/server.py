from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
app = Flask(__name__)
CORS(app)

@app.route('/graph', methods=['POST'])
def graph():
    content = request.json
    slope = content["slope"]
    y_intercept = content["yIntercept"]
    x = get_x(100)
    y = get_y(x, slope, y_intercept)
    create_fig(x, y)
    img = {"image": serialize_fig()}
    return jsonify(img)

def get_x(range: int):
    return np.arange(range)

def get_y(x, slope: int, y_intercept: int):
    calculate = lambda x: x * slope + y_intercept
    return calculate(x)

def create_fig(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([0, 100, 0, 100])
    plt.savefig('./temp/temp.png')
    plt.close()

def serialize_fig() -> str:
    with open("./temp/temp.png", "rb") as image_file:
        encoding = base64.b64encode(image_file.read())
    return str(encoding)

