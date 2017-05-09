#For setting up flask server to recive data from app.
from flask import Flask, jsonify, request
from bson import json_util
from bson.json_util import dumps
import cv2
import sys
import base64
import warnings
warnings.filterwarnings("ignore")
from main import motion

app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
def index():
    # import subprocess
    sys.stderr.write('Server Started\n')
    # img = cv2.imread('abc.jpg')
    # pre = motion(img)
    # sys.stderr.write(str(pre)+'\n')
    if request.method == 'POST':
        sys.stderr.write(str(request.get_json()))
        jsonResponse = (request.get_json())
        imgstring = jsonResponse['image']
        sys.stderr.write(str(imgstring))
        imgdata = base64.b64decode(imgstring)
        filename = 'image.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        # img = cv2.imread('image.jpg')
        # pre = motion(img)
        # sys.stderr.write(str(pre)+'\n')
    else:
        sys.stderr.write("Data not recived.")

@app.route('/main')
def main():
    return "Server made by Bharat Kumar and Vaibhav Sharma"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
