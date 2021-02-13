import time

from Base import *
from Timer import Timer

class Curve_ArcLength():
    Integration_NI=10
    Integration_Type=1 #(1) simpson, (2)
    
    ##!
    ##! If curve length defined with a function name, call it.
    ##! Otherwise, use numerical integration.
    ##!
    
    def S_Calc(self,t,t0=None,n=100):
        if (not t0):
            t0=self.t1
        return self.Calc_dS(t1,t2,n)
        #if (self.S_rc):
        #    method=getattr(self,self.S_rc)
        #    return method(t)
        #else:
        #    return self.Curve_Length(t0,t,n)
        
    ##!
    ##! Find arc lengths for t values in ts.
    ##!
    ##! Type 1: Trapezoids
    ##! Type 2: Simpsons
    ##!

    def Curve_Lengths_Calc(self,ts=[]):
        if (len(ts)==0):
            ts=self.ts
            
        t1=ts[0]
        ss=[0.0]
        dss=[0.0]
        s=0.0
    
        timer=Timer("Calculating "+str(len(ts))+" Arclengths:")
        
        for i in range(1, len(ts) ):
            t1=ts[i-1]
            t2=ts[i]

            ds=self.Curve_Length(t1,t2,self.Integration_NI)
            s+=ds

            ss.append(s)
            dss.append(ds)

        self.dS=dss        
        self.S=ss

        return s
        
    ##!
    ##! Return n nearest t value
    ##!

    def T2n(self,t):
        n=0
        for i in range( len(self.ts) ):
            if (t>=self.ts[i]):
                n=i
                if (n>=len(self.ts)-1) : n=len(self.ts)-1
        return n


    ##!
    ##! Find arc length. We suppose reparametrization has taken place.
    ##!

    def Curve_Length(self,t1,t2,n=100):
        return self.Trapezoids(t1,t2,n)


    def Trapezoid(self,t1,t2):
        f1=self.dr(t1).Length()
        f2=self.dr(t2).Length()
        
        return 0.5*(t2-t1)*(f2+f1)
    
    def Trapezoids_Naive(self,t1,t2,n=100):
        dt=(t2-t1)/(1.0*(n-1))

        t=t1        
        trapez=0.5*self.dr(t1).Length()
        for i in range(n-1):
            trapez+=self.dr(t).Length()
            t+=dt
            
        trapez=0.5*self.dr(t2).Length()
            
        return trapez*dt
    
    def Trapezoids(self,t1,t2,n=100):
        dt=(t2-t1)/(1.0*(n-1))

        trapez=0.0
        t=t1
        for i in range(n):
            trapez+=self.Trapezoid(t1,t1+dt)
            t+=dt
            
        return trapez
    
    def Simpson(self,t1,t2):
        h3=(t2-t1)/3.0
        f1=self.dr( t1          ).Length()
        f2=self.dr( 0.5*(t1+t2) ).Length()
        f3=self.dr( t2          ).Length()
        
        return h3*( f1+4.0*f2+f3 )
    
    def Simpsons(self,t1,t2,n=100):
        dt=(t2-t1)/(1.0*(n-1))

        t1=0.0
        t2=dt

        simpson=0.0
        for i in range(n):
            simpson+=self.Simpson(t1,t2)
            t1+=dt
            t2+=dt
             
        return simpson
    
    ##!
    ##! Calculate Curve (arc) lengths for a large number of curve points a
    ##! reparemetrize by the arclength.
    ##!
    
    def Reparameterize(self,nn=100):
        nn*=self.NPoints
        ts=Intervals(self.t1,self.t2,nn)
        dt=(self.t2-self.t1)/(1.0*len(ts))
        t=self.t1

        #self.Calc_dSs(ts)
        #s=self.Calc_Ss(ts)

        self.ts=ts
        s=self.Curve_Lengths_Calc()

        ds=s/(1.0*(self.NPoints-1))
        print "Curve Length: ",s,self.NPoints," intervals",s,ds
        
        if (self.Verbose>2):
            print "i\tj\ts_{j-1}\t\ts\t\ts_j"
            
        s=0.0
        rts=[self.t1]
        ss=[]
        for i in range( self.NPoints ):
            j=t2Interval(self.S,s)

            if (j>=0):
                eta=(s-self.S[j-1])/(self.S[j]-self.S[j-1])
                
                t=Convex( ts[j-1], ts[j], eta)
                if (self.Verbose>2):
                    print i,"\t",j,"\t",self.S[j-1],"\t",s,"\t",self.S[j]

                rts.append( t )
            s+=ds
            ss.append( s )
            
        rts.append(self.t2)
        ss.append(s)

        self.ts=rts
        #self.S=ss

        self.Integration_NI=1000
        self.Curve_Lengths_Calc()

        return rts

