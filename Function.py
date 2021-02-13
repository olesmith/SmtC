def ff(t):
    return t*t

class Function():

    func=""
    eps=0
    eps2inv=0
    
    def __init__(self,sf,eps=1.0E-3):
        self.func=sf
        
        self.eps=eps
        self.eps2inv=1.0/(2.0*self.eps)
        
    def f(self,t):
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(self.func)

        return method(t)

    def df(self,t):
        return (self.f(t+self.eps)-self.f(t-self.eps))*self.eps2inv

    def d2f(self,t):
        return (self.df(t+self.eps)-self.df(t-self.eps))*self.eps2inv

    def fs(self,t1,t2,n=100):
        ps=[]
        
        dt=(t2-t1)/(1.0*n)
        t=t1
        for i in range(n+1):
            ps.append( [t,self.f(t)] )
            t+=dt
        return ps

    def dfs(self,t1,t2,n=100):
        ps=[]
        
        dt=(t2-t1)/(1.0*n)
        t=t1
        for i in range(n+1):
            ps.append( [t,self.df(t)] )
            t+=dt
        return ps

    def d2fs(self,t1,t2,n=100):
        ps=[]
        
        dt=(t2-t1)/(1.0*n)
        t=t1
        for i in range(n+1):
            ps.append( [t,self.d2f(t)] )
            t+=dt
        return ps

    def Calc(self,t1,t2,n=100):
        ps=[[],[],[]]
        
        dt=(t2-t1)/(1.0*n)
        t=t1
        for i in range(n+1):
            ps[0].append( [t,self.f(t)] )
            ps[1].append( [t,self.df(t)] )
            ps[2].append( [t,self.d2f(t)] )
            t+=dt
        return ps

func=Function("ff")

print func.Calc(0,2)

