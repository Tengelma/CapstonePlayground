from flask import Flask, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import base64
app = Flask(__name__)

@app.route('/graph', methods=['POST'])
def graph():
    content = request.json
    slope = content["slope"]
    y_intercept = content["yIntercept"]
    x = getX(100)
    y = getY(x, slope, y_intercept)
    createFig(x, y)
    img = {"image": serializeFig()}
    return jsonify(img)

def getX(range: int):
    return np.arange(100)

def getY(x, slope: int, y_intercept: int):
    calculate = lambda x: x * slope + y_intercept
    return calculate(x)

def createFig(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([0, 100, 0, 100])
    plt.savefig('./temp/temp.png')

def serializeFig() -> str:
    with open("./temp/temp.png", "rb") as image_file:
        encoding = base64.b64encode(image_file.read())
    return str(encoding)
    
