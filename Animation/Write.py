import re,os

from File import *
from Base import *

class Animation_Write():
    
    ##! 
    ##! Writes Animation to HTML.
    ##!
    
    def Animation_Write_HTML_File(self,html,basename):
        html=[ self.XML_Tags("BODY",html) ]
        html=[ self.Animation_HTML_Doc_Head() ]+html
        html=html+[ self.XML_Tag_End("HTML") ]

        outfile="/".join( [ self.Animation_HTML_Path(),basename ] )

        self.File_Path_Create(outfile)
        html=self.HTML_Print(html)
        
        res=self.File_Write(outfile,[ html ],True)

        poops="/".join( [ self.Animation_HTML_Path(),"poops.css" ] )
        print poops,os.path.isfile(poops)
        if (True):
            command="/bin/cp poops.css "+poops
            print command
            os.system(command)
        else:
            print "Omitting: "+poops

        return outfile

    ##! 
    ##! Writes Animation to HTML.
    ##!
    
    def Animation_Write(self,curve):
        self.Animation_HTML_Write()

        self.Animation_Write_Setup(curve)
        self.Animation_Write_Curve_HTML(curve)
        self.Animation_Write_Image_Nav()
        
        curve.Curve_Write_Datas( self.Animation_HTML_Path() ),
        curve.Curve_Write_SVG( self.Canvas(),self.Animation_HTML_Path() ),

    ##! 
    ##! Writes Animation setup file.
    ##!
    
    def Animation_Write_Setup(self,curve):
        setupfile="/".join( [self.Path,self.FileName,"Setup.inf"] )
        info=[
            "Path: "+self.Path,
            "Name: "+self.Name,
            "RX: "+str(self.Resolution[0]),
            "RY: "+str(self.Resolution[1]),
        ]
        for i in range( len(self.Parameters) ):
            info.append( self.Parameters[i]+": "+self.Parameter_Names[i] )

        self.File_Write(setupfile,info)

        
    ##! 
    ##! Writes Animation curve to HTML.
    ##!
    
    def Animation_Write_Curve_HTML(self,curve):
        return self.Animation_Write_HTML_File(
            curve.Curve_Write_HTML_Nodes(),
            "Curve.html"
        )
        
    ##! 
    ##! Writes Animation curve to HTML.
    ##!
    
    def Animation_Write_Image_Nav(self):
        indent=3
        
        urls=[]
        n=1
        for svgfile in (self.Iteration_Files):
            htmlfile=re.sub('\.svg$',".html",svgfile)
            options={
                "href": self.CGI_Root+"/"+"?"+htmlfile
            }
            urls.append( self.HTML_Indent(indent+1)+self.XML_Tags("A", ("%03d"%n), options ) )
            n+=1

        urls=List_Slice(urls,20)

        sep="\n"+self.HTML_Indent(indent)+"|"
        html=""
        for rurls in urls:
            if ( len(rurls)>0 ):
                html=html+self.HTML_Indent(indent)+"[ "
                html=html+sep.join(rurls)+" ]"
            
                html=html+"\n"+self.BR()+"\n"

        html=html+"\n"+self.Animation_HTML_Body_File_IMG(svgfile)
        outfile=self.Animation_Write_HTML_File(html,"Frames.html")
       
        return outfile
        
       
