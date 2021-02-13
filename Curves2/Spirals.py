from math import *
import sys

sys.path.insert(0,'/usr/local/Python')

from Vector import *
from Curve2 import *

from Vector import *
from Curve2 import *
from Args import *

class Spiral(Curve2):

    rc="Spiral_Calc"
         
    ##!
    ##! Logarithmic Spiral: Rolling one circle (r=b) outside another, ratio a. Poop size: c.
    ##!

    def Spiral_Calc(self,t):        
        return Vector([ cos(pi*t),sin(pi*t) ])*self.a*exp(self.b*t*pi)

    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min00(self):
        return Vector([-3,-3])
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max00(self):
        return Vector([3,3])
   
 

mu=0.1
parms={
    #"rc": "Spiral_Calc",
    #"Name": "Spiral",
    #"Type": "Spiral",
    #"t1": 0,
    #"t2": 4*pi,
}
Args_Files_Add(["Curves/Spirals.inf"])

curve=Spiral(parms)
curve.Draw_Animated()
