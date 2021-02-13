
class Curve_Print():
        
    ##!
    ##! Prints curve node info.
    ##!
    
    def Curve_Node_Print(self,i):
        print "\ta",self.a,"\tb",self.b,"\tc",self.c
        print "%3d\t%.6f" % (i,self.ts[i])
        if (not self.CalcGeo):
            print "\tr =",self.R[i],"\tr' =",self.dR[i],"\tr'' =",self.d2R[i]
            print "\t|dr| =",self.dR[i].Length(),"\tdet =",self.Determinant[i]
            print "\tt =",self.T[i]," (",self.T[i].Length(),")","\tn =",self.N[i]," (",self.N[i].Length(),")"
        else:
            print "\tr =",self.R[i]
            print "\t|dr| =",self.dR[i].Length(),"\t|r' r''| =",self.Determinant[i],
            print "\tv^2/D =",self.d2R[i].Length2()/self.Determinant[i]
            print "\t\\kappa_2 =",self.Kappa[i],"\t\\rho_2 =",self.Rho[i]
            print "\tC =",self.Evolute_R[i]
            print "\tds =",self.dS[i],"s =",self.S[i]

        
    ##!
    ##! Prints curve nodes info, if Print is on.
    ##!
    
    def Curve_Print(self):
        if (self.Print>0):
            for i in range( len(self.R) ):
                self.Curve_Node_Print(i)
