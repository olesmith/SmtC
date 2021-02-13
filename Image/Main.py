
from Colors import Image_Colors
from Fonts  import Image_Fonts
from Draw   import Image_Draw
from IO     import Image_IO
from SVG    import Image_SVG

from Base import Base


class Image(Image_IO,Image_SVG,Image_Colors,Image_Fonts,Image_Draw,Base):
    RX=800
    RY=800
    Resolution=[800,800]
    #Image=""
    SVG=None
    
    Font=""
    Path="Graphics"
    File="I"
    Name="Image"
    W=False

    BackGround=(0,0,0)
    BackGround_Color="Black"

    Point_Size=3
    Text_Size=20
    Clipping=False

    
    def __init__(self,vals={}):
        self.Hash2Obj(vals)
        self.Image_Rewrite()

    def Image_File(self):
        return self.Path+"/"+self.File+".svg"

    def Pix_In_Image(self,px):
        #return True
        for i in range(2):
            if (px[i]<0 or px[i]>self.Resolution[i]):
                return False

        return True
    def Image_SVG_Append(self,svg):
        if (svg.__class__.__name__=="list"):
            self.SVG=self.SVG+svg
        else:
            self.SVG.append( svg )
    
    def Image_SVG_Comment(self,comment):
        svg=self.SVG_Comment(comment)
        self.SVG.append(svg)

        return svg
   
    def Image_SVG_Tag1(self,tag,options):
        self.SVG.append( self.XML_Tag1(tag,options) )
   
   
    def Image_Point_InView(self,px):
        for i in range(2):
            if (px[i]<0.0 or px[i]>1.0*self.Resolution[i]):
                return False
            
        return True
       
   
    def Image_Point_Clip_Zone(self,px):
        resx=1.0*self.Resolution[0]
        resy=1.0*self.Resolution[1]

        pos=0
        if (px[0]<0.0):
            #esquerda
            if (px[1]<0.0):
                pos=1
            elif (px[1]<resy):
                pos=2
            else:
                pos=3
        elif (px[0]<=resx):
            if (px[1]<0.0):
                pos=4
            elif (px[1]<resy):
                pos=5
            else:
                pos=6
        else:
            if (px[1]<0.0):
                pos=7
            elif (px[1]<resy):
                pos=8
            else:
                pos=9

        
        return pos
    
    #### Clips second point with relation to canvas
   
    def Image_Point_Clip_Point(self,px1,px2):
        #Clipping disabled?
        if (not self.Clipping):
            return px2
    
        
        resx=1.0*self.Resolution[0]
        resy=1.0*self.Resolution[1]
        clip2=self.Image_Point_Clip_Zone(px2)
        if (clip2!=5):
            #Clip second point

            ty=1.0
            dpy=1.0*px2[1]-1.0*px1[1]
            
            if ( dpy==0.0 ):
                ty=1.0
                
            elif ( (clip2 % 3)==1 and px2[1]!=px1[1] ):
                #Above
                ty=-1.0*px1[1]/dpy
                
            elif ( (clip2 % 3)==0 and px2[1]!=px1[1]):
                #Below
                ty=(1.0*resx-1.0*px1[1])/dpy
                
            tx=1.0
            dpx=1.0*px2[0]-1.0*px1[0]
            
            if ( dpy==0.0 ):
                tx=1.0
                
            elif ( clip2<=3 and px2[0]!=px1[0] ):
                #Left
                tx=-1.0*px1[0]/dpx
                
            elif ( clip2>6 and px2[0]!=px1[0]):
                #Right
                ty=(1.0*resy-1.0*px1[1])/dpy
            
            t=min(tx,ty)
            px2=px1*(1.0-t)+px2*t


        return px2
        

       
   
    
