import sys

sys.path.insert(0,'/usr/local/Python')

from Curve2 import *
from Rolling import *
from Args import *


class Ellipse(Rolling,Curve2):
    ##!
    ##! Calc Ellipse points.
    ##!

    def Ellipsis_Calc(self,t):
        cosine= cos( t+self.phi )
        sine  = sin( t+self.phi )

        c2=2.0/self.c
        if (c2!=1.0):
            cosine = Sign( cosine )*abs(cosine)**c2
            sine   = Sign( sine   )*abs(sine)**c2
        
        return [self.a*cosine,self.b*sine ]
    
 
    ##!
    ##! Calc Ellipse evolute points.
    ##!

    def Ellipsis_Evolute_Calc(self,t):
        sq=self.a**2-self.b**2
        a=sq/self.a
        b=-sq/self.b
        

        return [ a*(cos( t+self.phi )**3), b*(sin( t+self.phi )**3) ]


                                  
    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        f=1.0*(abs(self.a)+abs(self.b))
        return Vector([-f,-f])
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        f=1.0*(abs(self.a)+abs(self.b))
        return Vector([f,f])


    ##!
    ##! Run animation
    ##!

    def Run(self):
        self.CLI2Obj()

        ass=[
            1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0
        ]
        bss=[ 1.0 ]
        css=[ 2.0 ]
        
        parms={
            "a": ass,
            "b": bss,
            "c": css,
            "n": [ 400 ],
            "Types": [ "Curve", ],
        }

        timer=Timer("Generating Animations: ")

        self.Animations_Run(parms)

        ass=[
            1.0,
            2.0,
        ]
        bss=[ 1.0 ]
        css=[
            0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,
            1.0,
            1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,
            2.0,
            2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,
            3.0,4.0,5.0
        ]
        
        parms={
            "a": ass,
            "b": bss,
            "c": css,
            "n": [ 400 ],
            "Types": [ "Curve", ],
        }

        timer=Timer("Generating Animations: ")

        self.Animations_Run(parms)

        
 
Args_Files_Add(["Curves/Ellipse.inf"])

parms={
    "Resolution": [800,800],
    "Parameter_Names": ["a","b","n" ],
}

curve=Ellipse(parms)
curve.Run()
