from math import *
import sys

sys.path.insert(0,'/usr/local/Python')

from Vector import *
from Matrix import *
from Curve2 import *
from Rolling import *
from Args import *



class Quadratic(Curve2):
    #Quadratic form: x^T*A*x+b^T*x=c
    A=[]
    b=[]
    c=1.0

    post="" #for writing the forms

    #Eigenvalues: If A=A^T, both are real
    Lambdas=[]
    
    #Ortogonal Transformation: x'=D*x <=> x=D^T*x
    #ED has the eigenvectors in columns: D=(d0 d1), where
    #A*d0=lambda[0] d10  and   A*d1=lambda[1] d1
    D=Matrix([ [1.0,0.0],[0.0,1.0] ])
    DT=Matrix([ [1.0,0.0],[0.0,1.0] ])

    #Center
    C=Vector([ 0.0,0.0 ])

    Q=None
    
    def __init__(self,A,b,c,post=""):
        self.A=Matrix(A)
        self.b=Vector(b)
        self.c=c
        
        self.post=post
        
        self.Initialize()

    def Initialize(self):
        self.Q=self
        if (self.A[0][1]!=0.0 or self.A[1][0]!=0.0):
            self.Q=self.Quadratic_Diagonalize()
        else:
            self.Lambdas=Vector([ self.A[0][0],self.A[1][1] ])
            self.Q=self
            
    ##!
    ##! Show number
    ##!
    
    def Quadratic_Diagonalize(self):
        self.Lambdas=self.Quadratic_Eigen_Values()
        
        AA=Matrix([
            [ self.Lambdas[0],0.0             ],
            [ 0.0            ,self.Lambdas[1] ],
        ])

        bb=self.DT*self.b
        cc=self.c #+0.25*(    self.Lambdas[0]*bb[0]**2  +  self.Lambdas[1]*bb[1]**2    )
        
        diagonalized=Quadratic(AA,bb,cc,"'")
        self.D=self.Quadratic_Eigen_Vectors()
        self.DT=self.D.Transpose()

        return diagonalized
        
    ##!
    ##! Show number
    ##!
    
    def show(self,c,post=""):
        if (c>0.0):
            return " + %.6f*%s" %(c,post)
        elif (c<0.0):
            return " - %.6f*%s" %(-c,post)

        return ""
            
    ##!
    ##! Print the form
    ##!
    
    def Quadratic_Text(self):
        text="%.6f" % (self.A[0][0])

        text=text+"*x"+self.post+"^2"
        text=text+self.show(self.A[0][1]+self.A[1][0],"x"+self.post+"y"+self.post)
        text=text+self.show(self.A[1][1],"y"+self.post+"^2")
        
        text=text+self.show(self.b[0],"x"+self.post)
        text=text+self.show(self.b[1],"y"+self.post)
        text=text+" = "+str(self.c)

        return text

    ##!
    ##! Print the form
    ##!
    
    def Quadratic_Text2(self):
        text=""
        type=self.Quadratic_Classify()
        if (type==1):
            text=self.Ellipse_Text()

        return text

    ##!
    ##! Print the form
    ##!
    
    def __str__(self):
        text="%.6f" % (self.A[0][0])

        text=text+"*x"+self.post+"^2"
        text=text+self.show(self.A[0][1]+self.A[1][0],"x"+self.post+"y"+self.post)
        text=text+self.show(self.A[1][1],"y"+self.post+"^2")
        
        text=text+self.show(self.b[0],"x"+self.post)
        text=text+self.show(self.b[1],"y"+self.post)
        text=text+" = "+str(self.c)

        text=[self.Quadratic_Text()]
        text=[self.Q.Quadratic_Text()]
        
        text.append( "lambdas="+str(self.Lambdas) )
        text.append( "D="+str(self.D) )
        text.append( "A="+str(self.A) )
        #text.append( self.Quadratic_Classify() )
        return "\n".join(text)
        
    ##!
    ##! Calculates eigenvalues;
    ##!
    
    def Quadratic_Eigen_Values(self):
        return self.A.Eigen_Values()
        
    ##!
    ##! Calculates eigen vectors.
    ##!
    
    def Quadratic_Eigen_Vectors(self):
        return self.A.Eigen_Vectors2()
        self.DT=self.D.Transpose()

    ##!
    ##! Classifies the quadratic form.
    ##!
    
    def Quadratic_Classify(self):
        if ( self.Lambdas.Product()>0.0 ):

            #We have 1 on the RHS, so only sol if Lambdas>0
            if (self.Lambdas[0]>0.0):
                return 1
            else:
                return -1
        elif ( self.Lambdas.Product()<0.0 ):
            return 2
        else:
            return 3
        
    ##!
    ##! Calculates center or vertex
    ##!
    
    def Quadratic_Center(self):
        return self.b*(-0.5)
    
    ##!
    ##! Calculates v^T*A*v+b^T*v
    ##!
    
    def Quadratic_Calc(self,v):
        return v*(self.A*v)+self.b*v-self.c

    ##!
    ##! Generates all points in the quadratic form: splits in to ellipse, hiperbola and parabola cases.
    ##!
    
    def Quadratic_Points(self,d):
        if ( self.Lambdas.Product()>0.0 ):
            #We have 1 on the RHS, so only sol if Lambdas>0
            if (self.Lambdas[0]>0.0):
                print d,"Ellipse"
                return self.Ellipse_Points()
            else:
                print d,"Nothing"
                return Mesh([])
                

        elif ( self.Lambdas.Product()<0.0 ):
            print d,"Hyperbolas"
            return self.Hyperbola_Points()
        else:
            print d,"Parabolas - implement"
            return Mesh([])

        return []
   
    ##!
    ##! Get points old coordinates
    ##!

    def Coordinates_Old(self,p):
        return self.Quadratic_Center()+self.D*p

    
    ##!
    ##! Ellipse center
    ##!
    
    def Ellipse_Calc_Center(self):
        pc=self.b
        for i in range(2):
            pc[i]+=0.5*self.b[i]/self.A[i][i]
            
        return pc

    ##!
    ##! Ellipse Half axis'
    ##!
    
    def Ellipse_Calc_Axis(self):
        c=self.c
        for i in range( len(self.A) ):
            c+=0.25*(self.b[i]**2.0)/self.A[i][i]

        
        return Vector([
            sqrt(c/self.A[0][0]),
            sqrt(c/self.A[1][1]),
        ])

    ##!
    ##! Print the form
    ##!
    
    def Ellipse_Text(self):
        pc=self.Ellipse_Calc_Center()
        a=self.Ellipse_Calc_Axis()

        text=""
        text=text+"(x"+self.post+self.show(-pc[0])+")^2/("+str(a[0])+")^2)+"
        text=text+"(y"+self.post+self.show(-pc[1])+")^2/("+str(a[1])+")^2)"
        text=text+" = "+str(1.0)

        return text

    ##!
    ##! Generate ellipse point.
    ##!

    def Ellipse_Point(self,pc,a,b,t):
        return Vector([
            a*cos(t),
            b*sin(t),
        ])

        return pc+v

    ##!
    ##! Generate ellipse points.
    ##!

    def Ellipse_Points(self):
        dt=2.0*pi/(1.0*(self.NPoints-1))

        pc=self.Ellipse_Calc_Center()
        a=self.Ellipse_Calc_Axis()
        ps=Mesh()
        t=0
        for n in range( self.NPoints ):
            ps.append( self.Ellipse_Point(pc,a[0],a[1],t) )
            t+=dt

        return [ ps ]

    ##!
    ##! Map point: y=A*p+b
    ##!

    def Map_Point(self,p,A,b=[]):
        if (not b): b=Vector([0.0,0.0])

        return A*p+b
    
    ##!
    ##! Map points: y=A*p+b
    ##!

    def Map_Points(self,ps,A,b=[]):
        pps=Mesh([])
        for n in range( len(ps) ):
            pps.append( self.Map_Point(ps[n],A,b) )
            
        return pps
    
    ##!
    ##! Hyperbola center
    ##!
    
    def Hyperbola_Calc_Center(self):
        pc=self.b
        for i in range(2):
            pc[i]+=0.5*self.b[i]/self.A[i][i]
            
        return pc

    ##!
    ##! Hyperbola Half axis'
    ##!
    
    def Hyperbola_Calc_Axis(self):
        c=self.c
        for i in range( len(self.A) ):
            c+=0.25*(self.b[i]**2.0)/self.A[i][i]

        
        return Vector([
            sqrt(c/self.A[0][0]),
            sqrt(c/self.A[1][1]),
        ])

    
    ##!
    ##! Generate hyperbola point.
    ##!

    def Hyperbola_Point(self,a,b,t):
        return Vector([
            a*sqrt(1+t**2.0),
            b*t,
        ])

        return v

    ##!
    ##! Generate  Hyperbola points.
    ##!
    
    def Hyperbola_Points(self):
        pc=self.Hyperbola_Calc_Center()
        a=self.Hyperbola_Calc_Axis()

        
        ps=Mesh()

        a=b=0.0
        A=[]
        if (self.Lambdas[0]>0.0):
            a=sqrt(1.0/self.Lambdas[0])
            b=sqrt(1.0/(-self.Lambdas[1]))
            A=Matrix([
                [ -1.0, 0.0 ],
                [  0.0, 1.0 ],
            ])
        elif (self.Lambdas[1]>0.0):
            a=sqrt(1.0/-self.Lambdas[0])
            b=sqrt(1.0/(self.Lambdas[1]))
            A=Matrix([
                [  1.0, 0.0 ],
                [  0.0,-1.0 ],
            ])
        
        dt=2.0/(1.0*(self.NPoints-1))
        
        t=-1.0
        for n in range( self.NPoints ):
            ps.append( self.Hyperbola_Point(a,b,t) )
            t+=dt
            
        ps1=self.Map_Points(ps,A)

        assymptote1=Mesh("Assimptote1",[ ps[0], ps1[ len(ps1)-1 ] ])
        assymptote2=Mesh("Assimptote2",[ ps1[0],ps[  len(ps) -1 ] ])

        return [ ps,ps1,assymptote1,assymptote2 ]

    ##!
    ##! Generate quadratuic points
    ##!

    def Calc_Points(self,d):
        #First calc points on diagonalized quadratic
        ps=self.Q.Quadratic_Points(d)

        dd=0.0
        for curveno in range( len(ps) ):
            for n in range( len( ps[curveno] ) ):
                #dd=Max(d,abs(self.Quadratic_Calc(ps[curveno][n])))
                ps[curveno][n]=self.Coordinates_Old(ps[curveno][n])
                #dd=Max(d,abs(self.Quadratic_Calc(ps[curveno][n])))

        #print "Curve delta max: ",dd
        return ps
                
        
