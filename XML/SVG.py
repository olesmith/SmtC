from Base import *
from CGI import CGI

class XML_SVG(CGI):
    Unit=""
    Px=""
    
    def SVG_Unit(self):
        return self.Unit
    
    def SVG_Px(self):
        return self.Px
        
    def SVG_Write(self,canvas,svg,svgname):
        self.File_Path_Create(svgname)
        svg=self.SVG_Pre_Amble(canvas)+svg+self.SVG_Post_Amble(canvas)
        svg=self.XML_Print(svg)
        self.File_Write(svgname,[svg],True)
        
    def SVG_Pre_Amble(self,canvas):
        svg=[]
        svg=svg+self.SVG_Head()
        svg=svg+self.SVG_Header(canvas)
        svg=svg+[    "<!-- **** DRAWING START **** -->" ]

        return svg

    def SVG_Post_Amble(self,canvas):
        return [
            "<!-- **** DRAWING END **** -->",
            self.SVG_Close()
        ]

        
    def SVG_Version(self):
        return [
            '<?xml version="1.0"?>',
        ]
    def SVG_CSS_External(self):
        return [
            #'<?xml-stylesheet type="text/css" href="style8.css" ?>',
            '<?xml-stylesheet type="text/css" href="http://127.0.0.1/poops.css" ?>',            
        ]

    def SVG_DOCTYPE(self):
        return [
            '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"',
            '    "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">',
            '',
        ]

        
    def SVG_Head(self):
        return self.SVG_Version()+self.SVG_CSS_External()+self.SVG_DOCTYPE()

    
    def SVG_Header(self,canvas):
         svg=[
             self.SVG_Open(canvas),
             #self.SVG_CSS_Internal(),
             self.SVG_Title(self.Name),
             self.SVG_Name(self.Name),
         ]

         svg=svg+self.SVG_Defs()
         
         return svg
       
    def SVG_ViewBox(self,canvas):
        viewbox=[0,0,canvas.Resolution[0],canvas.Resolution[1]]

        #viewbox=[
        #    str(canvas.pmin[0])+self.SVG_Unit(),
        #    str(canvas.pmin[1])+self.SVG_Unit(),
        #    str(canvas.pmax[0])+self.SVG_Unit(),
        #    str(canvas.pmax[1])+self.SVG_Unit(),
        #]
        
        return viewbox
    
    def SVG_Open(self,canvas):
        return self.XML_Tag(
            "svg",
            {
                "xmlns":            'http://www.w3.org/2000/svg',
                "xmlns:xlink":      'http://www.w3.org/1999/xlink',
                "version":          "1.1",
                "width":            str(canvas.Resolution[0])+self.SVG_Px(),
                "height":           str(canvas.Resolution[1])+self.SVG_Px(),
                "viewBox":          self.SVG_ViewBox(canvas),
            }
        )
    
    def SVG_Close(self):
        return "</svg>"


    def SVG_CSS_URL(self,css="http://127.0.0.1/poops.css"):
        return css

    def SVG_CSS_Internal(self,css="poops.css"):
        css=self.File_Read(css)
        css="\n/* CSS BEGIN */\n"+css
        css=css+"\n/* CSS END */\n"

        css="<![CDATA[\n"+css+"]]>"
        return self.XML_Tags("style",css)

    def SVG_Title(self,title):
        return self.XML_Tags("title",title)

    def SVG_Name(self,name):
        return self.XML_Tags("name",name)

    def SVG_Defs(self):
        return [
            '<defs>',
            '</defs>',
        ]

    def SVG_BackGround_Polygon(self):
        resx=str(self.Resolution[0])
        resy=str(self.Resolution[1])
        pxs=[ "0 0",resx+" 0", resx+" "+resy, "0 "+resy ]
        return self.XML_Tag1(
                "polygon",
                {
                    "class": "BackGround",
                    "points": ", ".join(pxs),
                }
            )
    

 
    def SVG_Comment(self,comment):
        return self.XML_Comment(comment)
   
    #### Drawing text
    
    def SVG_Text(self,px,text,classs,color="",size="",parms={}):
        if (not color and not color): color="black"
        if (not size): size="20px"
        
        lparms={
            "x":     str(px[0])+self.SVG_Unit(),
            "y":     str(px[1])+self.SVG_Unit(),
            "class": classs,
            "style": {
                "stroke": color,                
                "fill": color,                
                "font-size": size,                
            }
        }
        
        parms.update(lparms)
        svg=self.XML_Tags("text",text,parms)
         
        return svg
       
    #### Drawing Points
    
    def SVG_Point(self,px,size,classs,color,parms={}):
        lparms={
            "class": classs,
            "cx": str(px[0])+self.SVG_Unit(),
            "cy": str(px[1])+self.SVG_Unit(),
            "r":  str(size)+self.SVG_Px(),
            "style": {
                "stroke": color,                
                "fill": color,                
            }
        }
        
        parms.update(lparms)
        svg=self.XML_Tag1("circle",parms)
        
        return svg
            

    def SVG_Node(self,px,i,size,classs,textclass,color,parms={},textparms={}):
        svg=self.SVG_Point(px,size,classs,color,parms)+"\n"
        svg=svg+self.SVG_Text(px,str(i),textclass,color,"",textparms)

        return svg

    
    #### Drawing Line segments
    ####
    #### Clipping areas
    ####
    #### 1 | 4 | 7
    #### ---------
    #### 2 | 5 | 8
    #### ---------
    #### 3 | 6 | 9
    #### ---------
    ####

    def SVG_Line(self,px1,px2,classs,color,parms={}):
        #clip1=self.Image_Point_Clip_Zone(px1)
        #clip2=self.Image_Point_Clip_Zone(px2)

        #In same zone, both outside
        #if (clip1==clip2 and clip1!=5):
        #    return ""

        #Both in left zone
        #if (clip1<=3 and clip2<=3):
        #    return ""

        #Both in right zone
        #if (clip1>6 and clip2>6):
        #    return ""

        #Both in top zone
        #if ( (clip1 % 3)==1 and (clip2 % 3)==1):
        #    return ""

        #Both in bottom zone
        #if ( (clip1 % 3)==0 and (clip2 % 3)==0):
        #    return ""

        #We need to draw
        #if (clip2!=5):
        #    px2=self.Image_Point_Clip_Point(px1,px2)
            
        #if (clip1!=5):
        #    px1=self.Image_Point_Clip_Point(px2,px1)
                    
        rparms={
            "x1": str(int(round(px1[0]))),
            "y1": str(int(round(px1[1]))),
            "x2": str(int(round(px2[0]))),
            "y2": str(int(round(px2[1]))),
            "class": classs,
            "style": {
                "stroke": color,
            }
        }
        
        rparms.update(parms)

        svg=self.XML_Tag1("line",rparms)

        return svg

    
    #### Drawing Polylines
    
    def SVG_Polyline(self,pxs,classs,color,parms={},close=False):
        if (close):
            psx.append( pxs[0] )
            
        points=[]
        for px in pxs:
            points.append( str(px[0])+self.SVG_Unit()+" "+str(px[1])+self.SVG_Unit() )

        #points=List_Slice(points,10)

        rpoints=[]
        for lpoints in points:
            lpoints=",\n   ".join(lpoints)
            rpoints.append( lpoints )
            
        parms[ "class" ]=classs
        rparms={
            "class": classs,
            "points": "\n   "+",\n   ".join(points)+"\n",
            "style": {
                "stroke": color,
                "fill": "none",
            }
        }

        rparms.update(parms)
        
        svg=self.XML_Tag1("polyline",rparms)

        return svg

    def SVG_Image(self,px,rx,filename,parms={}):
        rparms={
            "x": str(px[0])+self.SVG_Unit(),
            "y": str(px[1])+self.SVG_Unit(),
            "width":  abs(rx[0]),
            "height": abs(rx[1]),
            "xlink:href": filename,
        }
        
        rparms.update(parms)
        
        svg=self.XML_Tag1("image",rparms)

        return svg
    #### Drawing Circles

    def SVG_Circle(self,cx,rx,classs,color="",parms={}):
        if (not color): color="brown"
        
        rparms={
            "class": classs,
            "cx": str(cx[0])+self.SVG_Unit(),
            "cy": str(cx[1])+self.SVG_Unit(),
            "rx": str(abs(rx[0]))+self.SVG_Unit(),
            "ry": str(abs(rx[1]))+self.SVG_Unit(),
            "style": {
                "stroke": color,
                "fill": "none",
            }
        }
        
        rparms.update(parms)
        
        svg=self.XML_Tag1("ellipse",rparms)
        
        return svg
                
        
    def SVG_Vector(self,px1,px2,classs,color,parms={}):
        #Size of arrows
        vscale=0.1
        nscale=0.5*vscale

        v=px2-px1
        n=v.Transverse2()*nscale
        v*=vscale

        pxs=[px2,px2-v+n,px2-v-n,px2]

        svg=[]
        rparms=dict(parms)
        
        rparms[ "class" ]=classs

        svg.append( self.SVG_Line(px1,px2,classs,color,rparms) )
        rparms[ "style" ]={
            "stroke": color,
            "fill": color,
        }
        
        svg.append( self.SVG_Polyline(pxs,classs,color,rparms) )
        
        return svg
    
 
    def SVG_Mesh(self,pxs,size,classs,color="black",parms={}):
        svg=[]
        parms[ "class" ]=classs

        for px in pxs:
            svg.append( self.SVG_Point(px,size,classs,color,parms) )

        return svg
            
    def SVG_Curve_Conns_Clips(self,pxs):
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

        
        return rpxss
             
    def SVG_Curve_Conns(self,pxs,classs,color="yellow",parms={},close=False):
        svg=""
        
        svg=self.SVG_Polyline(pxs,classs,color,parms)
        return svg
             
    def SVG_Point_Texts(self,pxs,size,classs,parms={}):
        svg=[]
        i=1
        for px in pxs:
            svg.append( self.SVG_Text(px,str(i),classs,"","",parms) )
            i+=1
                        
        return svg
            
    def SVG_Conns(self,pxs,classs,color="orange",parms={}):
        svg=[]
        svg=svg+[self.SVG_Curve_Conns(pxs,classs,color,parms)]
         
        return svg
            
    def SVG_Overlay(self,svgfile):
        svgs=[]
        
        svgs=svgs+[ "<!-- *** Start: "+re.sub(r'-',"&ndash;",svgfile)+" *** -->" ]
        svgs=svgs+self.SVG_2_Body(svgfile)
        svgs=svgs+[ "<!-- *** End: "+re.sub(r'-',"&ndash;",svgfile)+" *** -->" ]
        
        return svgs
            
    def SVGs_Overlay(self,rsvgfile,canvas,svgfiles,basesvg=[]):
        svgs=self.SVG_Pre_Amble(canvas)
        
        svgs=svgs+basesvg
        for svgfile in svgfiles:
            svgs=svgs+self.SVG_Overlay(svgfile)
            
        svgs=svgs+self.SVG_Post_Amble(canvas)

        self.File_Write(rsvgfile,svgs,True)
        #call(["/usr/local/bin/svg2pdf.pl",rsvgfile ])
        
        return svgs
            
    def SVG_2_Body(self,svgfile):
        svg=self.File_Read(svgfile)

        svgs=svg.split("\n")

        rsvg=[]
        i=0
        while (i<len(svgs)):
            if ( re.search(r'DRAWING\s+START',svgs[i]) ):
                i+=1 #ignore current
                while (i<len(svgs) and not re.search(r'DRAWING\s+END',svgs[i]) ):
                    rsvg.append( svgs[i] )
                    i+=1
            else:
                i+=1
            
        return rsvg
    
    def SVGs_Overlays(self,canvas,defs,basesvg=[]):
        for svgfile in defs.keys():
            files=defs[svgfile ]
            self.SVGs_Overlay(svgfile,canvas,files,basesvg)
            
    def SVGs_Parms_Overlays(self,path,name,canvas,parms,basefiles=[]):
        defs={}

        basesvg=[]
        for basefile in basefiles:
            svg=self.SVG_2_Body(basefile)
            svg=self.SVG_Change_Class(svg,"Curve_","Base_")
            basesvg=basesvg+svg
                            
        
        rname=path+"/"+name+".svg"
        defs[ rname ]=[]
        for a in parms[ "a" ]:
            for b in parms[ "b" ]:
                for c in parms[ "c" ]:
                    for n in parms[ "n" ]:
                        parmsname="-".join( [ str(a),str(b),str(c),str(n) ] )
                        rrname=path+"/"+name+"-"+parmsname+".svg"            
                        defs[ rrname ]=[]
                        for type in parms[ "Types" ]:
                            fname=path+"/"+type+"-"+parmsname+".svg"            
                            defs[ rname ].append(fname)
                            defs[ rrname ].append(fname)

        
        self.SVGs_Overlays(canvas,defs,basesvg)

                            
        
    def SVG_Change_Class(self,svg,classs,outclass):
        for i in range( len(svg) ):
            if (re.search(r'class="'+classs,svg[i])):
                svg[i]=re.sub(r'class="'+classs,'class="'+outclass,svg[i])
                
        return svg
            
