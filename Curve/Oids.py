from math import *

from Vector import *

def Sign(t):
    if (t>0.0):
        return 1.0
    elif (t<0.0):
        return -1.0

    return 0.0

class Curve_Oids():

    ##!
    ##! Cycloid: Rolling start point
    ##!
    
    def Trochoid_R0(self,t):
        return Vector([
            self.r0[0]+self.a*t,
            self.r0[1]+self.a
        ])
    

   
    ##!
    ##! Trochoid: Rolling a circle (r=a) on a line. Poop size: b.
    ##!

    def Trochoid_Calc(self,t):
        tt=(t-self.phi)
        r0=self.Trochoid_R0(t)
                
        return [
            r0[0]-(self.a+self.b)*sin(tt),
            r0[1]-(self.a+self.b)*cos(tt)
        ]

    ##!
    ##! The trochoid evolute
    ##!

    def Trochoid_Evolute_Calc(self,t):

        a=self.a
        b=self.b+a

        r0=self.Trochoid_R0(t)
        tt=t-self.phi
        cos1=a-b*cos(tt)
        cos2=b-a*cos(tt)

        fact=0.0
        if (abs(cos2)>0.0):
            fact=-a/b*cos1/cos2
                                                   
        return [
            a*t-fact*b*sin(tt),
            a*fact-fact*b*cos(tt)
        ]

    
