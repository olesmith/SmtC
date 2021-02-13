#!/usr/bin/python

import sys

sys.path.append('//usr/local/Python')


from GPIO import GPIO 

import cgi
import cgitb
cgitb.enable()

gpio=GPIO()
gpio.Run()


