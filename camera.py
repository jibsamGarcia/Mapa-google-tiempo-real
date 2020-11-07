import cv2

class VideoCamera(object):
    def __init__(self, valor):
        # Using OpenCV to capture from device 0.
        self.video = cv2.VideoCapture(valor)


    def __del__(self):
        self.video.release()

    def get_frame(self):
        try:
            success, image = self.video.read()
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()
        except:
            pass
