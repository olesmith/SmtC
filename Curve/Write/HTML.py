from Vector import *

class Curve_Write_HTML():
    ##! 
    ##! Curve info HTML file name
    ##!
    
    def Curve_Write_HTML_FileName(self,path):
        return "/".join( [path,"Geometry.html"] )
    
        
    ##!
    ##! Prints curve node info.
    ##!
    
    def Curve_Write_HTML_Node_Row(self,i):
        if (   i>=len(self.R)   ): return []
        
        n=self.B(str(i))
        row=[ n,str(self.ts[i]) ]
        if (self.CalcGeo):
            row.append(htmlvect(self.R[i]))
            row.append(htmlvect(self.d2R[i]))
            row.append(htmlvect(self.dR[i]))
            
            row.append(str(self.dR[i].Length()))
            row.append(str(self.d2R[i].Length()))
            
            row.append(htmlvect(self.T[i]))
            row.append(htmlvect(self.N[i]))

            row.append(n)
            row.append(str(self.ts[i]))
            if (i<len(self.dS)):
                row.append(str(self.dS[i]))
                row.append(str(self.S[i]))
            row.append(str(self.Determinant[i]))
            row.append(str(self.Kappa[i]))
            row.append(str(self.Rho[i]))
            row.append(str(self.Phi[i]))
            
        if (self.Evolute_Numerical or self.Evolute_Anal or self.Roulette):
            row.append(n)
            row.append(str(self.ts[i]))
            
        if (self.Evolute_Numerical):
            row.append(htmlvect(self.Evolute_R[i]))
            
        if (self.Evolute_Anal):
            row.append(htmlvect(self.Evolute_Analytical.R[i]))
            
        if (self.Roulette):
            row.append(htmlvect(self.Roulette.R[i]))
           
        return row
    
    def Curve_Write_HTML_Node_Titles(self):
        row=[
            "n","t",
            "r(t)","r'(t)","r''(t)",
            "v(t)","a(t)",
            "t(t)","n(t)",
            "n","t",
            "ds","s(t)",
            "D(t)=[r' x r'']",
            "&kappa;(t)","&rho;(t)",
            "&phi;(t)=v(t)^2/D(t)",
            "n","t",
        ]
        
        if (self.Evolute_Numerical):
            row.append("c_n(t)")
            
        if (self.Evolute_Anal):
            row.append("c_a(t)")
            
        if (self.Roulette):
            row.append("Rou(t)")
            
        return row
    
    ##!
    ##! Generate Nodes table as matrix
    ##!
    
    def Curve_Write_HTML_Nodes_Table(self):
        table=[]
        for i in range(1,len(self.ts) ):
            table.append( self.Curve_Write_HTML_Node_Row(i) )

        return table
    
    ##!
    ##! Generate curve nodes html table.
    ##!
    
    def Curve_Write_HTML_Nodes(self):
        return self.HTML_Table(
            self.Curve_Write_HTML_Nodes_Table(),
            self.Curve_Write_HTML_Node_Titles(),
            [],
            {
                "border": 1,
                "repeat": 10,
            }
        )
