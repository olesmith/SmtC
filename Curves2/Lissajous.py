from math import *
import sys

sys.path.insert(0,'/usr/local/Python')

from Vector import *
from Curve2 import *

from Vector import *
from Curve2 import *
from Args import *

class Lissajous(Curve2):

    rc="Lissajous_Calc"
         
    ##!
    ##! Epitrochoid: Rolling one circle (r=b) outside another, ratio a. Poop size: c.
    ##!

    def Lissajous_Calc(self,t):        
        return [ cos(self.a*t),sin(self.b*t) ]

    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        return Vector([-3,-3])
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        return Vector([3,3])
   
    ##!
    ##! Set self.t1 and self.t2 for animation. Meant to be overridden!
    ##!
    
    def Animations_Set_Ts(self,a,b,c):
        self.t2=2.0*pi/min(self.a,self.b)
        
        return
    
    ##!
    ##! Run animation
    ##!

    def Run(self):
        self.Parameter_Names=["a","b","&gamma;"]
        self.CLI2Obj()

        n=5
        ass=[ 1.0,2.0 ]
        bss=[ 1.0,2.0 ] #canonical evolutes

        css=[ 0.0 ]
        for a in ass:
            parms={
                "a": [ a ],
                "b": bss,
                "c": css,
                "n": [ 400 ],
                "Types": [ "Curve", ],
            }

            timer=Timer("Generating Animations: ")
            self.Animations_Run(parms)
            

mu=0.1
parms={
    #"rc": "Lissajous_Calc",
    #"Name": "Lissajous",
    #"Type": "Lissajous",
    #"t1": 0,
    #"t2": 4*pi,
    "Parameter_Names": ["a","b","&gamma;" ],
}
Args_Files_Add(["Curves/Lissajous.inf"])

curve=Lissajous(parms)
curve.CalcGeo=True
curve.Evolute=True
curve.Run()
