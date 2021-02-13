from math import *

import sys

sys.path.insert(0,'/usr/local/Python')

from Vector import *
from Curve2 import *
from Rolling import *
from Args import *


class Epitrochoid(Rolling,Curve2):

    phi=0.0

    ##!
    ##! Rolling angular velocity: (a+b)/b, \omega parameter
    ##!

    def Epitrochoid_Omega(self):
        return (self.a+self.b)/self.b

    ##!
    ##! Rolling \lambda (relative poop size) parameter
    ##!

    def Epitrochoid_Lambda(self):
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
        return self.b
    

    ##!
    ##! Get n skew necessary for rolling circles to become right.
    ##!

    def Curve_Rolling_Skew(self):
        return 0
    ##!
    ##! Rolling angular velocity: (a+b)/b
    ##!

    def Epitrochoid_Rolling_Angle(self,t):
        return t*self.Epitrochoid_Omega()+self.phi

     
    ##!
    ##! Get rolled angle
    ##!

    def Curve_Rolling_Normal(self,n):
        t=self.ts[n]
        theta=self.Epitrochoid_Rolling_Angle(t)
        return E(theta)*(-1.0)
    
    ##!
    ##! Get rolled angle
    ##!

    def Curve_Rolling_Rolled_Normal(self,n):
        t=self.ts[n]

        return E(t)*(-1.0)
    
       
    ##!
    ##! Get rolling center
    ##!

    def Curve_Rolling_Center(self,n):
        t=self.ts[n]
        v=Vector([cos(t),sin(t)])*(self.a+self.b)

        return v
    
    ##!
    ##! Rolling coord system size
    ##!

    def Curve_Rolling_RCS_Size(self):
        return self.b

       
    ##!
    ##! Epitrochoid: Rolling one circle (r=b) outside another, ratio a. Poop size: c.
    ##!
    def Epitrochoid_Calc(self,t):
        rtheta=self.Epitrochoid_Rolling_Angle(t)

        return E(t)*(self.a+self.b)-E( rtheta )*(self.c+self.b)

    ##!
    ##! Epitrochoid evolute calculating the phi(t) function.
    ##!

    def Epitrochoid_Evolute_Phi(self,t):        
        omega=self.Epitrochoid_Omega()
        lmbda=self.Epitrochoid_Lambda()
        
        coss=cos( (omega-1)*t )
        
        counter=1.0+lmbda**2-2.0*lmbda*coss
        donominator=1.0+lmbda**2*omega-lmbda*(1.0+omega)*coss
        
        phi=counter
        if (donominator!=0.0):
            phi=counter/donominator

        return phi
    
    ##!
    ##! Epitrochoid evolute calculating function
    ##!

    def Epitrochoid_Evolute_Calc(self,t):
        omega=self.Epitrochoid_Omega()
        lmbda=self.Epitrochoid_Lambda()
        
        phi=self.Epitrochoid_Evolute_Phi(t)
        
        fact1=omega*(1.0-phi)
        fact2=lmbda*(1.0-omega*phi)

        #print fact1,fact2
        return (E(t)*fact1-E ( omega*t )*fact2)*self.b
    
    ##!
    ##! Draw Epitrochoid extra curves
    ##!
    def Curve_Draw(self,n,nframe):

        self.Curve_Rolling_Circle_Draw(n)
        #self.Canvas().Draw_Circle([0.0,0.0],self.a,"Fixed")
        self.Canvas().Draw_Circle([0.0,0.0],self.a,"Rolling_Fixed")
        Curve2.Curve_Draw(self,n,nframe)

        

    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        f=1.0*(abs(self.a)+2.0*abs(self.b)+abs(self.c))
        return Vector([-f,-f])
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        f=1.0*(abs(self.a)+2.0*abs(self.b)+abs(self.c))
        return Vector([f,f])
    
    ##!
    ##! Set self.t1 and self.t2 for animation. Meant to be overridden!
    ##!
    
    def Animations_Set_Ts(self,a,b,c):
        self.t2=max(2*pi,2.0*self.b/self.a*pi)
        
        return
        
    ##!
    ##! Epitrochoid analytical evolute parms
    ##!
    
    def Calc_Evolute_Analytical_Parms(self):
        omega=self.Epitrochoid_Omega()
        fact=self.a/(self.a+2.0*self.b)

        analyticalrolling=False
        if (self.c==0.0):
            analyticalrolling=True
        
        parms={
            "Canvas":       self.Canvas,
            "Parent":       self,
            "Name":         "Analytical_Evolute",
            "Type":         self.Name+"_Analytical",
            "rc":           "Epitrochoid_Evolute_Calc",
            "t1":           self.t1,
            "t2":           self.t2,
            "NPoints":      self.NPoints,
            "nlaps":        1,
            "phi":          self.phi,
            "a":            self.a,
            "b":            self.b,
            "r0":           [ 0,0 ],
            "Print":        0,
            
            "Mesh_Last":               True,
            "Point_Size":              3,
            "CalcGeo":                 False,
            "Reparametrization":       False,
            "Evolute_Anal":            False,
            "RCS":                     analyticalrolling,
            "Rolling_Circle":          analyticalrolling,
            "Rolling_Center":          analyticalrolling,
            "Rolling_Extended_Vector": analyticalrolling,
        }

        if (analyticalrolling):
            parms[ "rc" ]=self.rc
            parms[ "a" ]=fact*self.a
            parms[ "b" ]=fact*self.b
            parms[ "c" ]=0.0
            parms[ "phi" ]=self.phi+pi

        return parms
            
        
    ##!
    ##! Create analytical evolute as a curve object.
    ##!
    
    def Calc_Evolute_Analytical_Obj(self):
        return Epitrochoid(self.Calc_Evolute_Analytical_Parms())


        
    ##!
    ##! Run animation
    ##!

    def Run(self):
        self.Parameter_Names=["R","r","b"]
        self.CLI2Obj()

        n=5
        ass=[]
        bss=[1.0] #canonical evolutes

        css=[
            0.0,
            -0.75,-0.5,-0.25,-0.2,-0.15,-0.1,-0.05,
            0.25,0.5,0.75,
        ]
        
        for a in range(1,n+1):
            ass.append( 1.0*a )
        for a in range(2,n+1):
            ass.append( 1.0/(1.0*a) )
            
        for a in range(1,n+2):
            css.append( 1.0*a )
        for a in range(1,n+2):
            css.append( -1.0*a )

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
            continue
            canvas=Canvas2(
                {},
                [ self.Curve_Min(),self.Curve_Max() ],
                self.Resolution
            )

            
            baseparm=str(a)+"-1.0-0.0-400"
            name="Epitrochoid"
            path="curves/"+name+"/"
            self.SVGs_Parms_Overlays(
                "curves/"+name,
                name+"-"+str(a),
                canvas,
                parms,
                [
                    #"curves/Epitrochoid/Curve-"+baseparm+".svg",
                ]
            )

            parms[ "Types" ].append("Numerical_Evolute")
            path="curves/"+name+"/"
            self.SVGs_Parms_Overlays(
                "curves/"+name,
                name+"-Evolute"+"-"+str(a),
                canvas,
                parms,
                [
                    #"curves/Epitrochoid/Curve-"+baseparm+".svg",
                    #"curves/Epitrochoid/Numerical_Evolute-"+baseparm+".svg",
                ]
            )

 
parms={
    "Parameter_Names": ["R","r","b" ],
}
Args_Files_Add(["Curves/Epitrochoid.inf"])

curve=Epitrochoid(parms)
curve.Run()
