#!/bin/sh

python Curves/Ellipse.py 100 100

python Curves/Trochoid.py 100 100
python Curves/Trochoid.py 100 100 -b 0.5
python Curves/Trochoid.py 100 100 -b -0.5
python Curves/Trochoid.py 100 100 -b -0.2
python Curves/Trochoid.py 100 100 -b -0.1

