#!/usr/bin/env python
from flask import Flask, render_template, Response
from camera import VideoCamera
from time import sleep
from flask import Flask, request
from flask_cors import CORS

#import sys
#sys.path.insert(0, '/var/www/yourapplication/')
#from yourapplication import app as application

class datos:
    def __init__(self):
        self.caida = False
        self.latitud = 0
        self.longitud = 0
        self.latidos = 0

app = Flask(__name__)
CORS(app)
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', fall=datos.caida, lat=datos.latitud, lon=datos.longitud,lpm=datos.latidos)

@app.route('/locations')
def locations():
    return {"locations":[{"latitude": datos.latitud, "longitude": datos.longitud}]}

@app.route('/sensores')
def sensores():
    return render_template('sensores.html', fall=datos.caida, lat=datos.latitud, lon=datos.longitud,lpm=datos.latidos)

@app.route('/telemetria', methods=['POST'])
def DetectaRostros():
    data = request.get_json()
    datos.caida = data['Caida']
    if data['Latitud'] != 0:
        datos.latitud = data['Latitud']
    if data['Longitud'] != 0:
        datos.longitud = data['Longitud']
    if data['Latidos'] != 0:
        datos.latidos = data['Latidos']

    print("Lat: {}, Long: {}, Caida: {}, Latidos: {} ".format(datos.latitud, datos.longitud, datos.caida, datos.latidos))

    return {"error": False, "message": "ok"}

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        sleep(0.02)


@app.route('/video_feed')
def video_feed():
    try:
        # return Response(gen(VideoCamera('http://localhost:8080')),
        return Response(gen(VideoCamera(0)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    except:
        pass

@app.route('/video_feed2')
def video_feed2():
    try:
        return Response(gen(VideoCamera(2)),
        # return Response(gen(VideoCamera('http://localhost:8080')),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    except:
        pass
@app.route('/video_feed3')
def video_feed3():
    try:
        # return Response(gen(VideoCamera('http://10.88.145.248:8090/stream/video.mjpeg')), # Stream TotalPlay
        return Response(gen(VideoCamera('http://0.0.0.0:8090/stream/video.mjpeg')), # Stream directo espejo
        # return Response(gen(VideoCamera('http://192.168.233.173:9003/video_feed')), # Stream espejo con reconocimiento

                    mimetype='multipart/x-mixed-replace; boundary=frame')
    except:
        pass

if __name__ == '__main__':
    datos = datos()
    # app.run(host='192.168.100.20', threaded=True)
    app.run(host='0.0.0.0', threaded=True, port=8000)
