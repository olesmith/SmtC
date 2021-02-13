#!/usr/bin/python

import os,sys

comps=sys.argv[0]
comps=comps.split("/")

command=comps[ len(comps)-1 ]

if (len(sys.argv)==1 ):
   comps=[
      "Usage:",
      command,
      "pin_id",
   ]
   print " ".join( comps )
   exit()

pin=int(sys.argv[1])

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT) 
if (command=="up"):
   GPIO.output(pin, GPIO.HIGH)
      
   outfile="/var/lib/gpio/"+str(pin)
   os.system( "echo "+str(GPIO.HIGH)+" > "+outfile )

elif (command=="down"):
   GPIO.output(pin, GPIO.LOW)
      
   outfile="/var/lib/gpio/"+str(pin)
   os.system( "echo "+str(GPIO.LOW)+" > "+outfile )


#Uncommented, as it seems to reset changes done in this script.
#GPIO.cleanup()

