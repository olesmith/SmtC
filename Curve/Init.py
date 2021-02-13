
class Curve_Init():
    ##!
    ##! Detects curve min point. Considers evolute, if on.
    ##!
    
    def Curve_Min(self):
        p=self.R.Min()       
        if (self.Evolute_Numerical):
            p=p.Min(self.Evolute_R.Min())
            
        if (self.Evolute_Anal):
            p=p.Min(self.Evolute_Analytical.Min())

        if (self.Roulette):
            p=p.Min(self.Roulette.R.Min())

        return p
   
    ##!
    ##! Detects curve max point. Considers evolute, if on.
    ##!
    
    def Curve_Max(self):
        p=self.R.Max()       
        if (self.Evolute_Numerical):
            p=p.Max(self.Evolute_R.Max())
            
        if (self.Evolute_Anal):
            p=p.Max(self.Evolute_Analytical.Max())

        if (self.Roulette):
            p=p.Max(self.Roulette.R.Max())

        return p
   
    ##!
    ##! Initialize curve:
    ##!  -- Find min and max
    ##!  -- Considere Evolute, if on.
    ##!  -- Call self.Animation for initializing animation iteration.
    ##!
    
    def Curve_Init(self,n,frame):
        if (hasattr(self,self.rc+"_Init")):
            method=getattr(self,self.rc+"_Init")
            method()
        
        p1=self.Curve_Min() 
        p2=self.Curve_Max() 
        
        self.Zoom=float(self.Zoom)
        if (self.Zoom!=1.0):
            dp=p2-p1
            dp*=(self.Zoom-1.0)

            p1-=dp
            p2+=dp
        
        self.Animation().Iteration_Init(frame,p1,p2)
        if (hasattr(self,self.rc+"_Init")):
            method=getattr(self,self.rc+"_Init")
            method()
        
          
        return 
