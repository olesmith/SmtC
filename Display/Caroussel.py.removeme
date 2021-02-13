import os


from Base import *

class Display_Caroussel():
    Delay=200
    
    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def Display_Caroussel(self):
        self.Display_HTTP_Headers_Print()
        
        query=self.CGI_Query_Path()
        indent=3

        html=self.Display_Header()
        html=html+self.HTML_Indent(indent)
        html=html+self.XML_Tag_Start("BODY")+"\n"
        
        html=html+self.Display_Caroussel_HTML()
        
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
    
    def Display_Caroussel_IMG_SRC(self,svgfile):
         return "?".join( [ self.CGI_Root+"/"+"SVG",svgfile ] )
        
    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def Display_Caroussel_HTML(self):
        query=self.CGI_Query_Path()
        rquery="/".join( [ self.FS_Root,query ] )

        svgfiles=self.Path_Files(rquery,'\d+\.svg')
        mtime=self.Files_MTime(svgfiles)


        #return [ "Path",query,rquery,svgfiles]
        html=[]
        html=html+[ self.XML_Tag_Start("CENTER") ]
        html=html+[ self.XML_Tag_Start("DIV",{ "class": "w3-content w3-section" }) ]
        html=html+[ self.XML_Tags_NL("DIV","Generated: "+self.Time_Show(mtime),{"class": "Date", }) ]

        comps=query.split('/')
        if ( len(comps)>1 ):
            url="/curves/"+comps[1]
            html=html+[ self.A(url,"SVGs",options={}) ]
        
        imgargs={
            "class": "mySlides",
            "height": self.Display_Setup_Key("RY"),
            "width":  self.Display_Setup_Key("RX"),
        }
        for svgfile in svgfiles:
            svgfile=re.sub(self.FS_Root,"",svgfile)

            imgargs[ "src"]=self.Display_Caroussel_IMG_SRC(svgfile)
            html=html+[ self.XML_Tag_Start("IMG",imgargs) ]
            
        html=html+[ self.XML_Tag_End("DIV") ]
        
        js=self.File_Read(    "/".join( [ self.FS_Root,"poops.js" ] )    )
        js=re.sub(r'#Delay',str(self.Delay),js)

        html=html+[ self.XML_Tags_NL("SCRIPT",js) ]
        html=html+[ self.XML_Tag_End("CENTER") ]


        return  html
