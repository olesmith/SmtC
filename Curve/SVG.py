from Canvas2 import Canvas2

class Curve_SVG():
        
    ##!
    ##! Write curve vectors to SVG file.
    ##!
    
    def Curve_SVG_Vectors(self,vs,canvas,svgname,classs,color,r=[]):
        svgs=[]
        for n in range( len(self.R) ):
            if (not r): r=self.R[n]

            svgs=svgs+[
                self.SVG_Vector(
                    self.Canvas().P2Pix(r),
                    self.Canvas().P2Pix(r+vs[n]),
                    classs,
                    color
                )
            ]
                     
        svgs=self.SVG_Write(canvas,svgs,svgname)
    ##!
    ##! Write curve Velocities to SVG file.
    ##!
    
    def Curve_SVGs(self,canvas,svgname,classs,color):
        return self.R.Mesh_SVG(canvas,svgname,classs,color)

    ##!
    ##! Write curve Velocities to SVG file.
    ##!
    
    def Curve_SVG_Velocities(self,canvas,svgname,classs,color):
        return self.Curve_SVG_Vectors(self.dR,canvas,svgname,classs,color)

    ##!
    ##! Write curve Accelerations to SVG file.
    ##!
    
    def Curve_SVG_Accelerations(self,canvas,svgname,classs,color):
        return self.Curve_SVG_Vectors(self.d2R,canvas,svgname,classs,color)

    ##!
    ##! Write curve unit tangents, in self.T,  to SVG file.
    ##! If r not given, use curve point no n.
    ##!
    
    def Curve_SVG_Ts(self,canvas,svgname,classs,color,r=[]):
        return self.Curve_SVG_Vectors(self.T,canvas,svgname,classs,color,r)
        
    ##!
    ##! Write curve unit normals, in self.N,  to SVG file.
    ##! If r not given, use curve point no n.
    ##!
    
    def Curve_SVG_Ns(self,canvas,svgname,classs,color,r=[]):
        return self.Curve_SVG_Vectors(self.N,canvas,svgname,classs,color,r)

    ##!
    ##! Write phi(t) as a function (SVG): (t,phi(t))
    ##!
    
    def Curve_SVG_Phi(self,canvas,svgname,classs,color,r=[]):
        return self.Curve_SVG_Vectors(self.N,canvas,svgname,classs,color,r)

    ##!
    ##! Writes numerical evolute to file.
    ##!
    
    def Curve_SVG_Evolute_Numerical(self,canvas,svgname,classs,color):
        self.Evolute_R.Mesh_SVG(canvas,svgname,classs,color,{},[ self.R ])
 
    ##!
    ##! Writes numerical involute to file.
    ##!
    
    def Curve_SVG_Involute_Numerical(self,canvas,svgname,classs,color):
        self.Involute_R.Mesh_SVG(canvas,svgname,classs,color,{},[ self.R ])
 
        
    ##!
    ##! Writes analytical evolute to file.
    ##!
    
    def Curve_SVG_Evolute_Analytical(self,canvas,svgname,classs,color):
        self.Evolute_Analytical.R.Mesh_SVG(canvas,svgname,classs,color,{},[ self.R ])
 
    ##!
    ##! Writes analytical involute to file.
    ##!
    
    def Curve_SVG_InvoluteAnalytical_(self,canvas,svgname,classs,color):
        self.Involute_Analytical.R.Mesh_SVG(canvas,svgname,classs,color,{},[ self.R ])
 
        
        
    ##!
    ##! Writes roulette evolute to file.
    ##!
    
    def Curve_SVG_Roulette(self,canvas,svgname,classs,color):
        self.Roulette.R.Mesh_SVG(canvas,svgname,classs,color,{},[ self.R ])
 
        
    ##!
    ##! Generate parameters as svg text. 
    ##!
    
    def Curve_SVG_Parms_Text(self):
        return [
            self.SVG_Text([10,15],self.Parameter_Names[0]+"="+str(self.a),"Curve_Text","black","15px"),
            self.SVG_Text([10,35],self.Parameter_Names[1]+"="+str(self.b),"Curve_Text","black","15px"),
            self.SVG_Text([10,50],self.Parameter_Names[2]+"="+str(self.c),"Curve_Text","black","15px"),
        ]

    ##!
    ##! Write curve to SVG file.
    ##!
    
    def Curve_SVG_Write(self,meshes=[]):
        parms={}
        
        canvas=Canvas2(
            {},
            [ self.Curve_Min(),self.Curve_Max() ],
            self.Resolution
        )

        name="Curve"
        svgname=self.Curve_Parms_FileName(self.Name,name,"svg")
        
        paths=svgname.split('/')
        paths.pop()

        parmssvg=self.Curve_SVG_Parms_Text()
        
        color="blue"
        self.R.Color="blue"
        self.R.Mesh_SVG(canvas,svgname,name,"",parms,meshes,parmssvg)

        
        if (self.Evolute_Anal):
            name="Analytical_Evolute"
            svgname=self.Curve_Parms_FileName(self.Name,name,"svg")
            color="red"
            self.Evolute_Analytical.R.Mesh_SVG(canvas,svgname,name,color,parms,[ self.R ],parmssvg)

            
        if (self.Evolute_Numerical):
            name="Numerical_Evolute"
            svgname=self.Curve_Parms_FileName(self.Name,name,"svg")        
            color="orange"
            self.Evolute_R.Mesh_SVG(canvas,svgname,name,color,parms,[ self.R ],parmssvg)

            
            
        if (self.Roulette):
            name="Roulette"
            svgname=self.Curve_Parms_FileName(self.Name,name,"svg")        
            color="green"
            self.Roulette.R.Mesh_SVG(canvas,svgname,name,color,parms,[ self.R ],parmssvg)
           
        

