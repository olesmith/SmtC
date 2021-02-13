from Vector import Vector

class Curve_Draw():

    Evolute=[]
    
    ##!
    ##! Draw World Coord System
    ##!
    
    def Draw_WCS(self,classs="",color=""):
        if (not classs): classs="WCS"
        if (not color): color="black"
        
        return self.Canvas().Draw_CS(
            self.O,
            self.I,
            self.J,
            classs,
            color
            
        )
        
    ##!
    ##! Draw World Coord System
    ##!
    
    def Curve_Draw_Coordinate_System(self,canvas,pmin,pmax,classs="",color=""):
        if (not classs): classs=""
        if (not color): color="black"

        p1=Vector( [0.0, pmin[1]*0.9 ] )
        p2=Vector( [0.0, pmax[1]*0.9 ] )
        
        pp1=Vector( [pmin[0],0] )
        pp2=Vector( [pmax[0],0] )
        
        print "EX",pmin,pmax,p1,p2
        return [
            self.SVG_Vector(
                canvas.P2Pix(p1),
                canvas.P2Pix(p2),
                classs,color
            ),
            self.SVG_Vector(
                canvas.P2Pix(pp1),
                canvas.P2Pix(pp2),
                classs,color
            ),
        ]
        
    ##!
    ##! Draw curve ACS: r(t),t(t),n(t)
    ##!

    def Curve_ACS_Draw(self,classs,n):
        v=self.I+self.J

        #Insertion point
        p=self.Canvas().pmin+v

        return self.Canvas().Draw_CS(
            p,
            self.T[n],
            self.N[n],
            classs,
            "black"
        )

    ##!
    ##! Draw curve point no n. 
    ##!

    def Curve_Point_Draw(self,n,parms={}):
        color=self.Color
        self.Canvas().Draw_Point(
            self.R[n],
            self.Point_Size,
            self.Name+"_Last",
            color,
            parms
        )

    ##!
    ##! Draw the curve.
    ##!
    
    def Draw(self,n):
        self.Draw_Both(n)

        classs="Curve_Last"
        self.Canvas().Draw_Point(
            self.R[n],
            5,
            classs,
            self.Color
        )
        
        text=str(n)+": "+str(self.ts[ n ])
        return self.Canvas().Image_Draw_Text([25,25],text,"IterationText","",10)

    ##!
    ##! Draw oscillating circle
    ##!

    def Curve_Osculating_Circle_Draw(self,n,classs,parms={}):
        color="green"
        self.Canvas().Draw_Circle(
            self.Evolute_R[n],
            abs(self.Rho[n]),
            classs,
            color,
            parms
        )
        
    ##!
    ##! Draw curvature vector
    ##!

    def Curve_Osculating_Vector_Draw(self,n,classs,parms={}):
        color="grey"
        self.Canvas().Draw_Vector(
            self.R[n],
            self.Evolute_R[n],
            classs,
            color,
            parms
        )
        
    ##!
    ##! Draw curve info
    ##!

    def Curve_Info_Draw(self,n):
        if (self.WCS):
            self.Draw_WCS("WCS")

        if (self.ACS):
            self.Curve_ACS_Draw("ACS",n)
       
        if (self.Evolute_Numerical):

            if (self.Osculating_Circle):
                self.Curve_Osculating_Circle_Draw(n,"Curve_Osculating")
       
            if (self.Osculating_Vector):
                self.Curve_Osculating_Vector_Draw(n,"Curve_Osculating_Vector")
       
        if (self.Poop>0):
            poop="icons/poop"+str(self.Poop)+".png"
            canvas.Image_Draw_Image(canvas.P2Pix(self.R[n]),poop)
            
    ##!
    ##! Draw numerically calculated involute
    ##!
    
    def Curve_Involute_Numerical_Draw(self,n=0):
        color="brown"
        self.Involute_R.Draw_Both(
            self.Canvas(),
            color,
            n
        )

        classs="Numerical_Involute_Last"
        self.Canvas().Draw_Point(
            self.Involute_R[n],
            5,
            classs,
            color
        )
        
    ##!
    ##! Draw numerically calculated evolute
    ##!
    
    def Curve_Evolute_Numerical_Draw(self,n=0):
        #Evolute_R: Mesh
        color="orange"
        self.Evolute_R.Draw_Both(
            self.Canvas(),
            color,
            n
        )

        classs="Numerical_Evolute_Last"
        self.Canvas().Draw_Point(
            self.Evolute_R[n],
            5,
            classs,
            color
        )
        
    ##!
    ##! Draw analytical evolute, if given.
    ##!
    
    def Curve_Evolute_Analytical_Draw(self,n,nframe):
        color="red"
        self.Evolute_Analytical.CSS_Class="Analytical_Evolute"
        self.Evolute_Analytical.Color=color
        self.Evolute_Analytical.R.Draw_Both(self.Canvas(),color,n)
        #self.Evolute_Analytical.Curve_Draw(n,nframe)
       
        classs="Analytical_Evolute_Last"
        self.Canvas().Draw_Point(self.Evolute_Analytical.R[n],3,classs,color)

        #if (hasattr(self.Evolute_Analytical,"Curve_Rolling_Circle_Draw")):
        #    svg=self.Evolute_Analytical.Curve_Rolling_Circle_Draw(n)
        #    self.Canvas().Draw_Circle([0.0,0.0],self.Evolute_Analytical.a,"Rolling_Fixed")
        #    self.Canvas().SVG.append(svg)
        
    ##!
    ##! Draw analytical evolute, if given.
    ##!
    
    def Curve_Roulette_Draw(self,n=0):
        color="green"
        self.Roulette.R.CSS_Class="Roulette"
        self.Roulette.R.Draw_Both(
            self.Canvas(),
            color,
            n
        )

        classs="Roulette_Last"
        self.Canvas().Draw_Point(
            self.Roulette.R[n],
            5,
            classs,
            color
        )
        self.Roulette.Curve_Roulette_Circles_Draw(n)
        

    def Draw_Both(self,n):
        name=self.R.Name
        self.R.Name=self.CSS_Class
        self.R.Draw_Both(self.Canvas(),self.Color,n)
        
        self.R.Name=name

    ##!
    ##! Draw iteration no n.
    ##!
    
    def Curve_Draw(self,n,nframe):
        self.Curve_Init(n,nframe)
        N=len(self.ts)-1
        self.Draw(n)

        if (self.Involute_Numerical):
            self.Curve_Involute_Numerical_Draw(n)
    
        if (self.Evolute_Numerical):
            self.Curve_Evolute_Numerical_Draw(n)
    

        if (self.Evolute_Anal):
            self.Curve_Evolute_Analytical_Draw(n,nframe)
            
        self.Curve_Info_Draw(n-1)

        if (self.Roulette):
            self.Curve_Roulette_Draw(n)
            

        res=self.Animation().Iteration_Save(nframe)
        return res

