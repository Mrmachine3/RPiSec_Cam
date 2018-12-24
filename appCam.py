#!/usr/bin/env python

###########################################################################
# Script Name: appCam.py
# Create Date: 12/24/2018 
# Description: This script runs to spin up a webserver to render video.
# Author: Mr. Machine
# Tags: Python3, hardware, PiCamera, IoT
########################################################################### 
# -*- coding: uft-8 -*-
#
# Library imports
from flask import Flask, render_template, Response
# Raspberry Pi camera module (requires picamera package, developed by Miguel Grinberg
from camera_pi import Camera
app = Flask(__name__)
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an image tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)




