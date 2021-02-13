from math import *
import sys

sys.path.insert(0,'/usr/local/Python')

from Vector import *
from Curve2 import *
from Rolling import *
from Args import *


class Descartes(Curve2):
         
    ##!
    ##! Folium of Descartes, parametrization
    ##!

    def Descartes_Calc(self,theta):
        cosine=cos(theta)
        sine=sin(theta)
        r=3.0*self.a*sine*cosine/(sine**3.0+cosine**3.0)
        
        return [ r*cosine,r*sine ]

    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        return Vector([-self.a,-self.a])*2.0
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        return Vector([self.a,self.a])*4.0
   
    ##!
    ##! Run animation
    ##!

    def Run(self):
        mu=0.1
        self.CLI2Obj()
        self.t1=-pi/4+mu
        self.t2=3*pi/4-mu
        
        self.Draw_Animated()
 


parms={
    "Parameter_Names": ["a","b","&gamma;" ],
}
Args_Files_Add(["Curves/Descartes.inf"])


curve=Descartes(parms)

curve.Run()
