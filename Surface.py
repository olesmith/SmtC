from math import *
import re,sys,time

from Animation import *
from Canvas3 import *
from Mesh import *
from Vector import *
from Base import *



class Surface(Base):

    __Switches__={
        "v":      "Verbose",
        "n":      "n",
        "z":      "Zoom",
        "-nlaps": "nlaps",
        "-eps":   "eps",
        "a":      "a",
        "b":      "b",
        "c":      "c",
        "R":      "Reparametrization",
        "P":      "Print",
        "E":      "Evolute",
        "-poop":  "Poop"
    }
    __Switches_Text__={
        "v":     "Set verbose level",
        "n":      "Noof points",
        "z":     "Zoom",
        "-nlaps": "No of laps",
        "-eps":   "Epsilon used for derivatives",
        "a":      "a parameter for curves generated",
        "b":      "b parameter for curves generated",
        "c":      "c parameter for curves generated",
        "R":      "Do arc length reparametrization",
        "P":      "Print Curve info",
        "E":      "Draw evolute",
        "poop":   "Add Poop picture no."
    }
    __Args__=["rc","nx","ny"]
    __Args_Text__=["Function generating surface","No of points"]
    
    __Animation__=""
    
    __Canvas3__=None
    
    Verbose=0
    Name="Surfaces"
    Resolution=[800,800]

    Zoom=1.0
    
    dim=2
    rc=""
    eps=1.0E-3
    eps2inv=0
    

    nu=50
    nv=50

    u1=0.0
    u2=10.0
    du=0.0
    
    v1=0.0
    v2=10.0
    dv=0.0
    
    UVs=[]
    R=[]
 
    ##!
    ##! Creator.
    ##!
    
    def __init__(self,vals={}):
        self.Hash2Obj(vals)
           
        self.SetParms()

    ##!
    ##! Sets eps parms.
    ##!
    
    def SetParms(self):
        self.du=(self.u2-self.u1)/(1.0*self.nu)
        self.dv=(self.v2-self.v1)/(1.0*self.nv)
        self.eps2inv=1.0/(2.0*self.eps)

        self.eps2inv=1.0/(2.0*self.eps)

        self.R=Mesh()
        self.Canvas3()
        

    def Canvas3(self,parms={}):
        if (not self.__Canvas3__):
            self.__Canvas3__=Canvas3(parms)
            
        return self.__Canvas3__
       
    def Canvas_Init(self,p1,p2):
        self.Canvas3().Verbose=1
        self.Canvas3().Canvas_Init(p1,p2)
        print self.Verbose
    
    ##!
    ##! Call coordinate generating function, parameter t.
    ##! Name in slef.rc; should return a list of numbers.
    ##!
    
    def r(self,u,v):
        method=getattr(self,self.rc)
        return Vector( method(u,v) )

    def Calc_UVs(self):
        self.UVs=[]
        
        u=self.u1
        for i in range(self.nu+1):
            self.UVs.append([])
            
            v=self.v1
            for j in range(self.nv+1):
                self.UVs[i].append([u,v])
                v+=self.dv
            u+=self.du

        return self.UVs[i]

    def Conns_UV(self):
        conns=[]
        for i in range(self.nu+1):
            for j in range(self.nv+1):
                print i,j
            
        return conns

    def Calc_Rs(self):
        self.R=Mesh([])
        
        for i in range(self.nu+1):
            for j in range(self.nv+1):
                u=self.UVs[i][j][0]
                v=self.UVs[i][j][1]
                r=self.r(u,v)
                print r
                self.R.append(r)

        return self.R

    ##!
    ##! Do actual curve drawing: draw mesh - and optionally evolute.
    ##!
    
    def Draw(self,n=0,canvas=None,color=""):
        if (not canvas):
            canvas=self.Canvas3()
            
        self.R.Draw(canvas,n,color)

    def Helix(self,u,v):
        return [ u*cos(v),u*sin(v),v]

surface=Surface()
surface.rc="Helix"

surface.Calc_UVs()
surface.Calc_Rs()
surface.Draw()

