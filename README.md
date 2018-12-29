# Raspberry Pi 3 B+ Surveillance Camera

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

<figure class="center">
<a href="https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat"><img alt="Pan-tilt HAT" src="https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-1.jpg"></a>
<figcaption><a href="https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-1.jpg"><strong>Pimoroni Pan-Tilt HAT</strong></a></figcaption>
</figure>¬

[Pan Tilt HAT](/img/pantilt-HAT.jpg)

### Software Installation

### Unit Testing

### Webpage build

---
### Pipe Dreams:
+ Weather-proof RPi and Pan Tilt HAT enclosure
+ Record video based on motion detection 
+ Schedule job to archive images in local NAS
+ Automate post-capture image analysis to flag exceptions
+ Enable direct messaging of image exceptions
+ Remotely access webpage to view live video/image archives
+ Develop ansible playbook to automate setup of IoT device

---
[1]: https://www.adafruit.com/product/3353
[2]: https://www.adafruit.com/product/3099i
[3]: https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat
