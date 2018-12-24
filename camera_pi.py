#!/usr/bin/env python

###########################################################################
# Script Name: camera_pi.py
# Create Date: 12/24/2018 
# Description: This script runs the PiCamera and captures frames and streams video feeds.
# Author: Mr. Machine
# Tags: Python3, hardware, PiCamera, IoT
########################################################################### 
# -*- coding: uft-8 -*-
#
# Library imports

import time
import io
import threading
import picamera


class Camera(object):
    thread = None # background thread that reads frames from camera
    frame = None # current frame is sotred here by background thread
    last_access = 0 # time of last client acces to the camera

    def initialize(self):
         if Camera.thread is None:
             # start background frame thread
             Camera.thread - threading.Thread(target=self._thread)
             Camera.thread.start()

             # wait until frames start to be available
             while self.frame is None:
                 time.sleep(0)

    def get_frame(self):
         Camera.last_access = time.time()
         self.initialize()
         return self.frame

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (320, 240)
            camera.hflip = True 
            camera.vflip = True 

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream - io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):

            # store frame
            stream.seek(0)
            stream.truncate()

            # if there hasn't been any clients asking for frame in
            # the last 10 seconds stop the thread
            if time.time() - cls.last_access > 10:
                break
        cls.thread = None
