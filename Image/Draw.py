from math import *

class Image_Draw():

    def Image_Add_Open_Tag(self,tag,options={}):
        self.SVG.append(self.XML_TagIt(tag,options))
                
    def Image_Add_Close_Tag(self,tag):
        self.SVG.append(self.XML_TagIt("/"+tag))
                
    #### Drawing text
    
    def Image_Draw_Text(self,px,text,classs,color="",size="",parms={}):
        svg=self.SVG_Text(px,text,classs,color,size,parms)
        self.SVG.append(svg)
         
        return svg
       

    #### Drawing Points
    
    def Image_Draw_Point(self,px,size,classs,color,parms={}):
        svg=self.SVG_Point(px,size,classs,color,parms)
        self.SVG.append(svg)
        
        return svg
            
    def Image_Draw_Node(self,px,i,size,classs,textclass,color,parms={},textparms={}):
        
        svg=self.SVG_Node(px,i,size,classs,textclass,color,parms,textparms)
        self.SVG.append(svg)
        
        return svg

    #### Drawing Meshes
    
    def Image_Draw_Mesh(self,pxs,classs,color="blue",parms={},close=False):
        rpxss=[]
        rpxs=[]
        n=0
        while ( n<len(pxs) ):
            if  ( self.Image_Point_InView( pxs[n] ) ):
                rpxs.append(pxs[n])
                while (n+1<len(pxs) and self.Image_Point_InView( pxs[n+1] ) ):
                    rpxs.append(pxs[n+1])
                    n+=1
                    
            else:
                rpxs=[]                
                while (n+1<len(pxs) and not self.Image_Point_InView( pxs[n+1] ) ):
                    n+=1
            n+=1

        if ( len(rpxs)>0 ):
            rpxss.append( rpxs )

        svg=self.SVG_Polyline(pxs,classs,color,parms,close)
        self.SVG.append(svg)
        #print svg
        #rsvg=""
        #for rpxs in rpxss:
        #    svg=self.SVG_Polyline(rpxs,classs,parms,close)
        #    self.SVG.append(svg)
        #    rsvg=rsvg+svg+"\n"

        return svg
            
    #### Drawing Line segments

    def Image_Draw_Line(self,px1,px2,classs,color,parms={}):
        svg=self.SVG_Line(px1,px2,classs,color,parms)
        self.SVG.append(svg)
        
        return svg
                
    #### Drawing Images (bitmaps)
    
    def Image_Draw_Image(self,px,imagefile):
        return
        
    #### Drawing Polylines
    
    def Image_Draw_Polyline(self,pxs,classs,color,parms={},close=False):
        svg=self.SVG_Polyline(pxs,classs,color,parms,close)
        self.SVG.append(svg)

        return svg
            
    #### Drawing Circles

    def Image_Draw_Circle(self,cx,rx,classs,color="",parms={}):
        svg=self.SVG_Circle(cx,rx,classs,color,parms)
        self.SVG.append(svg)
        
        return svg
                
        
        
