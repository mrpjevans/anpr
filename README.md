# Automatic Number Plate Recognition
ANPR Tutorial Code for MagPi #78 [https://raspberrypi.org/magpi]()

## Requirements

* Raspberry Pi
* Pi Camera Module
* Raspian Stretch Lite


## Installation

```
cd
sudo apt update && sudo apt -y upgrade
sudo apt install git python-pip openalpr openalpr-daemon openalpr-utils libopenalpr-dev
git clone http://github.com/mrpjevans/anpr.git
```

## Configuration

Edit anpt/anpr.py and set `PUSHOVER_USER_KEY` and `PUSHOVER_APP_TOKEN` to the values for your Pushover account. See MagPi for full details.

## Usage

```
python ~/anpr/anpr.py
```

## Run at Boot

```
sudo nano /etc/rc.local
```

Before the final line `exit 0` add the following:

```
#Start ANPR Monitoring
/usr/bin/python /home/pi/anpr.py
```
Reboot

