from math import *


from Base import *

def Format_Real(t):
    return "%.6f" % t

def htmlvect(v):
    vs=map(Format_Real,v)
    return "(" + ",<BR>".join(vs) + ")"



class Vector(list):

    def __init__(v,w=[]):
        if (w.__class__.__name__=="int"):
            v.__Calloc__(w)
            
        else:
            v.__Calloc__( len(w) )
            for i in range( len(w) ):
                v[i]=1.0*w[i]
        
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

    def __sub__(v,w):
        u=Vector(v)
        for i in range(len(v)):
            u[i]-=w[i]
        
        return u

    def __isub__(v,w):
        return v-w

    def __neg__(v):
        return v*(-1.0)

    def __mul__(v,w):
        if (w.__class__.__name__=="Vector"):
            dot=0.0
            for i in range( len(v) ):
                dot+=v[i]*w[i]
            return dot
        
        if (w.__class__.__name__=="Matrix"):
            u=Vector()
            u.__Alloc__( len(w) )
            
            for i in range( len(w) ):
                u[i]=0.0
                for j in range( len(v) ):
                    u[i]+=w[j][i]*v[j]
            return u
        
        #We should be e number from now on
        if (w.__class__.__name__=="int"):
            w*=1.0
            
        if (w.__class__.__name__=="float"):
            u=Vector(v)
            for i in range( len(v) ):
                u[i]*=w
            return u

        print "Vector.__mul__: Invalid second argument: ",w.__class__.__name__

    def __imul__(v,w):
        return v*w

    def __div__(v,b):
        #We should be e number from now on
        if (b.__class__.__name__=="int"):
            w*=1.0
            
        if (b.__class__.__name__=="float"):
            u=Vector(v)
            for i in range( len(v) ):
                u[i]/=b
            return u

        print "Vector.__div__: Invalid second argument: ",b.__class__.__name__
        
    def __idiv__(v,b):
        return v/b

    def __str__(v):
        vs=map(Format_Real,v)
        return "(" + ",".join(vs) + ")"

    def __html__(v):
        vs=map(Format_Real,v)
        return "(" + ",<BR>".join(vs) + ")"

    def DotProduct(v):
        return v*v
    
    def Length2(v):
        return v.DotProduct()
    
    def Length(v):
        return sqrt( v.Length2() )
    
    def Normalize(v,length=1.0):
        if (v.Length()>0.0):
            v*=length/v.Length()

        return v
    
    def Transverse2(v,length=1.0):
        return Vector([ -length*v[1],length*v[0] ])
                      
    def Determinant2(v,w):
        return v[0]*w[1]-w[0]*v[1]
    
    def Max(v,vv):
        if (len(v)==0): v=Vector( len(vv) )

        for i in range( len(vv) ):
            v[i]=Max(v[i],vv[i])
                
        return v
                
    def Min(v,vv):
        if (len(v)==0): v=Vector( len(vv) )
        
        for i in range( len(vv) ):
            v[i]=Min(v[i],vv[i])
                
        return v
                
    def Rotate2(v,theta):
        return Vector([
            cos(theta)*v[0]-sin(theta)*v[1],
            sin(theta)*v[0]+cos(theta)*v[1],
        ])
    
    def Angle2(v):
        if (v[0]>0.0):
            ang=atan(v[1]/v[0])
        elif (v[0]<0.0):
            if (v[1]>=0.0):
                ang=atan(v[1]/v[0])+pi
            else:
                ang=atan(v[1]/v[0])-pi
        elif (v[0]==0.0):
            if (v[1]>0.0):
                ang=pi/2.0
            else:
                ang=-pi/2.0
        else:
            return None
        
        while (ang<0.0):
            ang+=2.0*pi
            
        return ang
        
    def Radian2(v):
        rad=int( 180.0*v.Angle2()/pi )
        while (rad>360):
            rad-=360
        while (rad<0):
            rad+=360

        return rad

    def Sum(v):
        res=0.0
        for i in range( len(v) ):
            res+=v[i]

        return res

    def Product(v):
        prod=1.0
        for i in range( len(v) ):
            prod*=v[i]

        return prod
    
           
      
def Print(vs):
    for i in range( len(vs) ):
        print i,"\t",vs[i]
        
def Test():
    u=Vector([4,5,6])
    v=Vector([1,2,3])

    u+=v

    d=u
    d*=v
    print d
    print u,"+",v,"=",(u+v)

    w=u,"*",v,"=",u*v
    print u,"*",2,"=",u*2


def Vectors_Max(vs):
    vm=vs[0]
    for i in range( len(vs) ):
        for j in range( len(vs[i]) ):
            vm[ j ]=Max(vm[ j ],vs[ i ][ j ])

    return vm
                
def Vectors_Min(vs):
    vm=vs[0]
    for i in range( len(vs) ):
        for j in range( len(vs[i]) ):
            vm[ j ]=Min(vm[ j ],vs[ i ][ j ])

    return vm
                
def Determinant2(v,w):
    return v.Determinant2(w)
    
def E(t,r=1.0):
    return Vector( [r*math.cos(t),r*math.sin(t)] )

def F(t,r=1.0):
    return Vector( [-r*math.sin(t),r*math.cos(t)] )
    
def Rotate2(v,t):
    return v.Rotate2(t)

def E(t,omega=1.0):
    return Vector([cos(omega*t),sin(omega*t)])

def F(t,omega=1.0):
    return Vector([-sin(omega*t),cos(omega*t)])

def P(t,omega=1.0):
    return Vector([-cos(omega*t),sin(omega*t)])

def Q(t,omega=1.0):
    return Vector([-sin(omega*t),-cos(omega*t)])

