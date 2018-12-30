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

# Neutral horizontal servo postion
pt.pan(0)

# Neutral vertical servo postion
pt.tilt(90)

# This list defines the servo angle value increments
pan_inc = [-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90]

for x in pan_inc:
    pt.pan(x)
    sleep(1.5)
pt.pan(0)

