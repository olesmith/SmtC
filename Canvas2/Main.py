from Image import *
from Vector import *

from Draw import Canvas2_Draw

class Canvas2(Canvas2_Draw,Image):
    HTML_Root=""
    
    __Switches__={
        "v": {
            "Attr": "Verbose",
            "Text": "Verbosity level. Augmento to see more numbers...",
            "Type": "int",
        },
        "rx": {
            "Attr": "RX",
            "Text": "X Resolution",
            "Type": "int",
        },
        "ry": {
            "Attr": "RY",
            "Text": "Y Resolution",
            "Type": "int",
        },
        "W": {
            "Attr": "W",
            "Text": "White background",
            "Type": "bool",
        },
    }
    
    __Args__=[]
    
    Verbose=0
    

    #Converts Points and Vectors to pixels:
    #  px=A*p+b
    A=[]
    B=[]

    pmin=None
    pmax=None
    dp=None
    
    Eps=0.05 #pixel margin %
    
    
    def __init__(self,vals={},pexts=[],resolution=[]):
        self.A=Vector([1.0,1.0])
        self.B=Vector([0.0,0.0])
        
        self.CLI2Obj()
        self.Hash2Obj(vals)

        if (resolution):
            self.Resolution=resolution

        #if (pexts):
        self.Canvas_Init(pexts[0],pexts[1])
        
       
    def __str__(self):
        text="Canvas2, Path: "
        text+="Pix Margin: "+str(self.Eps)
        text+="\n\tR: "+str(self.Resolution)
        text+="\n\tA: "+str(self.A)
        text+="\n\tb: "+str(self.B)
        text+="\n\tpmin: "+str(self.pmin)
        text+="\n\tpmax: "+str(self.pmax)

        return text

    
    def Canvas_Init(self,p1,p2):
        p=p2-p1


        #Store min/max point
        self.pmin=p1
        self.pmax=p2
        self.dp=p
        
        dp=p*self.Eps
        p1-=dp
        p2+=dp

        p=p2-p1
        self.A=Vector([1.0,1.0])
        self.B=Vector([0.0,0.0])

        for i in range(2):
            self.A[i]=self.Resolution[i]/p[i]
            self.B[i]=-self.A[i]*p1[i]

    def P2Pix(self,p):
        px=Vector()
        for i in range(2):
            px.append( self.A[i]*p[i]+self.B[i] )
            
        #Flip point vertically, as (0,0) in lower left
        px[1]=self.Resolution[1]-px[1]
        return px
            
    def V2Pix(self,p):
        px=Vector()
        for i in range(2):
            px.append( self.A[i]*p[i] )
            
        #Flip vector vertically, as (0,0) in lower left
        px[1]=-px[1]
        return px
            
    def Ps2Pix(self,ps):
        pxs=[]
        for i in range( len(ps) ):
            pxs.append( self.P2Pix(ps[i]) )
            
        return pxs
