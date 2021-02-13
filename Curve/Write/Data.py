#from Vector import *

class Curve_Write_Data():
    ##! 
    ##! Write curve datas to files.
    ##!
    
    def Curve_Write_Datas(self,path):
        self.Curve_Write_Data_R(path)
        self.Curve_Write_Data_dR(path)
        self.Curve_Write_Data_d2R(path)
        
        self.Curve_Write_Data_T(path)
        self.Curve_Write_Data_N(path)
        
        if (self.Evolute_Numerical):
            self.Curve_Write_Data_Evolute_Numerical(path)

        if (self.Evolute_Anal):
            self.Curve_Write_Data_Evolute_Analytical(path)
            
        if (self.Roulette):
            self.Curve_Write_Data_Roulette(path)

    ##! 
    ##! Write curve R to file.
    ##!
    
    def Curve_Write_Data_R(self,path,file="R.txt"):
        self.R.Mesh_Write_Nodes( "/".join( [ path,file ] ) )

    ##! 
    ##! Write curve dR to file.
    ##!
    
    def Curve_Write_Data_dR(self,path,file="dR.txt"):
        self.dR.Mesh_Write_Nodes( "/".join( [ path,file ] ) )

    ##! 
    ##! Write curve d2R to file.
    ##!
    
    def Curve_Write_Data_d2R(self,path,file="d2R.txt"):
        self.d2R.Mesh_Write_Nodes( "/".join( [ path,file ] ) )


    
    ##! 
    ##! Write curve T to file.
    ##!
    
    def Curve_Write_Data_T(self,path,file="T.txt"):
        self.T.Mesh_Write_Nodes( "/".join( [ path,file ] ) )

    
    ##! 
    ##! Write curve N to file.
    ##!
    
    def Curve_Write_Data_N(self,path,file="N.txt"):
        self.N.Mesh_Write_Nodes( "/".join( [ path,file ] ) )

    ##! 
    ##! Write curve Numerical Evolute to file.
    ##!
    
    def Curve_Write_Data_Evolute_Numerical(self,path,file="C_EN.txt"):
        self.Evolute_R.Mesh_Write_Nodes( "/".join( [ path,file ] ) )

    ##! 
    ##! Write curve Analytical Evolute to file.
    ##!
    
    def Curve_Write_Data_Evolute_Analytical(self,path,file="C_EA.txt"):
        self.Evolute_Analytical.R.Mesh_Write_Nodes( "/".join( [ path,file ] ) )
    ##! 
    ##! Write curve Roulette to file.
    ##!
    
    def Curve_Write_Data_Roulette(self,path,file="C_R.txt"):
        self.Roulette.R.Mesh_Write_Nodes( "/".join( [ path,file ] ) )

