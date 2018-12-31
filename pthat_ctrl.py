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
from time import sleep, time 
from datetime import datetime

#Define sleep time
s =.5     #short sleep interval
ls =1.5   #long sleep interval

# Define script start time
start_time = datetime.utcnow()
now = start_time.strftime("%H:%M:%S")

# Neutral horizontal and vertical servo postions
pt.pan(0)
pt.tilt(90)

pan_in = abs(int(input("Enter desired angle between -90 and 90 on the horizontal axis: ")))

# This list defines the servo angle value increments
pan_presets = [-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90]

# Move servo to both viewpoints of input parameters
pt.pan(pan_in * -1)
sleep(ls)
pt.pan(pan_in)
sleep(ls)
    
# Begin at farthest viewpoint position on right side and loop through servo angle parameters 
for x in pan_presets:
    pt.pan(x)
    sleep(s)
for x in pan_presets[::-1]:
    pt.pan(x)
    sleep(s)

# Move servo to both viewpoints of input parameters
pt.pan(pan_in * -1)
sleep(ls)
pt.pan(pan_in)
sleep(ls)

# Define script end time
end_time = datetime.utcnow()
duration = (end_time-start_time).total_seconds()
#time = duration.strftime("%H:%M:%S")
print("Script ran in " + str(round(duration,2)) + " seconds")
