# Raspberry Pi Surveillance Camera

### Description
This github repository contains project files related to building, programming, and deploying a Raspberyy Pi (RPi) for use as a security camera. Additionally, this unit has Adafruit's [Pan Tilt HAT][1] module that controls the angle of the [PiCamera][2]. The Raspberry Pi will host a Flask webserver that will serve a webpage that displays a live video feed and also a pan-tilt controller that will relay commands back to the Raspberry Pi to control the Pan Tilt servo mechanism. 

### Objectives:
+ Deploy a Raspberry Pi with a Pan Tilt HAT
  + Program script to control pan-tilt hardware 
  + Add scheduled job to run servo control script 
  + Enable logging of servo status and/or script errors, including current positions
  + Enable automated messaging of raspberry pi pan-tilt hardware status
+ Capture pictures/video at set intervals throughout a 24 hour period
  + Program script to control pi camera hardware
  + Add scheduled job to run camera script in image capture mode 
  + Add scheduled job to run camera script in video capture mode
  + Enable logging of camera status, and/or script errors, including current capture setting 
  + Add scheduled job to archive images and video
  + Add scheduled job to delete archived images and video
  + Enable automated messaging of raspberry pi storage status
+ Deploy a webservice to locally stream video feeds to a webpage
  + Program script to serve webpages
  + Program script to control pan-tilt hardware via a web interface
  + Add scheduled job to run web application script
  + Enable logging of web app service status, and/or script errors,
  + Enable automated messaging of web app service status
+ Program setup shell script: 
  + To enable cron job logging
  + To add microservice admin user
  + To add networking rules
---

#### Install Pre-Requisites
Run the following commands on your Raspberry Pi's terminal:

```bash
sudo apt-get install python3-pantilthat
```
```bash
sudo apt-get install python-smbus opencv-python opencv-data
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
