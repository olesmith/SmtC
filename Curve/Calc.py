from math import *


from Base import *
from Mesh import *
from Main import *

from Oids import *

class Curve_Calc():

    ##!
    ##! Call coordinate generating function, parameter t.
    ##! Name in slef.rc; should return a list of numbers.
    ##!
    
    def r(self,t):
        method=None
        if ( hasattr(self,self.rc) ):
            method=getattr(self,self.rc)
        else:
            parent=self.Parent
            if ( hasattr(parent,self.rc) ):
                method=getattr(parent,self.rc)
 
        v=[0.0,0.0]
        if (method):
            v=method(t)
        else:
            print "Warning! No method!!!",method,self.rc,self.Name
            
        return Vector(v)

    ##!
    ##! Calculate derivative, calling self.r.
    ##!
    
    def dr(self,t):
        v=self.r(t+self.eps)-self.r(t-self.eps)
        return v*self.eps2inv

    ##!
    ##! Calculate second derivative, calling self.dr.
    ##!
    
    def d2r(self,t):
        v=self.dr(t+self.eps)-self.dr(t-self.eps)
        return v*self.eps2inv

    ##!
    ##! Calc Max point
    ##!
    
    def Max(self):
        return self.R.Max()
         
    ##!
    ##! Calc Min point
    ##!
    
    def Min(self):
        return self.R.Min()
         

    ##!
    ##! Calculate derivative, calling self.r.
    ##!
    
    ##!
    ##! Generate sequence of n equidistant t-values.
    ##!
    
    def Calc_ts(self,n=0):
        if (n==0):
            n=self.NPoints
        
        self.ts=[]
        t=self.t1
        self.dt=(self.t2-self.t1)/(1.0*(n-1))
        
        for i in range(n):
            self.ts.append( t )
            t+=self.dt

        return self.ts

    ##!
    ##! Returns stored t-values.
    ##!
    
    def Get_ts(self,ts):
        if ( len(ts)==0 ):
            ts=self.Calc_ts()
            
        return ts
    
    ##!
    ##! Calculate and store self.r(t) Vectors.
    ##!
    
    def Calc_Rs(self,ts=[]):
        ts=self.Get_ts(ts)
            
        self.R=Mesh(self.Name, len(ts) )
        self.R.Point_Size=self.Point_Size
        for i in range( len(ts)):
             self.R[i]=self.r(ts[i])
             
        return self.R


    ##!
    ##! Calculate and store self.r(t) derivatives.
    ##!
    
    def Calc_dRs(self,ts=[]):
        ts=self.Get_ts(ts)
        self.dR=Mesh("dR", len(ts) )
        for i in range( len(ts )):
            self.dR[i]=self.dr(ts[i])
            
        return self.dR
     
    ##!
    ##! Calculate and store self.r(t) second order derivatives.
    ##!
    
    def Calc_d2Rs(self,ts=[]):
        ts=self.Get_ts(ts)
        
        self.d2R=Mesh("d2R", len(ts) )
        for i in range( len(ts )):
            self.d2R[i]=self.d2r(ts[i])
            
        return self.d2R

    ##!
    ##! Calculate and store self.r(t) unit tangent vectors: r'/|r'|.
    ##!
    
    def Calc_Ts(self):
        self.T=Mesh("Ts", len(self.R) )
        for i in range( len(self.R) ):
            self.T[i]=self.dR[ i ].Normalize()
            
        return self.T

    ##!
    ##! Calculate and store self.r(t) unit normal vectors: n=\widehat{t}
    ##!
    
    def Calc_Ns(self):
        self.N=Mesh("Ns", len(self.R) )
        for i in range( len(self.R) ):
            self.N[i]=self.T[ i ].Transverse2()
            
        return self.N

    ##!
    ##! Calculate length if r', dS.
    ##!
    
    def Calc_dS(self,t1,t2,nintervals=10):
        if (self.S_rc):
            method=None
            if ( hasattr(self,self.S_rc) ):
                method=getattr(self,self.S_rc)

                return method(t2)- method(t1)
            else:
                print "No Arclength method, ",self.S_rc
        elif (self.Integration_Method==1):
            return self.Trapezoids(t1,t2,nintervals)
        elif (self.Integration_Method==2):
            return self.Simpsons(t1,t2,nintervals)
        


    ##!
    ##! Calculate and store incremental curvelengths
    ##!
    
    def Calc_dSs(self,ts):
        self.dS=Vector( len(ts) )
        for i in range(len(ts)-1 ):
            self.dS[i]=self.Calc_dS(ts[i],ts[i+1])
            
        return self.dS


    ##!
    ##! Calculate and store accumulated curvelengths
    ##!
    
    def Calc_Ss(self):
        self.S=Vector( len(self.dS)+1 )
        s=0.0
        self.S[0]=0.0
        for i in range( len(self.dS) ):
            s+=self.dS[i]
            self.S[i+1]=s

        if (self.S_rc):
            method=None
            if ( hasattr(self,self.S_rc) ):
                method=getattr(self,self.S_rc)

                print "Curvelength",s,(method(self.t2)- method(self.t1))
        else:
            print "Curvelength",s

        return s

    ##!
    ##! Calculate and store derivatives determinant: [r' r'']
    ##!
    
    def Calc_Determinants(self):
        self.Determinant=Vector( len(self.R) )
        for i in range( len( self.R ) ):
            self.Determinant[i]=Determinant2(self.dR[ i ],self.d2R[ i ])
            
        return self.Determinant

    ##!
    ##! Calculate and store phi(t): v(t)^2/D(t)
    ##!
    
    def Calc_Phis(self):
        self.Phi=Vector( len(self.R) )
        for i in range( len( self.R ) ):
            self.Phi[i]=0.0
            len2=self.dR[i].Length2()
            if (len2>0.0):
                self.Phi[i]=self.Determinant[i]/len2
            
        return self.Phi

    ##!
    ##! Calculate and store curvatures.
    ##!
    
    def Calc_Kappas(self):
        self.Kappa=Vector( len(self.R) )
        
        for i in range( len(self.R) ):
            kappa=0.0
            length=self.dR[ i ].Length()
            if (length>0.0):
                kappa=Determinant2(self.dR[ i ],self.d2R[ i ])
                kappa/=length**3.0
            self.Kappa[i]=kappa

        return self.Kappa
            
    ##!
    ##! Calculate and store curvature ratios.
    ##!
    
    def Calc_Rhos(self):
        self.Rho=Vector( len(self.R) )
        for i in range( len( self.R ) ):
            kappa=self.Kappa[i]
            rho=0.0
            if (kappa!=0.0):
                    rho=1.0/kappa
                    
            self.Rho[i]=rho
            
        return self.Rho
            
            
    ##!
    ##! Calculate and store curvature ratios.
    ##!
    
    def Calc_Evolute(self):
        self.Evolute_R=Mesh("Numerical_Evolute", len(self.Kappa) )
        for i in range( len( self.R ) ):
            self.Evolute_R[i]= self.R[i]+self.N[i]*self.Rho[i]

        return self.Evolute_R
    
    ##!
    ##! Calculate and store curvature ratios.
    ##!
    
    def Calc_Involute(self):
        self.Involute_R=Mesh("Numerical_Involute", len(self.S) )
        for i in range( len( self.R ) ):
            self.Involute_R[i]= self.R[i]+self.T[i]*self.S[i]

        return self.Involute_R
    
    ##!
    ##! Compares evolutes.
    ##!
    
    def Calc_Evolutes_Compare(self):
        diff=0.0
        for n in range( len(self.Evolute_R) ):
            v=self.Evolute_R[n]-self.Evolute_Analytical.R[n]
            diff+=v.Length()

        n=len(self.Evolute_R)
        print "Evolute Compare:",str(n),str(diff),str(diff/(1.0*n))
        
    ##!
    ##! Calculate Curve points - and details if asked for.
    ##! Optionally Reparameterize as well.
    ##!
    
    def Calc(self,ts=None,write=True,meshes=[]):
        if (not ts):
            self.ts=Intervals(self.t1,self.t2,self.NPoints)
        else:
            self.ts=ts

        self.Calc_Rs(self.ts)
        self.dim=len(self.R[0])
        
        #if (self.Reparametrization):
        #    self.ts=self.Reparameterize()
        #else:
        #    self.Calc_dS(self.ts)
            

        if (self.CalcGeo):
            self.Calc_dRs(self.ts)
            self.Calc_d2Rs(self.ts)
            self.Calc_Ts()
            self.Calc_Ns()
            
            self.Calc_Determinants()
            self.Calc_Phis()
            self.Calc_Kappas()
            self.Calc_Rhos()
        
        if (self.Curve_Lengths):
            self.Calc_dSs(self.ts)
            self.Calc_Ss()
           
        if (self.Involute_Numerical):
            self.Calc_Involute()
            
        if (self.Evolute_Numerical):
            self.Calc_Evolute()
            
        if (self.Evolute_Anal):
            self.Calc_Evolute_Analytical()

        #Compare numerical and analytical evolutes!
        if (self.Evolute_Numerical and self.Evolute_Anal):
            self.Calc_Evolutes_Compare()
            
        if (self.Roulette):
            mtime=int(time.time())
            print "Calc Roulette",self.Roulette_A,self.Roulette_B
            self.Calc_Roulette()
            print "Done, calc Roulette",int(time.time())-mtime," secs"

           
        if (not self.Parent and write):
            self.Curve_SVG_Write(meshes)
