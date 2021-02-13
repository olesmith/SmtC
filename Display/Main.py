#import os
import sys


from Base import *
from HTML import *
from CGI import *

from Setup     import Display_Setup
from Headers   import Display_Headers
from Top       import Display_Top
from Middle    import Display_Middle
from Bottom    import Display_Bottom

from Head      import Display_Head
from Body      import Display_Body
from LeftMenu  import Display_LeftMenu

from Central    import Display_Central
from SVG        import Display_SVG
from Carousel   import Display_Carousel
from Frames     import Display_Frames

class Display(
        Display_Setup,
        Display_Headers,
        Display_Top,
        Display_Middle,
        Display_Bottom,
        Display_Head,
        Display_Body,
        Display_LeftMenu,
        Display_Central,
        Display_SVG,
        Display_Carousel,
        Display_Frames,
        HTML,
        CGI
    ):
    
    FS_Root="/usr/local/Python"
    HTML_Root="http://127.0.0.1/"
    CGI_Root="http://127.0.0.1/cgi-bin/"
    

    Setup={}
    BasePath="curves"
    HtmlPath="/"
    Indent="-->"
    Indent="   "

    Titles=[
        "Poopys",
        "Computational and Differential Geometry",
        "Instituto de Matem&aacute;tica e Estat&iacute;stica",
        "Universidade Federal de Goi&aacute;s",
        "Prof. Ole Peter Smith"
    ]
    
    Title="Poopys"
    
    
    Animation_Titles=[
        "Carousel",
    ]
    
    Animation=None
    Animation_Parms=[]
    
    
    def __init__(self):
        return
    
    def Display_HTTP_Headers_Print(self,content="text/html\n"):
        print  self.CGI_HTTP_Header(content)
    
    def Display_Generate(self):
        self.Display_HTTP_Headers_Print()
         
        html=[]
        
        html=html+self.HTML_Header()
        html=html+[ self.Display_Body() ]
        html=html+[ self.Display_Tailer() ]

        print self.HTML_Print(html)

    
    def Display_Animation_Parms_Set(self):
        comps=self.CGI_Query_Path().split('/')
        
        if ( len(comps)>0 ):
            self.Animation=comps[0]
            del comps[0]
            self.Animation_Parms=comps
        
    def Display_Animation_Parms(self):
        if (not self.Animation):
            self.Display_Animation_Parms_Set()
            
        return self.Animation_Parms
        
    def Display_Animation(self):
        if (not self.Animation):
            self.Display_Animation_Parms_Set()
            
        return self.Animation
