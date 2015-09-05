# WhArduino
A python script that helps tracking how many and what kind of Arduino Boards are connected to a pc via USB, and at what COM port each one of them is connected.
# Dependencies
+ [Python](https://www.python.org)
+ [PySerial](http://pyserial.sourceforge.net)

# Usage
```BASH
python WhArduino.py
```
# Supported Arduino devices
+ Arduino Uno 
+ Arduino Uno R3
+ Arduino Mega 2560
+ Arduino Mega 2560 R3
+ Arduino Mega ADK
+ Arduino Mega ADK R3

Other devices having the Arduino VID (0x2341) are shown just as Arduino without specifying their type.  
Old Arduino boards that use FTDI's VID (0x0403) are shown as FTDI without specifying what product are they.  
Arduino boards from other vendors are not supported yet.

# What's missing
+ A list of the different Arduino boards and their respective PID
+ A list of the different Arduino boards from other vendors and their respective VID/PID