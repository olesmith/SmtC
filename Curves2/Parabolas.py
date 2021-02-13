from math import *
import sys

sys.path.insert(0,'/usr/local/Python')

from Vector import *
from Curve2 import *
from Rolling import *
from Args import *



class Parabolas(Curve2):

    S_Calc="Parabola_S_Calc"
    ##!
    ##! Parabolas
    ##!

    def Parabola_Calc(self,t):
        
        return [ t,(self.a*t+self.b)*t+self.c ]

         
    ##!
    ##! Parabolas
    ##!

    def Parabola_Delta(self):        
        return self.b**2-4.0*self.a*self.c

    ##!
    ##! Parabolas
    ##!

    def Parabola_Vertex(self):        
        return Vector([
            -self.b/(2.0*self.a),
            -self.Parabola_Delta()/(4.0*self.a)
        ])

         
    ##!
    ##! Parabola analytical arc length 
    ##!

    def Parabola_S_Calc(self,t):        
        return 0.0

    ##!
    ##! returns parms name.
    ##!
    
    def Curve_Parms_Paths(self):
        b="%.12f" % (self.b+3.0)
        return  [str(self.a),b,str(self.c),str(self.NFrames)]
   
    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        return Vector([-2.0,-4.0])
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        
        return Vector([5.0,10.0])
   
    ##!
    ##! Run animation
    ##!

    def Run(self):
        self.CLI2Obj()

        self.NPoints=200
        self.t1=-2.0
        self.t2=2.0
        self.dt=(self.t2-self.t1)/(1.0*(self.NPoints-1))
        
        ncurves=100
        self.a=-1.0
        self.b=0.0
        self.c=0.0

        parabola=self.Calc_Rs()

        self.R=None
        parms={
            "a": [  1.0, 1.0 ],
            "b": [ -3.0, 3.0 ],
            "c": [  0.0, 0.0 ],
        }

        timer=Timer("Generating Curve Family: ")

        ds={}
        for parm in parms.keys():
            ds[ parm ]=(parms[ parm ][1]-parms[ parm ][0])/(1.0*(ncurves-1))

        values={}
        for parm in parms.keys():
            values[ parm ]=parms[ parm ][0]

        vertices=Mesh()
        vertices.Draw_Connections=False
        vertices.Draw_Mesh=True
        vertices.Point_Size=2
        vertices.Color="red"
        
        vertex=Mesh()
        vertex.append([])
        vertex.Draw_Connections=False
        vertex.Point_Size=5
        vertex.Draw_Mesh=True
        vertex.Color="blue"
        
        self.t1=-10.0
        self.t2=10.0
        self.dt=(self.t2-self.t1)/(1.0*(self.NPoints-1))
        
        for n in range(ncurves):
            #Retrieve parameters
            self.a=values[ "a" ]
            self.b=values[ "b" ]
            self.c=values[ "c" ]

            rvertex=self.Parabola_Vertex()
            vertex[0]=rvertex
            if ( (n%5)==0 ):
                vertices.append( rvertex )

            self.Calc(None,True,[ parabola,vertices,vertex ])
            
            #Increment parameters
            for parm in parms.keys():
                values[ parm ]+=ds[ parm ]

parms={
    "Resolution": [300,300],
}
Args_Files_Add(["Curves/Parabolas.inf"])

curve=Parabolas(parms)
curve.Run()
