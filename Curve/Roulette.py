from math import *

from Vector import *



class Curve_Roulette():
    
    ##!
    ##! Get rolling angular velocity as function of t
    ##!

    def Curve_Roulette_Angle(self,t):
        n=self.T2n(t)
        s=self.S[n]
        
        return -s/(self.Roulette_A)
    
    ##!
    ##! Calculates curve unit normal vector.
    ##!

    def Curve_Normal(self,t):
        return self.dr(t).Normalize().Transverse2()
    
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
        R=self.r(t)

        return R+self.Curve_Normal(t)*self.Roulette_A
    
    ##!
    ##! Get coordinates of rolling point as function of t.
    ##!

    def Curve_Roulette_Calc(self,t):
        center=self.Parent.Curve_Rolling_Center(t)
       
        e=self.Parent.Curve_Roulette_e(t)
        return center+e    

    
    def Curve_Roulette_e(self,t):
        normal=self.Curve_Normal(t)
        normal*=-self.Roulette_B
        e=self.Curve_Roulette_Rotated(t,normal)
        #e*=-1.0

        return e
        
    ##!
    ##! Get coordinates of rolling center in point n
    ##!

    def Curve_Roulette_Circles_Draw(self,n):

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
            -angle,
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
