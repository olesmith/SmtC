class Animation_Iteration():

    def Iteration_FileName(self,n):
        path="/".join( [self.FileName,self.Curve_Parms_Path,self.Name] )
        
        return path+"-"+("%06d" % n)
 
    def Iteration_Init(self,n,p1,p2):
        self.Canvas().HTML_Root=self.HTML_Root
        self.Canvas().Name=self.FileName
        self.Canvas().Path=self.Path
        self.Canvas().File=self.Iteration_FileName(n)
                
        self.Canvas().Canvas_Init(p1,p2)
 
        return self.Canvas()

    def Iteration_Save(self,n):
        filename=self.Canvas().Image_Write()

        self.Iteration_Files.append(filename)
        if (int(self.Images_Rewrite)>0):
            self.Canvas().Image_Rewrite()
            
        return filename
    


