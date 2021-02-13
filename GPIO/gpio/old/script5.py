#!/usr/bin/python

import sys


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init list with pin numbers

pinList = [6, 13, 19, 26, 12, 16, 20, 21, ]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    print "Setup",i
    GPIO.setup(i, GPIO.OUT) 
    #GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

exit()
SleepTimeS = 0.2
SleepTimeL = 0.5

# main loop

#try:
for i in pinList:
    GPIO.output(i, GPIO.LOW)
    time.sleep(SleepTimeS);
    print i,GPIO.input(i)

    GPIO.output(i, GPIO.HIGH)
    time.sleep(SleepTimeS);
    print i,GPIO.input(i)



# End program cleanly with keyboard
#except KeyboardInterrupt:
#  print "  Quit"

# Reset GPIO settings
GPIO.cleanup()

# find more information on this script at
# http://youtu.be/oaf_zQcrg7g
