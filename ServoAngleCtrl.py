#!/usr/bin/env python

###########################################################################
# Script Name: pantiltcntrl.py
# Create Date: 12/24/2018
# Description: The purpose of this script is to remotely control the pan-tilt
# servo angle of PiCamera. 
# Author: Mr. Machine
# Tags: hardware, IoT, servos,  
########################################################################### 

# Library imports
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setServoAngle(servo, angle):
    assert angle >=30 and angle <= 150
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.3)
    pwm.stop()

if __name__ == '__main__':
    import sys
    servo = int(sys.argv[1])
    GPIO.setup(servo, GPIO.OUT)
    setServoAngle(servo, int(sys.argv[2]))
    GPIO.cleanup()
