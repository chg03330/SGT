
from flask import Flask, render_template, redirect, request, url_for, Response, jsonify
import requests
import json
import itertools
import time
from datetime import datetime
import cv2
import threading
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

app = Flask(__name__)
frame = None

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_BUFFERSIZE, 1000)
    #threading.Timer(1.0, FindFace).start()
    while True:
        ret, frame = capture.read()
        ret, frame = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

def FindFace():
    # set to your own subscription key value
    subscription_key = 'df84384c5ba742d4b2e8bedee6374d99'
    assert subscription_key

    # replace <My Endpoint String> with the string from your endpoint URL
    face_api_url = 'https://2020sgt.cognitiveservices.azure.com/face/v1.0/detect'

    image_url = request.base_url + '/imgage'

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'true',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    response = requests.post(image_url, params=params,
                         headers=headers, json={"url": request.base_url + '/azure_result'})
    

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/azure_result')
def azure_result():
    return None
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True, port='9000')