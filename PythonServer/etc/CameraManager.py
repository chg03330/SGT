import cv2

class Img:
    cameraNo = 0
    img = None

class CameraManager:
    cameraList = []

    def __init__(self, cameraList):
        for camera in cameraList:
            print(camera)
            capture = cv2.VideoCapture(camera)
            capture.set(cv2.CAP_PROP_BUFFERSIZE, 1000)
            print(capture)
            self.cameraList.append(capture)

    def readAll(self):
        cameraFrames = []
        for camera in self.cameraList:
            ret, frame = camera.read()
            ret, frame = cv2.imencode(".jpg", frame)
            img = Img(camera, frame)
            cameraFrames.append(img)
        return cameraFrames
    
    def read(self, cameraNo):
        ret, frame = self.cameraList[cameraNo].read()
        ret, frame = cv2.imencode(".jpg", frame)
        return frame

    def cutImg(self, img, rect):
        return None
            

