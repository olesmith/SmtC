from CS import *
from Mesh import *
from Animation import *
from Canvas2 import *
from Image import *
from Mesh import *
from Vector import *
from Base import *
import traceback

from HTML        import HTML
from CGI         import CGI

from Parms       import Curve_Parms
from Calc        import Curve_Calc
from ArcLength   import Curve_ArcLength
from Init        import Curve_Init
from Print       import Curve_Print
from SVG         import Curve_SVG
from Curve.Write import Curve_Write
from Connections import Curve_Connections
from Colors      import Curve_Colors
from Draw        import Curve_Draw
from Samples     import Curve_Samples
#from Roulette    import Roulette
from Oids        import Curve_Oids

__Animation__=None


class Curve(
        HTML,CGI,
        CS,
        Curve_Init,
        Curve_Calc,
        Curve_Parms,
        Curve_SVG,
        Curve_ArcLength,
        Curve_Draw,
        Curve_Colors,
        Curve_Connections,
        Curve_Print,
        Curve_Write,
        Curve_Samples,
        Curve_Oids
    ):

    Type="Curve"
    CSS_Class="Curve"
    
    BasePath="curves"
    Indent="   "
    Parent=None
    __Animation__=None
    
    #Curve info will be printed, if self.Print set to >0
    Print=0
    #Curve will be calculated, if self.CalcGeo set
    CalcGeo=False
    #Curve will be reparametrisized if self.Reparametrization set
    Reparametrization=False
    
    #Accompanying Coord System
    #Draw World/Accompanying Coordinate Systems
    WCS=False
    ACS=False

    #Draw osculating circle and/or vector.
    Osculating_Circle=False
    Osculating_Vector=False

    
    #Draw last mesh point
    Mesh_Last=False
    #Drawing color
    Color="blue"

    Point_Size=2
    Last_Point_Size=5

    #Default resolution
    Resolution=[800,800]

    #Global curve parameters
    a=1.0
    b=1.0
    c=0.0

    #Phasing parameter
    phi=0.0
    
    t1=0.0
    t2=1.0
    dt=1.0
    NPoints=100
    NFrames=100
    
    rc=""

    ts=[]
    R=[]
    dR=[]
    d2R=[]
    T=[]
    N=[]

    #Curve (Arc) Lengths
    S=[]
    dS=[]
    
    Closed=False

    #Curve length. If defined will be used to calculate curve lengths.
    S_rc=""
    Curve_Lengths=True
    Integration_Method=1 #1: Trapezoids, 2: Simpson
    
    #Numerical Involute will be calculated, if set
    Involute_Numerical=False
    #Numeric Involute points
    Involute_R=None
    
   #Numerical Evolute will be calculated, if set
    Evolute_Numerical=False
    #Numeric Curvature centers
    Evolute_R=None
    
    #Do we have an Analytical Evolute?
    Evolute_Anal=False
    Evolute_Analytical=None
    Evolute_rc=""
    
    Determinant=[]
    Kappa=[]
    Rho=[]
    Phi=[]
    
    
    #Generate Roulette
    Roulette=False
    Roulette_rc=""
    Parent_rc=""
    Roulette_Direction=1.0
    Roulette_A=1.0
    Roulette_B=1.0
    
    ##!
    ##! Creator.
    ##!
    
    def __init__(self,vals={}):
        self.Hash2Obj(vals)
        self.SetParms()
        self.Type=self.__class__.__name__

    def __str__(self):
        return self.Name

    ##!
    ##! Sets eps parms.
    ##!
    
    def SetParms(self,vals={}):
        self.CS_SetParms(vals)

        self.R=Mesh(self.Name)

 
    ##!
    ##! Get n skew necessary for rolling circles to become right.
    ##!

    def Curve_Rolling_Skew(self):
        return 0
    ##!
    ##! Returns color for named entity types.
    ##!
    
    def GetColor(self,type=""):
        animation=self.Animation()

        scheme=animation.BackGround_Color()
        
        if (type==""):
            return scheme

        return self.Color_Schemes[ scheme ][ type ]
    
    ##!
    ##! Returns Animation object for controlling the process.
    ##!
    
    def Animation(self):
        global __Animation__    # Needed to modify global copy of __Animation__

        if (not __Animation__):
            parms={
                "Curve_Parms_Path": self.Curve_Parms_Path(),
                "Name": self.Type,
                "FileName": self.Type,
                "Resolution": self.Resolution,
                "pmin": self.Curve_Min(),
                "pmax": self.Curve_Max(),
            }
            __Animation__=Animation(self.Curve_Min(),self.Curve_Max(),parms)
            __Animation__.Curve_Parms_Path=self.Curve_Parms_Path()
              
            __Animation__.Initialize()
            __Animation__.Resolution=self.Resolution

        return __Animation__

    ##!
    ##! Returns Canvas object, stored in self.Animation
    ##!
    
    def Canvas(self):
        return self.Animation().Canvas()

    
    ##!
    ##! Applies command line options and arguments to Curve object.
    ##!
    
    def CLI_Apply(self):
        self.CLI2Obj()
        self.eps=float(self.eps)
        
    
    ##!
    ##! Generate roulette as a curve
    ##!
    
    def Calc_Roulette(self):
        parms={
                "Parent":       self,
                "Name":         self.Name+"Roulette",
                "rc":           "Curve_Roulette_Calc",
                "Name":         "Roulette",
                "Type":         "Curve_Roulette",
                "t1":           self.t1,
                "t2":           self.t2,
                "NPoints":      self.NPoints,
                "nlaps":        1,
                "Roulette_A":   self.Roulette_A,
                "Roulette_B":   self.Roulette_B,
                "r0":           [ 0,0 ],
                "Print":        0,
                "Mesh_Last":               True,
                "CalcGeo":                 True,
                "Point_Size":              3,
            
                "Reparametrization":       False,
                "Evolute_Numerical":       False,
                "Evolute_Anal":            False,
                "Closed":                  False,
        }

        from Roulette import Roulette

        self.Roulette=Roulette(parms)
        self.Roulette.Parent=self

        self.Roulette.Calc(self.ts)
        self.Roulette.Category="Roulette"
        
 
    ##!
    ##! Return analyutical evolute parameters
    ##!
    
    def Calc_Evolute_Analytical_Parms(self):
        return {
            "Parent":       self,
            "rc":           self.Evolute_rc,
            "Name":         "Analytical_Evolute",
            "Type":         self.Name+"_Analytical",
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
        }
    
    ##!
    ##! Create analytical evolute as a curve object.
    ##!
    
    def Calc_Evolute_Analytical_Obj(self):
        return Curve(self.Calc_Evolute_Analytical_Parms())

    
    ##!
    ##! Generate roulette as a curve
    ##!
    
    def Calc_Evolute_Analytical(self):        
        self.Evolute_Analytical=self.Calc_Evolute_Analytical_Obj()
        self.Evolute_Analytical.Calc(self.ts)
        self.Evolute_Analytical.Parent=self
        self.Evolute_Analytical.Category="Analytical_Evolute"
        self.Evolute_Analytical.R.Name="Analytical_Evolute"

        
