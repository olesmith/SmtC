from math import *

from Vector import *
from Curve2 import *


class Rolling():

    More_Colors={
        "White": {
            "RCS":                     "Red",
            "Rolling_WCS":             "Black",
            "Rolling_Center":          "Black",
            "Rolling_Circle":          "Green",
            "Rolling_ACS":             "Blue",
            "Rolling_Extended_Vector": "Green",
            "Poop_Circle":             "Red",
         },
        "Black":{
            "RCS":                     "Red",
            "Rolling_WCS":             "White",
            "Rolling_Center":          "White",
            "Rolling_Circle":          "Green",
            "Rolling_ACS":             "Blue",
            "Rolling_Extended_Vector": "Green",
            "Poop_Circle":             "Red",
        },
    }

    #Rolled circle Coord System.
    RCS=False
    #Rolled circle ficed Coord System.
    RWCS=False

    Rolling_Circle=False
    Rolling_Center=False
    Rolling_Extended_Vector=False

    Rolling_R=1.0
   
         
    ##!
    ##! Rolling coord system size
    ##!

    def Curve_Rolling_RCS_Size(self):
        return self.a+self.b

    
    ##!
    ##! Get Rolled normal vector.
    ##!

    def Curve_Rolling_Rolled_Normal(self,n):
        pc=self.Curve_Rolling_Center(n)
        
        e=self.R[n]-pc
        e=e.Normalize(self.Curve_Rolling_RCS_Size())
        
        return e
    
    ##!
    ##! Draw Rolling coord system
    ##!

    def Curve_Rolling_RCS_Draw(self,n,classs,color):
        return self.Canvas().Draw_CS(
            self.Curve_Rolling_Center(n),
            self.Curve_Rolling_Rolled_Normal(n), #*self.Curve_Rolling_RCS_Size(),
            None,
            classs,
            color
        )
        
            
    ##!
    ##! Rolling first ratio.
    ##!

    def Curve_Rolling_a(self):
        return self.a

    ##!
    ##! Rolling second ratio.
    ##!

    def Curve_Rolling_b(self):
        return self.a+self.b

    
    ##!
    ##! Draw the trochoid extension of radius vector, between self.a and self.a+self.b.
    ##!

    def Curve_Rolling_Extended_Vector_Draw(self,n,classs,color):
        pc=self.Curve_Rolling_Center(n)
        ra=self.R[n]-pc
        ra=ra.Normalize()
            
        #p1=pc+ra*self.Curve_Rolling_a()
        #p2=pc+ra*self.Curve_Rolling_b()
        p2=self.R[n]
        self.Canvas().Draw_Vector(pc,p2,classs,color)
         
    ##!
    ##! Radius of rolling circle.
    ##!

    def Rolling_Circle_Radius(self):
        return self.a
    
    ##!
    ##! Draw Trochoid extra curves
    ##!

    def Curve_Rolling_Circle_Draw(self,n):
        n+=self.Curve_Rolling_Skew()
        if ( n>=len(self.ts) ):
            return
        
        #Center of rolling circle
        pc0=self.Curve_Rolling_Center(0)
        pc=self.Curve_Rolling_Center(n)

        rollingcolor="darkgray"
        rollingcolor2="gray"

        svg=[]
        
        #svg=svg+[
        #    self.Canvas().Draw_Circle(pc0,self.a,"Rolling_Fixed")
        #]
        
        if (self.RCS):
            svg=svg+[ self.Curve_Rolling_RCS_Draw(n,"Rolling_CS",rollingcolor) ]
              
        if (self.Rolling_Center):
            svg=svg+[ self.Canvas().Draw_Point(pc,3,"Rolling_Center",rollingcolor) ]
        
        if (self.Rolling_Extended_Vector):
            svg=svg+[ self.Curve_Rolling_Extended_Vector_Draw(n,"Rolling_Vector",rollingcolor2) ]
    
        if (self.Rolling_Circle):
            normal=self.Curve_Rolling_Normal(n)*self.Rolling_Circle_Radius()
                        
            nrolled=self.Curve_Rolling_Rolled_Normal(n) #*self.Rolling_Circle_Radius()
        
            svg=svg+[
                self.Canvas().Draw_Circle_Spans(
                    pc,
                    normal,
                    nrolled.Angle2()-normal.Angle2(),
                    "Roulette_Arc_Rolled",
                    "Roulette_Arc_Unrolled",
                    rollingcolor,
                    rollingcolor2
                )
            ]

        return svg
