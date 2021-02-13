from math import *

from Vector import *
from Curve2 import *


class Hyperbola(Curve2):

    rc="Hyperbola_Calc"
         
    ##!
    ##! Epitrochoid: Rolling one circle (r=b) outside another, ratio a. Poop size: c.
    ##!

    def Hyperbola_Calc(self,t):
        v=[ sqrt(1+t*t),t]
        return v

    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        return Vector([0,-3])
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        return Vector([3,3])
   
 

parms={
    "rc": "Hyperbola_Calc",
    "Name": "Hyperbola",
    "Type": "Hyperbola",
    "t1": -2,
    "t2": 2,
}

curve=Hyperbola(parms)
curve.CalcGeo=True
curve.Evolute=True

curve.Draw_Animated()
