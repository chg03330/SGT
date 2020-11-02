import threading

class ImgSendThread(threading.Thread):
    def __init__(self, ):
        threading.Thread.__init__(self)
        

    def run(self):
        self.server.serve_forever()