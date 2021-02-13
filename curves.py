#!/usr/bin/python

import os

def System_Exec(commands):
    try:
        os.system(" ".join(commands))
    except:
        print "Warning! Unable to execute system command: "+" ".join(commands)

curves=[
    #"Spirals",
    "Quadratic",
    "Parabola",
    "Parabolas",
    "Lissajous",
    "Ellipse",
    "Descartes",
    "Hypotrochoid",
    "Trochoid",
    "Epitrochoid",
]
for curve in curves:
    print System_Exec([
        "/usr/bin/python",
        "Curves/"+curve+".py",
        #"> Curves/"+curve+".log",
    ])
