from math import *

from Vector import *
from Curve import Curve



class Roulette(Curve):
    
    ##!
    ##! Get rolling angular velocity as function of t
    ##!

    def Curve_Roulette_Angle(self,t):
        s=0.0
        if (self.Parent.S_rc):
            method=getattr(self.Parent,self.Parent.S_rc)
            s=method(t)-method( self.ts[0] )
        else:
            n=self.T2n(t)
            s=self.Parent.S[n]-self.Parent.S[0]
        #print "S",t,s
        return -s/(self.Roulette_A)
    
    ##!
    ##! Calculates curve unit normal vector.
    ##!

    def Curve_Normal(self,t):
        dR=self.Parent.dr(t)
        N=dR.Normalize().Transverse2()

        return N
    
    ##!
    ##! Calculates rotated vector: The normal, 
    ##!

    def Curve_Roulette_Rotated(self,t,normal):
        if (not normal):
            normal=self.Curve_Normal(t)
            
        angle=self.Curve_Roulette_Angle(t)

        return normal.Rotate2(angle)
    
    ##!
    ##! Get coordinates of rolling point as function of t.
    ##!

    def Curve_Rolling_Center(self,t):
        n=self.Parent.T2n(t)
        R=self.Parent.r(t)
        dR=self.Parent.dr(t)
        N=dR.Normalize().Transverse2()
        
        return R+N*self.Roulette_A
    
    ##!
    ##! Get coordinates of rolling point as function of t.
    ##!

    def Curve_Roulette_Calc(self,t):
        
        return self.Curve_Rolling_Center(t)+self.Curve_Roulette_e(t)

    
    def Curve_Roulette_e(self,t):
        normal=self.Curve_Normal(t)
        normal*=self.Roulette_B
        e=self.Curve_Roulette_Rotated(t,normal)
        e*=-1.0

        return e
        
    ##!
    ##! Get coordinates of rolling center in point n
    ##!

    def Curve_Roulette_Circles_Draw(self,n):
        n+=self.Parent.Curve_Rolling_Skew()
        ra=self.Roulette_A

        t=self.ts[n]
        center=self.Curve_Rolling_Center(t)
        normal=self.Curve_Normal(t)
        e=self.Curve_Roulette_e(t)
        normal*=-self.Roulette_A

        color1="magenta"
        color2="yellow"

        angle=-self.Curve_Roulette_Angle(t)
        while (angle<-2.0*pi):
            angle+=2.0*pi
        
        while (angle>2.0*pi):
            angle-=2.0*pi
            
        self.Canvas().Draw_Circle_Spans(
            center,
            normal,
            e.Angle2()-normal.Angle2(),
            "Roulette_Arc_Rolled",
            "Roulette_Arc_Unrolled",
            color1,
            color2
        )
         
        self.Canvas().Draw_CS(
            center,
            normal,normal.Transverse2(),
            "Rolling_CS",
            color1
        )
        self.Canvas().Draw_CS(
            center,
            e,e,
            "Roulette_CS",
            color1
        )
