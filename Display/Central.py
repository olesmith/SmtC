import os

from Base import *

class Display_Central():

    Display_Central_Var_Names=["","",'a','b','c','N']
    
    ##! 
    ##! Animation typed file name.
    ##!
    
    def Display_File_Name(self,name):
        query=self.CGI_Query_Path()
        htmlfile="/".join( [
            self.BasePath,            
            query,
            name
        ] )
        
        if (os.path.isfile(htmlfile)):
            return htmlfile

        print "No such file: "+htmlfile

        return None
        
    ##! 
    ##! Animation typed file url.
    ##!
    
    def Display_File_URL(self,name):
        htmlfile=self.Display_File_Name(name)
        
        if (htmlfile and os.path.isfile(htmlfile)):
            return "/".join( [
                "http://127.0.0.1",
                self.HtmlPath,
                htmlfile
            ] )
            

        return None
        
    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def HTML_Central_Screen(self):
        html=[]

        hs=self.Hs(self.Animation_Titles)        
        
        html=html+[ self.BR()+self.BR() ]
        html=html+[ self.Display_Central_Info() ]

        html=html+[ self.Display_Carousel_HTML() ]
        
        html=html+[ self.Display_Central_Info_Images() ]
        
        html=html+[ self.BR()+self.BR() ]
        html=html+[ self.Display_Frames_HTML() ]

        return html

    
    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def Display_Central_Info(self):
        html=self.H(1,"PooPys")
        phtmls=[]
        
        indent=6
        query=self.CGI_Query_Path()
        spaths=query.split('/')
        
        paths=[ self.FS_Root ]

        size=1
        for spath in spaths:
            paths.append(spath);
            
            abspath="/".join(paths)

            if (size<len(self.Display_Central_Var_Names) and self.Display_Central_Var_Names[ size-1 ]):
                phtmls.append(  self.Display_Central_Var_Names[ size-1 ]+"="+spath  )


            fhtml=""
            infofile="/".join([ abspath,"Info.html" ])
            if (self.File_Exists(infofile)):
                fhtml=fhtml+self.HTML_Parse( self.File_Read(infofile) )
                
            size+=1
                
            html=html+self.H(size,fhtml,{"class": "Info_"+str(size),})
                

        return html+self.BR()+", ".join(phtmls)

    ##! 
    ##! Generates SRC for individual images.
    ##!
    
    def Display_Central_IMG_SRC(self,svgfile):
        svgfile=re.sub(self.FS_Root+"/","",svgfile)
        return "?".join( [ self.CGI_Host_Name_Qualified()+"/cgi-bin/"+"SVG",svgfile ] )
        
    ##! 
    ##! Generates Curve Info image.
    ##!
    
    def Display_Central_Info_Image(self,rfile,args):
        svgfile="/".join( [ self.FS_Root,self.CGI_Query_Path(),rfile+".svg"  ])
        
        #Keep changes local
        rargs=dict(args)
        rargs[ "title" ]=rfile+"(t)"

        return self.HTML_Image_Add_If_Exists(
            svgfile,
            self.Display_Central_IMG_SRC(svgfile),
            rargs
        )
    
    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def Display_Central_Info_Images(self):
        args={
            "class": "",
            "height": "300",
            "width":  self.Display_Setup_Key("RX"),
        }

        html=[]
        html=html+[ self.XML_Tag_Start("CENTER") ]
        for rfile in [ "phi","Det" ]:
            html=html+self.Display_Central_Info_Image(rfile,args)

        html=html+[ self.XML_Tag_End("CENTER") ]
        return  html
    
    ##! 
    ##! Generates Middle row geometry info frame.
    ##!
    
    def Display_Middle_Geometry_Frame(self):
        query=self.CGI_Query_Path()
        url="/".join( [ self.HTML_Root,query,"Curve.html" ] )
        
        comps=query.split('/')
        if ( len(comps)<6 ): return []
        
        html=""
        if (url and len(comps)>2 ):
            args={
                "width":  "100%",
                "height": self.Setup[ "RY" ],
                "class": "GeometryFrame",
            }
            
            html=self.HTML_Indent(6)+self.IFrame(url,args)
            
        return html

