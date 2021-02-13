from Vector import *
from Mesh import *
from Canvas2 import Canvas2

class Curve_Write_SVG():
    ##! 
    ##! Write curve datas to files.
    ##!
    
    def Curve_Write_SVG(self,canvas,path):
        self.Curve_Write_SVG_R(canvas,path)
        self.Curve_Write_SVG_dR(canvas,path)
        self.Curve_Write_SVG_d2R(canvas,path)
        
        self.Curve_Write_SVG_T(canvas,path)
        self.Curve_Write_SVG_N(canvas,path)
        
        if (self.Involute_Numerical):
            self.Curve_Write_SVG_Involute_Numerical(canvas,path)

        if (self.Evolute_Numerical):
            self.Curve_Write_SVG_Determinant(canvas,path)
            self.Curve_Write_SVG_Phi(canvas,path)
            self.Curve_Write_SVG_Evolute_Numerical(canvas,path)

        if (self.Evolute_Anal):
            self.Curve_Write_SVG_Evolute_Analytical(canvas,path)
            
        if (self.Roulette):
            self.Curve_Write_SVG_Roulette(canvas,path)

    ##! 
    ##! Write curve R to file.
    ##!
    
    def Curve_Write_SVG_R(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="R.svg"
        if (not classs):   classs="Curve"
        if (not color):    color="blue"
        
        self.Curve_SVGs(canvas,path+"/"+filename,classs,color)

    ##! 
    ##! Write curve dR to file.
    ##!
    
    def Curve_Write_SVG_dR(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="dR.svg"
        if (not classs):   classs="Curve"
        if (not color):    color="green"
        
        self.Curve_SVG_Velocities(canvas,path+"/"+filename,classs,color)

    ##! 
    ##! Write curve d2R to file.
    ##!
    
    def Curve_Write_SVG_d2R(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="d2R.svg"
        if (not classs):   classs="Curve"
        if (not color):    color="green"

        self.Curve_SVG_Accelerations(canvas,path+"/"+filename,classs,color)


    
    ##! 
    ##! Write curve T to file.
    ##!
    
    def Curve_Write_SVG_T(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="T.svg"
        if (not classs):   classs="Curve"
        if (not color):    color="green"

        self.Curve_SVG_Ts(canvas,path+"/"+filename,classs,color)

    
    ##! 
    ##! Write curve N to file.
    ##!
    
    def Curve_Write_SVG_N(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="N.svg"
        if (not classs):   classs="Curve"
        if (not color):    color="green"

        self.Curve_SVG_Ns(canvas,path+"/"+filename,classs,color)

    ##! 
    ##! Write curve phi(t) to file, as a function.
    ##!
    
    def Curve_Write_SVG_Determinant(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="Det.svg"
        if (not classs):   classs="Curve"
        if (not color):    color="green"

        f=Mesh("Determinant", len(self.ts) )
        for i in range( len(self.ts) ):
            f[i]=Vector([ self.ts[i],self.Determinant[i] ])

        f.Mesh_SVG_Draw_With_Coordinate_System(
            path+"/"+filename,
            classs,
            color,
            [self.Resolution[0],300]
        )
    ##! 
    ##! Write curve phi(t) to file, as a function.
    ##!
    
    def Curve_Write_SVG_Phi(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="phi.svg"
        if (not classs):   classs="Curve"
        if (not color):    color="blue"

        f=Mesh("Phi",[])
        for i in range( len(self.ts) ):
            f.append( Vector([ self.ts[i],self.Phi[i] ]) )

        f.Mesh_SVG_Draw_With_Coordinate_System(
            path+"/"+filename,
            classs,
            color,
            [self.Resolution[0],300]
        )

    
    ##! 
    ##! Write curve Numerical Involute to file.
    ##!
    
    def Curve_Write_SVG_Involute_Numerical(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="C_IN.svg"
        if (not classs):   classs="Involute_Numerical"
        if (not color):    color="brown"

        self.Curve_SVG_Involute_Numerical(canvas,path+"/"+filename,classs,color)

    ##! 
    ##! Write curve Numerical Evolute to file.
    ##!
    
    def Curve_Write_SVG_Evolute_Numerical(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="C_EN.svg"
        if (not classs):   classs="Evolute_Numerical"
        if (not color):    color="orange"

        self.Curve_SVG_Evolute_Numerical(canvas,path+"/"+filename,classs,color)

    ##! 
    ##! Write curve Analytical Evolute to file.
    ##!
    
    def Curve_Write_SVG_Evolute_Analytical(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="C_EA.svg"
        if (not classs):   classs="Evolute_Analytical"
        if (not color):    color="red"

        self.Curve_SVG_Evolute_Analytical(canvas,path+"/"+filename,classs,color)
        
    ##! 
    ##! Write curve Roulette to file.
    ##!
    
    def Curve_Write_SVG_Roulette(self,canvas,path,filename="",classs="",color=""):
        if (not filename): filename="C_R.svg"
        if (not classs):   classs="Evolute_Analytical"
        if (not color):    color="orange"

        self.Curve_SVG_Roulette(canvas,path+"/"+filename,classs,color)

