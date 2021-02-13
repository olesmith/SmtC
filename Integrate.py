
#Watch number of function calls

global NFunctionCalls
NFunctionCalls=0



## Simple Trapezoid

def Trapezoid(f,t1,t2,h):
    global NFunctionCalls
    NFunctionCalls+=2
    
    return h*(f(t2)+f(t1))

## Divide in [t1,t2] em n intervals and sum Trapezoid for each one.

def Trapezoids(f,t1,t2,n=100):
    dt=(t2-t1)/(1.0*(n-1))

    h=dt*0.5
    trapez=0.0
    t=t1
    for i in range(n):
        dtrapez=Trapezoid(f,t,t+dt,h)
        trapez+=dtrapez
        t+=dt

    return trapez
    
## Divide in [t1,t2] em n intervals and calc Repeated Trapezoids: Optimized version

def Trapezoids_Repeated(f,t1,t2,n=100):
    dt=(t2-t1)/(1.0*(n-1))
    h=0.5*dt
    global NFunctionCalls
    
    trapez=f(t1)
    NFunctionCalls+=1
    
    t=t1
    for i in range(n-2):
        dtrapez=2.0*f(t+dt)
        trapez+=dtrapez
        t+=dt
        NFunctionCalls+=1
        
    trapez+=f(t2)
    NFunctionCalls+=1

    return h*trapez
    
## Simple Simpson

def Simpson(f,t1,t2,t3,h):
    global NFunctionCalls
    NFunctionCalls+=3
    
    simp=f(t1)+4.0*f(t2)+f(t3)
    
    return simp*h
    
## Divide in [t1,t2] em n intervals and sum Simpson for each one.

def Simpsons(f,t1,t2,n=100):
    dt=(t2-t1)/(1.0*(n-1))
    h=dt/6.0
    
    simpson=0.0

    t=t1
    for i in range(n):
        simpson+=Simpson(f,t,t+0.5*dt,t+dt,h)
        t+=dt
            
    return simpson


## Divide in [t1,t2] em n intervals and calc Repeated Simpson: Optimized version

def Simpsons_Repeated(f,t1,t2,n=100):
    global NFunctionCalls

    dt=(t2-t1)/(1.0*(n-1))
    h=dt/6.0
    
    simpson=0.0
    
    simpson+=1.0*f(t1)
    NFunctionCalls+=1
    
    t=t1
    for i in range(n-1):
        
        #odd
        dsimpson1=4.0*f(t+h)
        simpson+=dsimpson1
        NFunctionCalls+=1
         
        #even
        dsimpson2=2.0*f(t+2.0*h)
        simpson+=dsimpson2
        NFunctionCalls+=1
        

        t+=dt

    simpson+=1.0*f(t2)
    NFunctionCalls+=1
    
    return h*simpson
    

def f1(x):
    return x*x*x

x1=1.0
x2=2.0
anal=(x2**4.0-x1**4.0)/4.0


print "************ Trapezoids %.6f ************" % (anal)

print "N\tSum\t\tRel err(%)\tNF\t\tRepated\t\tResidue(%)\tNF"

for n in range(1,11):
    N=100*n
    
    NFunctionCalls=0
    trapez1=Trapezoids(f1,x1,x2,N)
    nf1=NFunctionCalls
    
    NFunctionCalls=0
    trapez2=Trapezoids_Repeated(f1,x1,x2,N)
    nf2=NFunctionCalls
    NFunctionCalls=0

    r1 =100.0*(trapez1-anal)/anal
    r2 =100.0*(trapez2-anal)/anal

    print "%d\t%.6f\t%.6f\t%d\t\t%.6f\t%.6f\t%d" % (n,trapez1,r1,nf1,trapez2,r2,nf2)


print "************ Simpson 1/3 %.6f ************" % (anal)

print "N\tSum\t\tRel err(%)\tNF\t\tRepated\t\tResidue(%)\tNF"


for n in range(1,11):
    N=100*n
    
    NFunctionCalls=0
    simpsons1=Simpsons(f1,x1,x2,N)
    nf1=NFunctionCalls

    NFunctionCalls=0
    simpsons2=Simpsons_Repeated(f1,x1,x2,N)
    nf2=NFunctionCalls

    r1 =100.0*(simpsons1-anal)/anal
    r2 =100.0*(simpsons2-anal)/anal

    print "%d\t%.6f\t%.6f\t%d\t\t%.6f\t%.6f\t%d" % (n,simpsons1,r1,nf1,simpsons2,r2,nf2)


