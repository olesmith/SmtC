

class Curve_Parms():
    
    def Curve_Parms_Paths(self):
        return  [str(self.a),str(self.b),str(self.c),str(self.NFrames)]
    
    def Curve_Parms_Path(self):
        return "/".join( self.Curve_Parms_Paths() )

    def Curve_Parms_FileName(self,cname,fname,ext="svg"):
        fnames=self.Curve_Parms_Paths()
        n=fnames.pop()

        paths=[self.BasePath,self.Name]
        fnames=[ fname,]+fnames+[ n+"."+ext ]
        
        fname="-".join(fnames)
        paths.append(  "-".join(fnames)  )

        return "/".join(paths)
        

    
