from math import *


from Vector import Vector
from Matrix import *
#Quadratic form:
#    v^T A v+b^T v=c

class Quadratic(list):
    def __init__(self,A=None,b=None,c=None):
        I=I( len(A) )
        
        if (not A): self.A=Matrix(I)
        if (not b): self.b=[0.0,0.0]
        if (not c): self.c=1.0

        #We assume symmetry!
        self.A[0][1]=0.5*(self.A[0][1]+self.A[1][0])
        self.A[1][0]=self.A[0][1]
        
        #Orthogonal matrix, I if already diagonal
        self.D=Matrix(I)
        
        if (self.A[0][1]*self.A[1][0]!=0.0):
            self.Lambdas=A.Eigen_Values()
            self.D=A.Eigen_Vectors
        else:
            for i in range( len(A) ):
             self.Lambdas[i]=A[i][i]
    
       self.DT=self.D.Transpose()

       #Diagonal matrix
       self.A=Diagonal(self.Lambdas)

       #Map affin part
       self.b=self.DT*b

       #Center or vertex or..
       # lambda*x^2+b*x=lambda( (x- 1/2 b/lambda)^2 - 1/4 b^2/lambda
       self.C=b
       for i in range(2):
           if (self.Lambdas[i]!=0.0):
               self.C[i]-=0.5*self.b[i]/self.Lambdas[i]
        
        #Add 1/4 b^2/lambda on RHS
        for i in range( len(self.A) ):
            self.c+=0.25*(self.b[i]**2.0)/self.Lambdas[i]

        #If RHS is negative, multiply c and lambdas by -1
        if (self.c<0.0):
            self.Lambdas=self.Lambdas(_1.0)
            self.c=-self.c


    #Classification:
    #
    #   1: Ellipsis
    #   2: Hyperbola
    #   3: Parabola
    #   4: Two lines
    #   5: One line (A 0 matrix)
    #   6: One point
    #   7: Nothing
    
    def Quadratic_Classify():
        res=0
        product=self.Lambdas.Product()
        if (product>0.0):
            if (self.c>0.0):    res=1 #ellipse
            elif (self.c==0.0): res=6 #point
            else:               res=7 #nothing
        elif (product<0.0):
            if (self.c==0.0): res=4 #two lines, the assymptotes
            else:             res=2 #hyperbola
        elif (product==0.0):
            res=3 #parabola

        self.Type=res
        return res

    ##!
    ##! Half axis'
    ##!
    
    def Quadratic_Axis(self):
        v=Vector()
        for i in range( len() ):
            v.append(      sqrt(   abs( self.c/self.Lambdas[i])  )      )
        return v
        
    def Quadratic_Generate_Ellipse(n):
        dt=2.0*pi/(1.0*(n-1))

        a=self.Quadratic_Axis()
  
        ps=Mesh()
        t=0
        for n in range( self.NPoints ):
            p=Vector([ a[0]*cos(t),a[1]*sin(t) ])
            ps.append( self.C+p )
            t+=dt

        return [ ps ]
        
    ##!
    ##! Map points: y=A*p+b
    ##!

    def Map_Points(self,ps,A,b=[]):
        pps=Mesh([])
        for n in range( len(ps) ):
            pps.append( self.Map_Point(ps[n],A,b) )
            
        return pps
    
    def Quadratic_Generate_Hyperbola(np,t=3.0):
        dt=2.0*t/(1.0*(np-1))

        a=self.Quadratic_Axis()
  
        ps=Mesh()
        t=-t
        for n in range( self.NPoints ):
            p=Vector([
                a[0]*sqrt(1+t**2.0),
                a[1]*t,
            ])
            
            ps.append( self.C+p )
            t+=dt

        S=[]
        if (self.Lambdas[0]>0.0):
            S=Matrix([
                [ -1.0, 0.0 ],
                [  0.0, 1.0 ],
            ])
        elif (self.Lambdas[1]>0.0):
            S=Matrix([
                [  1.0, 0.0 ],
                [  0.0,-1.0 ],
            ])

        pss=self.Map_Points(ps,A)
        assymptote1=Mesh("Assimptote1",[ ps[0], ps1[ len(ps1)-1 ] ])
        assymptote2=Mesh("Assimptote2",[ ps1[0],ps[  len(ps) -1 ] ])
        
        return [ ps,pss,assymptote1,assymptote2 ]
    
    def Quadratic_Generate_Points_New(n):
        pss=Mesh()
        if (self.Type==1):
            pss=self.Quadratic_Generate_Ellipse(n)
        elif (self.Type==2):
            pss=self.Quadratic_Generate_Hyperbola(n)
            
        
