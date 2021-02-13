import re,math

def Format_Real(t):
    return "%.6f" % t

class Polynomial(list):
    Roots=[]
    Order=0
    
    def __init__(P,Q=[]):
        if (Q.__class__.__name__=="int"):
            P.__Calloc__(Q)
            
        else:
            P.__Calloc__( len(Q) )
            for i in range( len(Q) ):
                P[i]=1.0*Q[i]

        P.Order=len(P)-1
        P.Roots_Calc()
        #P.Roots_Test()
        
        
    def __Calloc__(v,size):
        for i in range(size):
            v.append(0.0)
        
    def __add__(v,w):
        
        u=Vector(v)
        for i in range(len(v)):
            u[i]+=w[i]
        return u

    def __iadd__(v,w):
        return v+w

    def __mul__(v,w):
        u=Polynomial( len(v)*len(w) )
        return u

                      
    def __str__(P):
        text=""
        for i in ( len(P) ):
            pi=P[i]
            itext=str(P[i])
            if (pi>0.0):
                itext="+"+itext
            if (i>0):
                itext=""+"x^"+i
                
                
            text=text+itext
                
        return "(" + ",".join(ps) + ")"+"\t(" + ",".join(roots) + ")"

    def Roots_Calc(P):
        if (P.Order==1):
            if (P[1]!=0.0):
                P.Roots=[ -P[0]/P[1] ]
        
        elif (P.Order==2):
            if (P[2]!=0.0):
                delta=P[1]*P[1]-4.0*P[0]*P[2]
                if (delta>=0.0):
                    delta=math.sqrt(delta)
                    
                P.Roots=[
                    (-P[1]+delta)/(2.0*P[2]),
                    (-P[1]-delta)/(2.0*P[2]),
                ]
        
                
    def Roots_Test(P):
        if ( len(P.Roots) )>0:
            pol=Polynomial([1.0])
            for root in P.Roots:
                poli=Polynomial([-root,1.0])
                p=p*poli
            print poli

pol=Polynomial([1,2,1])
print pol
