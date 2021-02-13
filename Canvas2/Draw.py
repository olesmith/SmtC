from math import pi

class Canvas2_Draw():
    def Draw_Text(self,p,text,classs):
        self.Image_Draw_Text(self.P2Pix(p),text,classs)
    
    
    def Draw_Point(self,p,size,classs,color,parms={}):
        return self.Image_Draw_Point(self.P2Pix(p),size,classs,color,parms={})
    
    def Draw_Segment(self,p1,p2,classs,color="",parms={}):
        if (not color): color="magenta"
        return self.Image_Draw_Line(self.P2Pix(p1),self.P2Pix(p2),classs,color,parms)
    
    def Draw_Node(self,p,i,size,classs,textclass,color,parms={},textparms={}):
        color="cyan"
        return self.Image_Draw_Node(
            self.P2Pix(p),
            i,
            size,
            classs,
            textclass,
            color,
            parms,
            textparms
        )

    #Drawing points as nodes
    def Draw_Nodes(self,ps,size,classs,textclass,color,parms={},textparms={},every=1):

        svns=[]
        for i in range( len(ps) ):
            if ( (i % every)==0):
                svn=self.Draw_Node(
                    ps[i],
                    i,
                    size,
                    classs,
                    textclass,
                    color,
                    parms,
                    textparms
                )

                svns.append(svn+"\n")

        return svns
 
    
    def Draw_Vector(self,p1,p2,classs,color="maroon",parms={}):
        px1=self.P2Pix(p1)
        px2=self.P2Pix(p2)

        svg="\n".join( self.SVG_Vector(px1,px2,classs,color,parms) )
        self.SVG.append( svg )
        return svg

    def Draw_CS(self,O,e,f,classs,color,parms={}):
        svg=""
        svg=svg+self.Image_SVG_Comment("Drawing CS: "+classs)

        svg=svg+self.Draw_Point(O,self.Point_Size,classs,color,parms)
        svg=svg+self.Draw_Vector(O,O+e,classs,color,parms)

        if (f):
            svg=svg+self.Draw_Vector(O,O+f,classs,color,parms)

        return svg
    
        
    def Draw_Circle(self,pc,r,classs,color="",parms={}):
        if (not color): color="brown"
        
        pcx=self.P2Pix(pc)
        rx=self.V2Pix([r,r])

        return self.Image_Draw_Circle(pcx,rx,classs,color,parms)

    def Draw_Polyline(self,ps,classs,color,parms={},close=False):
        
        pxs=self.Ps2Pix(ps)
        return self.Image_Draw_Polyline(pxs,classs,color,parms,close)

        
    def Draw_Arc(self,pc,r,ang1,ang2,color,width=1,npoints=100):
        pxs=self.P2Pix([ pc[0]+r*cos(ang1) , pc[1]+r*sin(ang1) ])
        
        dang=(ang2-ang1)/(1.0*(npoints-1))
        ang=ang1
        
        for i in range(npoints):
            px=self.P2Pix([ pc[0]+r*cos(ang) , pc[1]+r*sin(ang) ])
            pxs.append( px )

            ang+=dang

        classs="Arc"
        return self.Image_Draw_Polyline(pxs,classs,color)
    
        #Remove width parameter
        
    def Draw_Arc_Span(self,pc,v,ang,classs,color,npoints=100):
        
        dang=ang/(1.0*(npoints-1))
        ang=0.0

        pxs=[]
        for i in range(npoints):
            p=pc+v.Rotate2(ang)
            px=self.P2Pix(p)
            pxs.append(px)
            
            ang+=dang
            
        return self.Image_Draw_Polyline(pxs,classs,color)
    
        
    def Draw_Circle_Span(self,pc,v,ang1,ang2,classs,color,npoints=100):
        
        dang=(ang2-ang1)/(1.0*(npoints-1))
        rang=ang1

        pxs=[]
        for i in range(npoints):
            p=pc+v.Rotate2(rang)
            px=self.P2Pix(p)
            
            pxs.append(px)
            rang+=dang

        return self.Image_Draw_Polyline(pxs,classs,color)

    
    def Draw_Circle_Span_External(self,pc,v,angle,classs,color,npoints=100):
        angle2=-2.0*pi
        if (angle>0.0):
            angle2=2.0*pi
            
        return self.Draw_Circle_Span(pc,v,angle,angle2,classs,color,npoints)
    
    def Draw_Circle_Span_Internal(self,pc,v,angle,classs,color,npoints=100):
        return self.Draw_Circle_Span(pc,v,0.0,angle,classs,color,npoints)
    
    
    def Draw_Circle_Spans(self,pc,v,angle,classs,invclasss,color,invcolor,npoints=100):
        if (angle<0.0):
            tmp=classs
            classs=invclasss
            invclasss=tmp
            
            tmp=color
            color=invcolor
            invcolor=tmp
            
        svg=self.Draw_Circle_Span_External(pc,v,angle,classs,color,npoints)
        return svg+self.Draw_Circle_Span_Internal(pc,v,angle,invclasss,invcolor,npoints)
    
        
    
    
