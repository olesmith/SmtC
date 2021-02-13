import os,glob


from Base import *


class caroussel(Base):
    Delay=200
    
    ##! 
    ##! Generates Carroussel java script as code.
    ##!
    
    def Caroussel_JS(self,basepath,delay):
        js=self.File_Read_Lines(    "/".join( [ basepath,"poops.js" ] )    )
        for i in range( len(js) ):
            js[i]=re.sub(r'#Delay',str(delay),js[i])

        return js
        
    ##! 
    ##! Generates Carroussel image entries.
    ##!
    
    def Caroussel_Images(self,basepath,svgfiles,imgargs={},every=1):
        imgargs[ "class" ]="mySlides"

        html=[]
        n=0
        m=0
        for svgfile in svgfiles:
            if ( (n % every)==0 ):
                svgfile=re.sub(basepath,"",svgfile)
                imgargs[ "src"]=svgfile
                imgargs[ "title"]=svgfile
                html.append( self.XML_Tag_Start("IMG",imgargs) )
                m+=1
            n+=1

        return html
        
    ##! 
    ##! Generates Carroussel entry (as html)
    ##!
    
    def Caroussel_Display(self,globpath,basepath,every=1,delay=200,imgargs={}):
        if (not basepath): basepath=="/var/www/html"
        globpath="/".join([ basepath,globpath ])

        svgfiles=glob.glob(globpath)
        svgfiles.sort()
        mtime=self.Files_MTime(svgfiles)
        
        n=len(svgfiles)
        m=n % every
        
        html=[]
        html=html+[
            self.XML_Tag_Start("DIV",{ "class": "w3-content w3-section" }),
            self.Caroussel_Images(basepath,svgfiles,imgargs,every),
            self.XML_Tag_End("DIV"),
            self.XML_Tags(
                "SCRIPT",
                self.Caroussel_JS(basepath,delay)
            ),
            self.XML_Tags("DIV","Generated: "+self.Time_Show(mtime),{"class": "Caroussel_Info_Text", }),
            self.XML_Tags("DIV","Delay: "+delay,{"class": "Caroussel_Info_Text", }),
            self.XML_Tags("DIV",str(m)+" of "+str(n)+" images",{"class": "Caroussel_Info_Text", }),
            self.XML_Tags("DIV","Glob: "+globpath,{"class": "Caroussel_Info_Text", }),
        ]

        return  html
