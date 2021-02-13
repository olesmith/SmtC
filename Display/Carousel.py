import os


from Base import *

class Display_Carousel():
    Delay=200
    
    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def Display_Carousel(self):
        self.Display_HTTP_Headers_Print()
        
        query=self.CGI_Query_Path()
        indent=3

        html=self.Display_Header()
        html=html+self.HTML_Indent(indent)
        html=html+self.XML_Tag_Start("BODY")+"\n"
        
        html=html+self.Display_Carousel_HTML()
        
        html=html+self.XML_Tag_End("CENTER")+"\n"
        html=html+self.XML_Tag_End("BODY")+"\n"
        
        html=html+self.Display_Tailer()

        print html

        
    def CGI_Query_Path(self):
        query=self.CGI_Query_String()
        comps=query.split('&')

        paths=comps[0].split("/")
        if (len(paths)==5):
            path=self.FS_Root+"/"+comps[0]
            paths=glob.glob(self.FS_Root+"/"+comps[0]+"/*")
            paths=sorted(paths)

            
            path=paths.pop(0)
            path=re.sub(self.FS_Root+"/","",path)
            return path
        return comps[0]
        
    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def Display_Carousel_HTML(self):
        query=self.CGI_Query_Path()
        rquery="/".join( [ self.FS_Root,query ] )

        svgfiles=self.Path_Files(rquery,'\d+\.svg')
        mtime=self.Files_MTime(svgfiles)


        #return [ "Path",query,rquery,svgfiles]
        html=[]
        html=html+[ self.XML_Tag_Start("CENTER") ]
        
        comps=query.split('/')
        if ( len(comps)>1 ):
            url="/curves/"+comps[1]
            html=html+[ self.A(url,"SVGs",options={}) ]
        
        imgargs={
            "class": "mySlides",
            "height": self.Display_Setup_Key("RY"),
            "width":  self.Display_Setup_Key("RX"),
        }
        
        html=html+self.HTML_Carousel_Display(self.FS_Root,rquery,svgfiles,1,imgargs)
        html=html+self.HTML_Carousel_JS(delay)
        html=html+[ self.XML_Tag_End("CENTER") ]

        return html
