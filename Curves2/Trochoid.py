from math import *
import sys

sys.path.insert(0,'/usr/local/Python')

from Vector import *
from Curve2 import *
from Rolling import *
from Args import *


class Trochoid(Rolling,Curve2):

    a=1.0
    b=0.0
    nlaps=2
    phi=0.0

        


    ##!
    ##! Cycloid: Rolling start point
    ##!
    
    def Trochoid_R0(self,t):
        return Vector([
            self.r0[0]+self.a*t,
            self.r0[1]+self.a
        ])
    

   
    ##!
    ##! Trochoid: Rolling a circle (r=a) on a line. Poop size: b.
    ##!

    def Trochoid_Calc(self,t):
        tt=(t-self.phi)
        r0=self.Trochoid_R0(t)
                
        return [
            r0[0]-(self.a+self.b)*sin(tt),
            r0[1]-(self.a+self.b)*cos(tt)
        ]

    ##!
    ##! The trochoid evolute
    ##!

    def Trochoid_Evolute_Calc(self,t):

        a=self.a
        b=self.b+a

        r0=self.Trochoid_R0(t)
        tt=t-self.phi
        cos1=a-b*cos(tt)
        cos2=b-a*cos(tt)

        fact=0.0
        if (abs(cos2)>0.0):
            fact=-a/b*cos1/cos2
                                                   
        return [
            a*t-fact*b*sin(tt),
            a*fact-fact*b*cos(tt)
        ]

    

    r0=[0.0,0.0]
         
    ##!
    ##! Get rolled angle
    ##!

    def Curve_Rolling_Angle(self,n):
        
        return -self.ts[n]*self.a #+self.phi
    
    ##!
    ##! Get rolled angle
    ##!

    def Curve_Rolling_Normal(self,n):
        return Vector([0.0,-1.0])
    
       
    ##!
    ##! Get coordinates of rolling center no n
    ##!

    def Curve_Rolling_Center(self,n):
        return self.Trochoid_R0(self.ts[n])
    
    ##!
    ##! Get n skew necessary for rolling circles to become right.
    ##!

    def Curve_Rolling_Skew(self):
        return 1
    
       

    ##!
    ##! Draw Trochoid extra curves
    ##!

    def Curve_Draw(self,n,nframe):
        Curve2.Curve_Draw(self,n,nframe)
        self.Curve_Rolling_Circle_Draw(n)
        self.Canvas().Draw_Segment([0.0,0.0],[self.t2,0.0],"Fixed","black")
        

    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        p=self.R.Min()       
        pmax=self.R.Max()       

        p[1]=-pmax[1]
        
        return p
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        p=self.R.Max()       

        return p
        
    ##!
    ##! Run animation
    ##!

    def Run(self):
        self.CLI2Obj()

        parms={
            "a": [ 1.0 ],
            "b": [
                -1.0,
                -0.75,-0.5,-0.25,-0.2,-0.15,-0.1,-0.05,
                0.0,
                0.25,
                0.5,
                0.75,1.0,1.25,1.5
            ],
            "c": [ 0.0 ],
            "n": [ 400 ],
            "Types": [ "Curve", ],
        }
        
        timer=Timer("Generating Animations: ")

        self.Animations_Run(parms)
        #exit()
        
        canvas=Canvas2(
            {},
            [ self.Curve_Min(),self.Curve_Max() ],
            self.Resolution
        )

        name="Trochoid"
        path="curves/"+name+"/"
        self.SVGs_Parms_Overlays(
            "curves/"+name,
            name,
            canvas,
            parms,
            [
                "curves/Trochoid/Curve-1.0-0.0-0.0-400.svg",
            ]
        )

        parms[ "Types" ].append("Numerical_Evolute")
        path="curves/"+name+"/"
        self.SVGs_Parms_Overlays(
            "curves/"+name,
            name+"-Evolute",
            canvas,
            parms,
            [
                "curves/Trochoid/Curve-1.0-0.0-0.0-400.svg",
                "curves/Trochoid/Numerical_Evolute-1.0-0.0-0.0-400.svg",
            ]
        )
       
 
parms={
    "Resolution": [1200,400],
}

Args_Files_Add(["Curves/Trochoid.inf"])


curve=Trochoid(parms)
curve.Run()

