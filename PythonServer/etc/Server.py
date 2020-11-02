from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from os import curdir, sep
import requests
import json
import time
import cv2
import mysql.connector
import datetime
import threading

mysql_con = None

class MainHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        f = open("./html/index.html", "r", encoding="UTF8")
        ###self.direcotry = "/html/"
        #parsed_path=urlparse(self.path)
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/html')
        self.end_headers() 
        self.wfile.write(f.read().encode("utf-8"))
        return None

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server = HTTPServer(('', 8080), MainHandler)

    def run(self):
        self.server.serve_forever()

if __name__ =='__main__':
    httpServer = ServerThread()
    httpServer.start()
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_BUFFERSIZE, 1000)

    frame = None

    print(capture)

    while True:

#        ret, frame = capture.read()

#        now = datetime.datetime.now().strftime("%d_%H-%M-%S")

#        out = cv2.imwrite(str(now) + ".jpg",frame)
        a = 10

    capture.release()

    
"""

mysql_con = mysql.connector.connect(host='localhost', port='3306', database='face_db', user='admin', password='1234')
                                            
    mysql_cursor = mysql_con.cursor()

    mysql_cursor.execute("show tables")
    
    for row in mysql_cursor:
        print(row)

    mysql_cursor.close()

  

# set to your own subscription key value
subscription_key = None
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://<My Endpoint String>.com/face/v1.0/detect'

image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
print(json.dumps(response.json()))
"""


