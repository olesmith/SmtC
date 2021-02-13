
class Curve_Connections():
    ##!
    ##! Generate connections necessary to draw a curve.
    ##!
    
    def Curve_Connections(self,n=0,closed=False):
        conns=[]
        for i in range(1, n ):
            conns.append( [i-1,i] )

        if (closed>0):
            conns.append( [ n-1 ,0] )
        return conns
    
