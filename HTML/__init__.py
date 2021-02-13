import time

from XML import XML
from Latex    import Latex


from Tags import HTML_Tags
from Heads import HTML_Heads
from Body import HTML_Body
from Parse import HTML_Parse
from Table import HTML_Table
from Table_Old import HTML_Table_Old

from Carousel import HTML_Carousel
from Images   import HTML_Images
from Icons    import HTML_Icons
from Icon     import HTML_Icon
from JS       import HTML_JS
from Form     import HTML_Form
from Input    import HTML_Input
from Button   import HTML_Button

class HTML(
        XML,Latex,
        
        HTML_Tags,
        HTML_Heads,
        HTML_Body,
        HTML_Parse,
        HTML_Table,
        HTML_Table_Old,
        HTML_Carousel,
        HTML_Images,
        HTML_Icons,
        HTML_Icon,
        HTML_JS,
        HTML_Form,
        HTML_Input,
        HTML_Button,
    ):

    Time_Start=time.time()
    HTML_Messages=[]

    Indent="   "
    
    Cell_Mode=False
    HTML_Version='<!DOCTYPE html>'
    HTML_Icons="/icons"
    HTML_Root="/"
    LINKs=[]
    CSSs=[ "/W3.css","/Poops.css", ]
    METAs=[
        {
            "http-equiv": "Content-type",
            "content": "text/html; charset=utf-8",
        },
        {
            "name": "Autor",
            "content": "Prof. Dr. Ole Peter Smith, IME/UFG",
        },
    ]

    #Names of Methods to call to generate Body matrix/table
    Body_Matrix=[
        [ "Top_Left","Top_Center","Top_Right", ],
        [ "Middle_Left","Middle_Center","Middle_Right", ],
        [ "Bottom_Left","Bottom_Center","Bottom_Right", ],
    ]
    

    #Body table row classes
    Body_Matrix_TR_CSS=[
        "Body_Top","Body_Middle","Body_Bottom"
    ]
    
    #Body table column classes
    Body_Matrix_TD_CSS=[
        "Body_Left","Body_Center","Body_Right",
    ]

    
    #Body_Matrix_TD_Widths=[ "20%","70%","10%" ]
    #Body_Matrix_TR_Heights=[ "20%","70%","10%" ]
    


    HTML_Top_Logos=[
        "/icons/ufg.png",
        "/icons/ufg.png"
    ]
    
    HTML_Bottom_Logos=[
        "/icons/sade_owl.png",
        "/icons/kierkegaard.png",
        "/icons/sade_owl.png"
    ]
    HTML_Middle_Right_Logos=[ 
        {
            "Name": "PooPys",
            "Url": "poop2.png",
            "Height": "",
            "URL": "/cgi-bin/Display",
        },
        {
            "Name": "Python",
            "Url": "python.jpg",
            "Width": "75px",
            "URL": "http://www.python.org",
        },
        {
            "Name": "SVG",
            "Url": "svg.jpg",
            "Width": "75px",
            "URL": "http://www.w3.org/Graphics/SVG",
        },
        {
            "Name": "Latex",
            "Url": "latex.png",
            "Width": "75px",
            "URL": "http://www.latex-project.org",
        },
        {
            "Name": "MathJax",
            "Url": "mathjax.svg",
            "Width": "75px",
            "URL": "http://www.mathjax.org",
        },
        {
            "Name": "W3Schools",
            "Url": "w3.jpg",
            "Width": "75px",
            "URL": "http://www.w3schools.com",
        },
        {
            "Name": "Inkscape",
            "Url": "inkscape.png",
            "Width": "75px",
            "URL": "http://www.inkscape.org",
        },
        {
            "Name": "Gimp",
            "Url": "gimp.jpg",
            "Width": "75px",
            "URL": "http://www.gimp.org",
        },
        {
            "Name": "Geogebra",
            "Url": "geogebra.png",
            "Width": "75px",
            "URL": "http://www.geogebra.org",
        },
    ]
    
    def HTML_Indent(self,n):
        html=""
        for i in range(n):
            html=html+self.Indent

        return html
    
    def HTML_Message_Add(self,msg):
        if (msg.__class__.__name__=="list"):
            msg=self.BR().join(msg)
            
        self.HTML_Messages.append(msg)
    
    def HTML_Exec_Time(self):
        mtime=int(time.time()-self.Time_Start)
        return self.I(str(mtime)+" secs.")
    
    def HTML_Messages_Show(self):
        mtime=int(time.time()-self.Time_Start)

        html=[ self.B("Messages: ") ]
        html=html+[ self.HTML_List(self.HTML_Messages) ]
        html=html+[ self.HTML_Exec_Time() ]
        
        return html
    
    ##!
    ##! Makes sure that options[ "class" ] is set
    ##* make it list
    ##* and add classs to it.
    ##!
    
    def HTML_AddClass(self,classs,options={}):
        roptions=dict(options)
        if (not roptions.has_key("class")):
            roptions[ "class" ]=[]
            
        if (roptions[ "class" ].__class__.__name__!="list"):
            roptions[ "class" ]=[ roptions[ "class" ] ]
        
        roptions[ "class" ].append(classs)
        return roptions
    
    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def HTML_Cookies(self):
        return []
    
    def Run(self):
        #self.CGI_HTTP_Header_Print()
       
        html=[]
        html=html+self.HTML_Header()
        html=html+self.HTML_Body()
        html=html+self.HTML_Tailer()

        print self.HTML_Print(html)
        
        return
    
    ##! 
    ##! Generates HTML Header end section: Just BODY and HTML end tag.
    ##!
    
    def HTML_Tailer(self):
        html=[]
        html=html+[ self.XML_Tag_End("HTML") ]

        return html
    
    ##! 
    ##! Prints HTML list hierarchy.
    ##!
    
    def HTML_Print(self,htmls,level=0):
        return self.XML_Print(htmls,level)
       
    ##! 
    ##! HTML image file add
    ##!
    
    def HTML_Image_Add_If_Exists(self,imagefile,imageurl="",options={}):
        html=[]
        if (self.File_Exists(imagefile)):
            #Keep changes local
            roptions=dict(options)
            roptions[ "src" ]=imageurl
            
            html=[ self.XML_Tag1("IMG",roptions) ]

        return html
       
