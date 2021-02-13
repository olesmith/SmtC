from Vector import Vector


class Polynomium(Vector):

    def __init__(P,Q=[]):
        P.__Alloc__(len(Q))
        for i in range(len(Q)):
            P[i]=1.0*Q[i]
        
    def __add__(v,w):
        
        w=Polynomium(v)
        for i in range(len(v)):
            w[i]+=w[i]
        return w
    
    def __sub__(v,w):
        w=Polynomium(v)
        for i in range(len(v)):
            w[i]-=w[i]
        return w
    
    def __mul__(P,Q):
        PP=Polynomium()
        PP.__Alloc__( len(P)+len(Q)-1 )
        
        for i in range(len(P)):
            for j in range(len(Q)):
                PP[ i+j ]+=P[i]*Q[j]
        return PP
    
    def __str__(P):
        text=""
        for i in range( len(P) ):
            if (abs(P[i])>0.0):
                if (i==0):
                    text+=str(P[i])+"aa"
                else:
                    if (P[i]>0):
                        text+="+"
                    else:
                        text+="-"
                        text+=str(abs(P[i]))+"x"+"bb"
                
                    if (i>1):
                        text+="^"+str(i)+"cc"
        return text

P=Polynomium([1,-2,1])
Q=Polynomium([1,1])

print "P=",P
print "Q=",Q

R=P-Q

print "P+Q=",P+Q
print "P-Q=",P-Q

    
