from math import *
import re,sys,time

from Animation import *
from Canvas2 import *
from Curve import *
from Mesh import *
from Vector import *
from Base import *
from Timer import Timer

__Animation__=None


class Curve2(Curve):

    #CLI=0
    __Switches__={
        "1": {
            "Attr": "One",
            "Text": "One set of Parameters only",
            "Type": "bool",
        },
        "v": {
            "Attr": "Verbose",
            "Text": "Verbosity level. Augment to see more numbers...",
            "Type": None,
        },
        "NP": {
            "Attr": "NPoints",
            "Text": "No of curve points",
            "Type": "int",
        },
        "NF": {
            "Attr": "NFrames",
            "Text": "No of frames points",
            "Type": "int",
        },
        "z":  {
            "Attr": "Zoom",
            "Text": "Zoom",
            "Type": "float",
        },
        "-nlaps": {
            "Attr":  "nlaps",
            "Text": "No of laps. Will multiply n by nlaps.",
            "Type": "int",
        },
        "-eps":  {
            "Attr": "eps",
            "Text": "Epsilon used for derivatives",
            "Type": "float",
        },
        "a":  {
            "Attr": "a",
            "Text": "a parameter for curves generated",
            "Type": "float",
        },
        "b":  {
            "Attr": "b",
            "Text": "b parameter for curves generated",
            "Type": "float",
        },
        "c":   {
            "Attr": "c",
            "Text": "c parameter for curves generated",
            "Type": "float",
        },
        "R":  {
            "Attr": "Reparametrization",
            "Text": "Do arc length reparametrization",
            "Type": "bool",
        },
        "P":  {
            "Attr": "Print",
            "Text": "Print Curve info",
            "Type": "bool",
        },
        "EN":   {
            "Attr": "Evolute_Numerical",
            "Text": "Draw numerical evolute",
            "Type": "bool",
        },
        "EA":   {
            "Attr": "Evolute_Anal",
            "Text": "Draw analytical evolute",
            "Type": "bool",
        },
        "-poop":  {
            "Attr": "Poop",
            "Text": "Add Poop picture no.",
            "Type": "str",
        },
    }
    __Args__=[
        {
            "Attr": "NPoints",
            "Text": "No of curve points",
            "Type": "int",
        },
        {
            "Attr": "NFrames",
            "Text": "No of frames points",
            "Type": "int",
        },
        {
            "Attr": "rc",
            "Text": "Curve generating function (name)",
            "Type": "str",
        },
    ]
    
    
   
    Verbose=0
    Name="Curve"

    One=0

    nlaps=1
    Poop=0
    Zoom=1.0
    
    dim=2

    
    
    
 
    ##!
    ##! Animate curve drawing, producing sequence of images, each time with one more node.
    ##!
    
    def Draw_Animated(self):
        #20170613 self.CLI_Apply()
        self.Animation_Run()

    ##!
    ##! Animate curve drawing, producing sequence of images, each time with one more node.
    ##!
    
    def Animation_Run(self):
        self.NPoints=int(self.NPoints)
        self.NFrames=int(self.NFrames)
        self.nlaps=int(self.nlaps)
       
        print "a="+str(self.a),"b="+str(self.b),"c="+str(self.c),"n="+str(self.NPoints)
        self.a=float(self.a)
        self.b=float(self.b)
        self.c=float(self.c)
        self.Animation().Parameter_Names=self.Parameter_Names

        self.Animation().Curve_Parms_Path=self.Curve_Parms_Path()
        self.Animation().CLI2Obj()

        if (self.rc!=""):
            self.Calc()
            self.Curve_Print()
        
        if (self.Evolute_Anal):
            print "Draw Animated",self.Evolute_Analytical.Name
       
        timer=Timer("Generating Animation: "+str(self.NPoints+1)+" Iterations")

        dn=self.NPoints/self.NFrames

        for n in range(1,self.NFrames+1 ):
            self.Curve_Draw(n*dn,n)
            if (self.One): exit()

        self.Animation().Animation_Write(self)


    ##!
    ##! Set self.t1 and self.t2 for animation. Meant to be overridden!
    ##!
    
    def Animations_Set_Ts(self,a,b,c):
        return
    
    ##!
    ##! Optional test for whether we should actually generate the curve.
    ##!
    
    def Animation_Should(self,a,b,c):
        return True
    ##!
    ##! Detect initialized parameters, and run all.
    ##!
    
    def Animations_Run(self,parms):
        self.CLI_Apply()
        if (self.HasArgs()):
            self.Animation_Run()
            return

        for a in parms[ "a" ]:
            for b in parms[ "b" ]:
                for c in parms[ "c" ]:
                    for n in parms[ "n" ]:
                        if (self.Animation_Should(a,b,c)):
                            self.a=a
                            self.b=b
                            self.c=c
                            self.NPoints=n
                            self.NFrames=n
                            self.Animations_Set_Ts(a,b,c)
                            self.Animation_Run()
