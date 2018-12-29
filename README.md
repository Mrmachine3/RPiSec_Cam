# Raspberry Pi Surveillance Camera

### Description
This github repository contains project files related to building, programming, and deploying a Raspberyy Pi (RPi) for use as a security camera. Additionally, this unit has Adafruit's [Pan Tilt HAT][1] module that controls the angle of the [PiCamera][2]. The Raspberry Pi will host a Flask webserver that will serve a webpage that displays a live video feed and also a pan-tilt controller that will relay commands back to the Raspberry Pi to control the Pan Tilt servo mechanism. 

### Objectives:
+ Deploy a RPi with the Pan Tilt HAT
+ Record live video feeds
+ Capture pictures at a set interval throughout a 24 hour period
+ Schedule job to archive images
+ Locally control Pan Tilt module 
+ Locally serve a webpage streaming live video feeds

---
### RPi & PanTilt HAT Setup
#### Assembling the Pan-Tilt HAT
For complete details on assembling the Pan-Tilt HAT module refer to the follwing tutorial: ***[Assembling Pan-Tilt HAT][3]*** 

<p align="center"><a href="https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat"><img alt="Pan-tilt HAT" src="https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-1.jpg" height="50%" width="50%"></a>
<p align="center"><strong>Pimoroni Pan-Tilt HAT</strong></p>

The Pan-Tilt HAT module has four holes to mount the unit to the raspberry pi. In addition to the four screw holes, the HAT module has a slot to route the servo cables and camera cable through the PCB for unobstructed movements. Finally, the bottom of the module has the 40 GPIO pin connectors to place directly onto the Raspberry Pi GPIO pins.

It's best to orient the module so that the head can rotate around the left edge of the PCB, as it is in the picture below.

<p align="center"><a href="https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat"><img alt="HAT Orientation" src="https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-3.jpg" height="50%" width="50%"></a>
<p align="center"><strong>HAT module orientation</strong></p>

#### Connecting the servos
Pass the two servo cables through the slot on the PCB labeled *Servo Cables*. Now flip the module to view the underside and connect the two sets of wires up with the brown wires connected to the ground pins, as depicted in the picture below.

<p align="center"><a href="https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat"><img alt="Underside of HAT module" src="https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-4.jpg" height="50%" width="50%"></a>
<p align="center"><strong>Underside of HAT module</strong></p>

Connect the pan servo, which moves horizontally, to servo channel 1, and the tilt servo, which that moves vertically, to servo channel 2. These can easily be swapped in software later.

#### Attaching the camera
The camera module can be mounted to the pan-tilt hinge mechanism by screwing the camera to the acrylic mounting plates that were included with the Pan-Tilt HAT full kit.

The piece with the t-shaped hole goes directly on top of the front face of the camera module with the camera cable protruding from the top edge of the mount (the one with the more rounded corners).

<p align="center"><a href="https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat"><img alt="Camera mounting plates" src="https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-6.jpg" height="50%" width="50%"></a></p>
<p align="center"><strong>Camera mounting plate</strong></p>

Place the other plastic piece on top, and then use two of the white nylon bolts and nuts to secure everything. Your camera and mount should now clip into the head of the pan-tilt module. Make sure that the cable protrudes from the top (the curves on the mount should match the curves on the head of the pan-tilt module). Finally, route the camera cable through the slot on the PCB marked *Cam Cable*, and then connect it to the camera connector on your Raspberry Pi.

I opted to exclude the optional Neopixel stick; however, if you want to use the Neopixel stick, then read the tutorial section labeled ***[Soldering and mounting a Neopixel Stick][4]***.

An option may be to add a ***[Night Vision Camera Module for Raspberry Pi][5]***.

<p align="center"><a href="https://cdn-shop.adafruit.com/970x728/3353-04.jpg"><img alt="Complete Pan-tilt Camera" src="https://cdn-shop.adafruit.com/970x728/3353-04.jpg" height="50%" width="50%"></a></p>
<p align="center"><strong>Complete Pan-tilt Camera</strong></p>

### ***MORE UPDATES COMING SOON***

<!--
### Software Installation

#### Install Pre-Requisites
Run the following commands on your Raspberry Pi's terminal:

```bash
sudo apt-get install python3-pantilthat
```
```bash
sudo apt-get install python-smbus python-opencv opencv-data
```



```bash
sudo raspi-config nonint do_camera 0
```




### Unit Testing

### Webpage build
-->

---
### Pipe Dreams:
+ Weather-proof RPi and Pan Tilt HAT enclosure
+ Record video based on motion detection 
+ Schedule job to archive images in local NAS
+ Automate post-capture image analysis to flag exceptions
+ Enable direct messaging of image exceptions
+ Remotely access webpage to view live video/image archives
+ Develop ansible playbook to automate setup of IoT device

## Documentation & Support
* ***[Pimoroni Pan-tilt HAT Github][6]***
* ***[Pimoroni Pan-tilt HAT documentation][7]***
* ***[Pimoroni Function Reference][10]***
* ***[Raspberry Pi GPIO Pin Layout][11]***
* ***[Pimoroni Forum Support][12]***
* ***[Guides and tutorials][9]***
* ***[Pimoroni Pan-tilt Face Tracker][8]***

---
[1]: https://www.adafruit.com/product/3353
[2]: https://www.adafruit.com/product/3099i
[3]: https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat
[4]: https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat
[5]: https://shop.pimoroni.com/products/night-vision-camera-module-for-raspberry-pi?variant=12516582752339
[6]: https://github.com/pimoroni/pantilt-hat
[7]: http://docs.pimoroni.com/pantilthat/#
[8]: https://learn.pimoroni.com/tutorial/electromechanical/building-a-pan-tilt-face-tracker
[9]: https://learn.pimoroni.com/pan-tilt-hat
[10]: http://docs.pimoroni.com/pantilthat/
[11]: https://pinout.xyz/pinout/pan_tilt_hat
[12]: http://forums.pimoroni.com/c/support
