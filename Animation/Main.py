import gd,os,time

from Html import Animation_Html
from Iteration import Animation_Iteration
from Write import Animation_Write

from Base import *
from Canvas2 import *
from Canvas2 import Canvas2
from Image import Image
from HTML import HTML

__Canvas__=None

class Animation(
        Animation_Html,
        Animation_Iteration,
        Animation_Write,
        Base,HTML
    ):
    Convert_Bin="/usr/bin/convert"
    HTML_Root="http://127.0.0.1/Graphics"
    CGI_Root="http://127.0.0.1/cgi-bin/Graphics/Display.py"
    
    __Switches__={
        "v": {
            "Attr": "Verbose",
            "Text": "Verbosity level. Augment to see more numbers...",
            "Type": None,
        },
        "-clean": {
            "Attr": "Clean",
            "Text": "Remove PNGs generated",
            "Type": "int",
        },
        "-rewrite": {
            "Attr": "Images_Rewrite",
            "Text": "Rewrite image file between iterations",
            "Type": None,
        },
        "l": {
            "Attr": "Loop",
            "Text": "Animated GIF no of loops (passed to convert)",
            "Type": None,
        },
        "d": {
            "Attr": "Delay",
            "Text": "Animated GIF delay (passed to convert)",
            "Type": None,
        },
        "W": {
            "Attr": "W",
            "Text": "White background",
            "Type": "bool",
        },
    }

    __Args__=[]
    
    Indent="   "
    W=False
    Verbose=1
    Delay="5"
    Loop="0"
    
    Path="curves"
    Curve_Parms_Path=""
    FileName="Curve"
    Name="Curve"

    Parameters=["a","b","c"]
    Parameter_Names=["a","b","c"]
    
    Clean=0 #Clean up afterwords
    
    Iteration_Files=[]
    Images_Rewrite=1

    def __init__(self,pmin,pmax,vals={}):
        self.Hash2Obj(vals)
        self.__Canvas__=Canvas2(vals,[ pmin,pmax ])
        self.Canvas([ pmin,pmax ]).CLI2Obj()

    ##!
    ##! Overrride __str__ to print some useful info.
    ##!
    
    def __str__(self):
        text="Animation, Path: "+self.Path
        text+="\n\tFileName: "+self.FileName
        text+="\n\tParms: "+self.Curve_Parms_Path
        text+="\n\tLoop: "+self.Loop
        text+="\n\tDelay: "+self.Delay
        text+="\n\tClean: "+str(self.Clean)
        text+="\n"+str(self.Canvas())
        
        return text
    
    ##!
    ##! Returns Canvas object, stored in self.__Canvas__
    ##!
    
    def Canvas(self,pexts=[]):
        global __Canvas__    # Needed to modify global copy of __Canvas__
        if (not __Canvas__):
            parms={
            }
            
            __Canvas__=Canvas2(parms,pexts)

        return __Canvas__
    
    def BackGround_Color(self):
        if (self.W):
            return "White"
        else:
            return "Black"
   
    def Initialize(self):
        self.Canvas().Resolution=self.Resolution
        self.Canvas().Image_Rewrite()
