from math import *

from Mesh import *


class Curve_Samples():

    def Ellipse(self,pc,a,b,n=100,name=""):
        ellipse=Mesh(name)

        

        dt=2.0*pi/(1.0*n)
        t=0.0
        for i in range(n+1):
            ellipse.append( [ pc[0]+a*cos(t) , pc[1]+b*sin(t) ] )
            t+=dt

        return ellipse

    def Draw_Ellipse(self,pc,a,b,color,n=100,mcolor=0):

        if (mcolor==0):
            mcolor=self.BackGround_Color()
            
        self.Ellipse(pc,a,b,n).Draw_Both(
            self.Canvas(),
            n+1,
            color,
            mcolor
        )
    


    def Circle(self,pc,r,n=100):
        return self.Ellipse(pc,r,r,n)

    def Draw_Circle(self,pc,r,classs):
        return self.Canvas().Draw_Circle(pc,r,classs)
        
    def Draw_Arc(self,pc,r,ang1,ang2,color,npoints=100,mcolor=0):
        cx=self.Canvas().P2Pix(pc)
        rx=self.Canvas().V2Pix([r,r])

        return self.Canvas().Image_Draw_Arc(cx,rx[0],ang1,ang2,color,npoints)
    
    def Draw_Arc2(self,pc,r,ang1,ang2,color,npoints=100,mcolor=0):
        return self.Canvas().Draw_Arc2(pc,r,ang1,ang2,color,1,npoints)
    
