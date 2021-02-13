from math import *
import sys

sys.path.insert(0,'/usr/local/Python')


from Vector import *
from Curve2 import *
from Rolling import *
from Args import *


class Hypotrochoid(Rolling,Curve2):

    phi=0.0

    
    ##!
    ##! Rolling angular velocity: (a+b)/b
    ##!

    def Hypotrochoid_Omega(self):
        return (self.a-self.b)/self.b

    ##!
    ##! Rolling \lambda (relative poop size) parameter
    ##!

    def Hypotrochoid_Lambda(self):
        return (self.b+self.c)/self.b

    ##!
    ##! Rolling first ratio.
    ##!

    def Curve_Rolling_a(self):
        return self.b

    ##!
    ##! Rolling second ratio.
    ##!

    def Curve_Rolling_b(self):
        return self.b+self.c


    ##!
    ##! Radius of rolling circle.
    ##!

    def Rolling_Circle_Radius(self):
        return self.Curve_Rolling_a()
    
    ##!
    ##! Get n skew necessary for rolling circles to become right.
    ##!

    def Curve_Rolling_Skew(self):
        return 0
     
    ##!
    ##! Rolling angle: omega*t+phi
    ##!

    def Hypotrochoid_Rolling_Angle(self,t):
        return t*self.Hypotrochoid_Omega()+self.phi


 
    ##!
    ##! Get rolling normal
    ##!

    def Curve_Rolling_Normal(self,n):
        t=self.ts[n]
        t=self.Hypotrochoid_Rolling_Angle(t)
        
        return E(t)


   ##!
    ##! Get rolled angle
    ##!

    def Curve_Rolling_Rolled_Normal(self,n):
        t=self.ts[n]
        
        return E(t)
    
    
    
    ##!
    ##! Get rolling center
    ##!

    def Curve_Rolling_Center(self,n):
        t=self.ts[n]
        
        return Vector([cos(t),sin(t)])*(self.a-self.b)
    

        
    ##!
    ##! Rolling coord system size
    ##!

    def Curve_Rolling_RCS_Size(self):
        return self.b

    ##!
    ##! Hypotrochoid: Rolling one circle (r=b) inside another, ratio a. Poop size: c
    ##!

    def Hypotrochoid_Calc(self,t):
        rtheta=self.Hypotrochoid_Rolling_Angle(t)
        
        return E(t)*(self.a-self.b) -P( rtheta )*(self.c+self.b)
   
    ##!
    ##! Hypotrochoid evolute calculating the phi(t) function.
    ##!

    def Hypotrochoid_Evolute_Phi(self,t,omega,lmbda):        
        coss=cos( (omega+1.0)*t )

        counter=(1.0+lmbda**2-2.0*lmbda*coss)
        donominator=1.0-lmbda**2*omega-lmbda*(1.0-omega)*coss

        phi=counter
        if (donominator!=0.0):
            phi=counter/donominator

        return phi
    
    ##!
    ##!  Hypotrochoid evolute calculating function
    ##!

    def Hypotrochoid_Evolute_Calc(self,t):
        omega=self.Hypotrochoid_Omega()
        lmbda=self.Hypotrochoid_Lambda()
        
        phi=self.Hypotrochoid_Evolute_Phi(t,omega,lmbda)
        
        fact1=omega*(1.0-phi)
        fact2=lmbda*(1.0+omega*phi)

        return ( E(t)*fact1-P( omega*t )*fact2 )*self.b
    
    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        f=2.2*(abs(self.a)+abs(self.b)+abs(self.c))
        return Vector([-f,-f])
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        f=2.2*(abs(self.a)+abs(self.b)+abs(self.c))
        return Vector([f,f])
        
    
    ##!
    ##! Draw Epitrochoid extra curves
    ##!

    def Curve_Draw(self,n,nframe):
        parms={
        }

        Curve2.Curve_Draw(self,n,nframe)
        self.Curve_Rolling_Circle_Draw(n)
        o=Vector([ 0.0,0.0 ])
        self.Canvas().Draw_Circle(o,self.a,"Rolling_Fixed")

        
    ##!
    ##! Set self.t1 and self.t2 for animation. Meant to be overridden!
    ##!
    
    def Animations_Set_Ts(self,a,b,c):
        self.t2=self.b*2.0*pi
        
        return
        
    ##!
    ##! Hypotrochoid analytical evolute parms
    ##!
    
    def Calc_Evolute_Analytical_Parms(self):
        omega=self.Hypotrochoid_Omega()
        fact=self.a/(self.a-2.0*self.b)
        
        return {
            "Canvas":       self.Canvas,
            "Parent":       self,
            "rc":           self.rc,
            "Name":         "Analytical_Evolute",
            "Type":         self.Name+"_Analytical",
            "t1":           self.t1,
            "t2":           self.t2,
            "NPoints":      self.NPoints,
            "nlaps":        1,
            "phi":          self.phi+pi,
            "a":            fact*self.a,
            "b":            fact*self.b,
            "r0":           [ 0,0 ],
            "Print":        0,
            
            "Mesh_Last":               True,
            "Point_Size":              3,
            "CalcGeo":                 False,
            "Reparametrization":       False,
            "Evolute_Anal":            False,
            "RCS":                     True,
            "Rolling_Circle":          True,
            "Rolling_Center":          True,
            "Rolling_Extended_Vector": True,
        }
        
    ##!
    ##! Create analytical evolute as a curve object.
    ##!
    
    def Calc_Evolute_Analytical_Obj(self):
        return Hypotrochoid(self.Calc_Evolute_Analytical_Parms())

    ##!
    ##! Optional test for whether we should actually generate the curve.
    ##!
    
    def Animation_Should(self,a,b,c):
        if (a==2.0*b): return False
        
        return True
    ##!
    ##! Run animation
    ##!

    def Run(self):
        self.CLI2Obj()
        ass=[2.0,3.0,4.0,5.0]
        #ass=[4.0]
        
        bss=[ 1.0,2.0,3.0 ]
        #bss=[4.0]
        for a in ass:
            parms={
                "a": [ a ],
                "b": bss,
                "c": [
                    0.0,
                    -0.75,-0.5,-0.25,-0.2,-0.15,-0.1,-0.05,
                    0.25,0.5,0.75,1.0,
                    2.0
                ],
                "n": [ 400 ],
                "Types": [ "Curve", ],
            }

            timer=Timer("Generating Animations: ")

            self.Animations_Run(parms)


            canvas=Canvas2(
                {},
                [ self.Curve_Min(),self.Curve_Max() ],
                self.Resolution
            )

            baseparm=str(a)+"-1.0-0.0-400"
            name="Hypotrochoid"
            path="curves/"+name+"/"
            self.SVGs_Parms_Overlays(
                "curves/"+name,
                name,
                canvas,
                parms,
                [
                    "curves/Hypotrochoid/Curve-"+baseparm+".svg",
                ]
            )

            parms[ "Types" ].append("Numerical_Evolute")
            path="curves/"+name+"/"
            self.SVGs_Parms_Overlays(
                "curves/"+name,
                "Curve-Evolute",
                canvas,
                parms,
                [
                    "curves/Hypotrochoid/Curve-"+baseparm+".svg",
                    "curves/Hypotrochoid/Numerical_Evolute-"+baseparm+".svg",
                ]
            )
 
           
parms={
}
Args_Files_Add(["Curves/Hypotrochoid.inf"])


curve=Hypotrochoid(parms)
curve.Run()
