import re

from File import *
from Base import *
from subprocess import call

class Animation_Html():
    
    ##! 
    ##! Animation main HTML path
    ##!
    
    def Animation_HTML_Path(self):
        return "/".join( [ self.Path,self.FileName,self.Curve_Parms_Path ] )
    
    ##! 
    ##! Animation main HTML file name
    ##!
    
    def Animation_HTML_FileName(self):
        return "/".join( [self.Animation_HTML_Path(),self.Name+".html"] )
    
    ##! 
    ##! HTML head section
    ##!
    
    def Animation_HTML_Doc_Head(self):
       return (
            "<!DOCTYPE html>\n"+
            self.XML_Tag_Start("HTML")+
            self.Animation_HTML_Head()
       )
   
    ##! 
    ##! Write animation main HTML file
    ##!
    
    def Animation_HTML_Write(self):
        html=self.Animation_HTML_Doc_Head()
        html=html+self.Animation_HTML_Body()
        html=html+self.XML_Tag_End("HTML")

        outfile=self.Animation_HTML_FileName()
        self.File_Path_Create(outfile)

        res=self.File_Write(outfile,[html])
        print outfile+":",res,"bytes"

        
    ##! 
    ##! Write animation css
    ##!
    
 
    def Animation_HTML_CSS(self):
        return self.XML_TagIt(
            "LINK",
            {
                "rel": "stylesheet",
                "href": self.HTML_Root+"/W3.css",
            }
        )+"\n"+self.XML_TagIt(
            "LINK",
            {
                "rel": "stylesheet",
                "href": self.HTML_Root+"/Poops.css",
            }
        )
    
    ##! 
    ##! Write animation script section
    ##!
    
    def Animation_HTML_Script(self):
        return self.XML_Tags_NL(
            "SCRIPT",
            self.File_Read("poops.js")
        )
            
        
    ##! 
    ##! Write animation head section
    ##!
    
 
    def Animation_HTML_Head(self):
        return self.XML_Tags_NL(
            "HEAD",
            self.Animation_HTML_Title()+self.Animation_HTML_CSS()
        )
            
    ##! 
    ##! Write animation title section
    ##!
    
    def Animation_HTML_Title(self):
        return self.XML_Tags_NL(
            "TITLE",
            "TITLE"
        )

    
    ##! 
    ##! Write animation body section
    ##!

    def Animation_HTML_Body(self):
        return self.XML_Tags_NL(
            "BODY",
            self.Animation_HTML_Animation_Element()
        )

    ##! 
    ##! Write animation SVG animation element.
    ##!

    def Animation_HTML_Animation_Element(self):
        imgs=[""]
        n=0
        for svgfile in (self.Iteration_Files):
            imgs.append(
                self.Animation_HTML_Body_File_IMG(svgfile,n)
            )
            n+=1

        
        return self.XML_Tags(
            "DIV",
            "\n".join(imgs)+"\n",
            {
                "class": "w3-content w3-section",
            }
        )+"\n"+self.Animation_HTML_Script()

    ##! 
    ##! Generate animated image tag.
    ##!

    def Animation_HTML_Body_File_IMG(self,svgfile,n=0):
        href=self.CGI_Root+"?"+svgfile

        return self.XML_Tag(
            "IMG",
            {
                "src":   href,
                "width": "800px",
                "class": "mySlides",
            }
        )
    
