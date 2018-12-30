#!/usr/bin/env python

###########################################################################
# Script Name: pthat_cntrl.py
# Create Date: 12/29/2018
# Description: The purpose of this script is to remotely control the pan-tilt
# servo angle of PiCamera. 
# Author: Mr. Machine
# Tags: hardware, IoT, servos,  
########################################################################### 

# Library imports
import pantilthat as pt
from time import sleep

# Neutral horizontal and vertical servo postions
pt.pan(0)
pt.tilt(90)

pan_input = int(input("Enter desired angle between -90 and 90 on the horizontal axis: "))

# This list defines the servo angle value increments
pan_presets = [-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90]

while pt.server_enable(1,True):
    if pan_input in pan_presets:
        for x in pan_presets:
            pt.pan(x)
            sleep(1.5)
        pt.pan(0)
        pt.idle_timeout(15)
    
