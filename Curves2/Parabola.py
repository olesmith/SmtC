from math import *
import sys

sys.path.insert(0,'/usr/local/Python')

from Vector import *
from Curve2 import *
from Rolling import *
from Args import *



class Parabola(Curve2):

    S_rc="Curve_Length_Calc"
    
    ##!
    ##! Calculate and store accumulated curvelengths
    ##!
    
    def Curve_Length_Calc(self,t):
        t2=sqrt(1+t*t)
        return 0.5*( t*t2+log( t+t2) )
    
    ##!
    ##! Calculate and store accumulated curvelengths
    ##!
    
    def Curve_Lengths_Calc(self,ts=[]):
        if (len(ts)==0): ts=self.ts
            
        self.S=Vector( len(ts) )
        s0=self.Curve_Length_Calc(ts[0])
        
        for i in range( len(ts) ):
            self.S[i]=self.Curve_Length_Calc(ts[i]) -s0
            #print i,self.S[i]
            
        s=self.S[ len(self.ts)-1 ]
        return s
         
    ##!
    ##! Epitrochoid: Rolling one circle (r=b) outside another, ratio a. Poop size: c.
    ##!

    def Parabola_Calc(self,t):        
        return [ t,self.a*t*t ] #+self.b*t+self.c ]

    ##!
    ##! Get n skew necessary for rolling circles to become right.
    ##!

    def Curve_Rolling_Skew(self):
        return 0
    
    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        return Vector([self.t1-2.0,-1.0])
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        y1=self.Parabola_Calc(self.t1)
        y2=self.Parabola_Calc(self.t2)
        
        return Vector([self.t2+2.0,Max(y1[1],y2[1])])
   
    ##!
    ##! Run animation
    ##!

    def Run(self):
        self.CLI2Obj()
        self.NPoints=200
        self.a=0.5

        for nn in range(1,5):
            self.b=1.0*nn
        
            S=self.Curve_Length_Calc(self.t2)/(2.0*nn*pi)
            self.Roulette_A=S

            n=21
            c1=1.0
            c2=2.0
            dc=(c2-c1)/(1.0*(n-1))
            c=c1
            for i in range(n):
                self.c=c
                self.Roulette_B=c*self.Roulette_A
            
                print "Calc Roulette",self.Roulette_A,self.Roulette_B
                self.Draw_Animated()
                c+=dc
                exit()
            

mu=0.1
parms={
}
Args_Files_Add(["Curves/Parabola.inf"])

curve=Parabola(parms)
curve.Run()