class Quadratics(Curve2):
    Curves=[]
    Colors=[
        "red","green","blue","yellow","brown",
        "maroon","gold","lightcoral","goldenrod","darksalmon",
        "orange","cyan","magenta","deepblue","grey",
    ]
    
    ##!
    ##! Calculates all curves Min
    ##!
    
    def Curve_Min(self):
        p=Vector(2)
        for rcurves in self.Curves:
            for curve in rcurves:
                if ( len(curve)>0 ):
                    p=p.Min( curve.Min() )

        return p
    
    ##!
    ##! Calculates all curves Max
    ##!
    
    def Curve_Max(self):
        p=Vector(2)
        for rcurves in self.Curves:
            for curve in rcurves:
                if ( len(curve)>0 ):
                    p=p.Max( curve.Max() )

        return p

    
    def Curves_SVG(self,quadratic,canvas,classs,color,curves):
        svg=[]
        for curve in curves:
            if ( len(curve)>0 ):
                parms={
                    "style": {
                        "stroke-width": 1,
                    }
                }
                svg=svg+curve.Mesh_SVGs(canvas,"Curve",color)

        return svg
    
    def Curves_Family_SVG(self,name,outpath,canvas,classs,color1,color2,csvg):
        svgs=[]
        
        d=self.d1
        t=0.0
        n=0
        for curves in self.Curves:
            text="%.6f" % d
            color=self.Color_Convex(t,color1,color2)
            color=self.Colors[ (n % len(self.Colors) ) ]

            
            textsvg=[
                self.SVG_Text([10,15],text,"Curve_Text","black","15px"),
                self.SVG_Text(
                    [10,35],
                    self.Quadratics[n].Quadratic_Text(),
                    "Curve_Text","black","15px"
                ),
                self.SVG_Text(
                    [10,50],
                    self.Quadratics[n].Quadratic_Text2(),
                    "Curve_Text","black","15px"
                ),
            ]
        
            svg=self.Curves_SVG(
                self.Quadratics[n],
                canvas,
                "",
                color,
                curves
            )
            
 
            pmin=self.Curve_Min()
            pmax=self.Curve_Max()
            
            self.SVG_Write(
                canvas,
                [
                    self.Draw_WCS()
                ]+
                svg+csvg+textsvg,
                outpath+text+".svg"
            )
                   
            svgs=svgs+svg
                
            d+=self.dd
            t+=self.dt
            n+=1

        return svgs

    def Run(self):
        self.NPoints=200
        self.Quadratics=[]
        
        self.a=1.0
        self.b=1.0
        
        self.d1=-2.0
        self.d2=2.0
        ncurves=100

        self.dd=(self.d2-self.d1)/(1.0*(ncurves-1))

        self.d=self.d1
        self.Curves=[]
        for n in range(ncurves):
            A=[
                [ 1.0,    self.d ],
                [ self.d, 1.0 ],
            ]

            b=[ 0.0,0.0 ]
            c=1.0

            quadratic=Quadratic(A,b,c)
            quadratic.Q.Quadratic_Classify()

            ps=quadratic.Calc_Points(self.d)
            self.Curves.append( ps )
            self.Quadratics.append( quadratic )

            self.d+=self.dd

        self.Resolution=[800,800]

        pmin=self.Curve_Min()
        pmax=self.Curve_Max()

        canvas=Canvas2(
            {},
            [ pmin,pmax ],
            self.Resolution
        )

        color1=Vector([0,255,20])
        color2=Vector([255,0,0])

        dt=1.0/(1.0*(ncurves-1))
        
        name="curves/Quadratic"
        outpath="/".join([
            name,
            str(self.a),
            str(self.b),
            str(self.c),
            str(self.NPoints),
            ""
        ])
        
        svg=self.Curve_Draw_Coordinate_System(canvas,pmin,pmax)
        svgs=self.Curves_Family_SVG(name,outpath,canvas,"Curve",color1,color2,svg)

        self.SVG_Write(canvas,svgs,name+".svg")

        for quadratic in self.Quadratics:
            print quadratic
            print quadratic.Q

#########Main################
parms={
}
Args_Files_Add(["Curves/Quadratic.inf"])

quadratics=Quadratics()
quadratics.Run()

