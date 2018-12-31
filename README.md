## Raspberry Pi Surveillance Camera

### Description
This github repository contains project files related to building, programming, and deploying a Raspberyy Pi (RPi) for use as a security camera. For additional details on hardware, software, and installation instructions, please view my github ***[project wiki][1]***.

#### Hardware Requirements
+ *[Raspberry Pi 3 B+][2]*
+ *[5V 2.5A Switching Power Suppy w/ MicroUSB Cable][3]*
+ *[Raspberry Pi NoIR Camera Board][4]*
+ *[Flex Cable for RPi Camera - 300mm/12"][5]*
+ *[Pimoroni Pan-Tilt HAT for Raspberry Pi][6]*  
  + ***NOTE:*** *The servo and frame kit are sold separately*
+ *[Mini Pan-Tilt Kit w/ Micro Servos][7]*

Since the *[Raspberry Pi 3 B+][2]* has a GPU that supports wireless local area networks (LANs), you have the option of enabling a Raspberry Pi to connect to your home WiFi signal. Optionally, you could connect an ethernet cable to the Raspberry Pi and connect to the extra LAN port on your home WiFi router. 

#### Software Package Requirements
When you first log into your Raspberry Pi, you should proceed with changing the default password to a password of your choosing. If you're comfortable with the command line, open up a terminal and enter ```cd``` to navigate to your Raspberry Pi's home directory. Once you're in the home directory you can enter ```pwd``` to verify you are located at ```/home/pi```. From this point on you can begin the set up process by first entering the following command to clone my github repository to your home directory.

```sh
git clone https://github.com/Mrmachine3/RPiSec_Cam.git
```

Once the repository has been successfully cloned to your home folder type the following command to move into the folder and list the contents of the directory.
```sh
cd RPiSec_cam; ls -al
```
Next, you will enter the following command to launch a bash shell script that will proceed to update your Rasberry Pi and install the required software packages.
```sh
chmod +x setup.sh
./setup.sh
```


---
[1]: https://github.com/Mrmachine3/RPiSec_Cam/wiki
[2]: https://tinyurl.com/yam29y4h
[3]: https://tinyurl.com/zfwq352
[4]: https://tinyurl.com/l8cuz6w
[5]: https://tinyurl.com/ycagt8h5
[6]: https://tinyurl.com/y9ny5knm
[7]: https://tinyurl.com/yd22q5s3
