from CGI      import *
from HTML     import HTML
from Time     import Time

from Slide        import Slides_Slide
from Menu         import Slides_Menu
from SubMenu      import Slides_SubMenu
from Search       import Slides_Search
from PDF          import Slides_PDF
from Latex        import Slides_Latex

class Slides(
        CGI,HTML,Time,
        
        Slides_Slide,
        Slides_Menu,
        Slides_SubMenu,
        Slides_Search,
        Slides_PDF,
        Slides_Latex,
    ):

    
    CSSs=[ "/Slides.css","/W3.css", ]
    LINKs=[
        {
            "rel":  'stylesheet',
            "href": "/fontawesome-free-5.3.1-web/css/all.css",
        },
    ]
    Scripts=[
        {
             "src": "/Slides.js",
        }
    ]

    App_Name="MySlides"
    DocRoot="/usr/local/Slides"
    FS_Root="/usr/local/Python"
    Title="SmtC: Show me the Code!"
    Titles=[
        "SmtC: Show me the Code",
        "Ole Peter Smith",
        "Instituto de Matem&aacute;tica e Estat&iacute;stica",
        "Universidade Federal de Goi&aacute;s",
        "http://www.olesmith.com.br",
    ]

    Cookies_Obj=None
    
    def __init__(self):

        self.Slides_CGI_Init()
        
        return
    
    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def Slides_CGI_Init(self):
        
        self.CGI_Init()
        pdf=self.CGI_POST("PDF")

        if (pdf==None):
            self.CGI_HTTP_Header_Print()

        if (pdf):
            self.Slides_PDF()
            
        
    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def HTML_Cookies(self):
        if (self.Cookies_Obj!=None):
            return self.Cookies_Obj.HTML_Cookies()
        
        print "Slide Cookies"
        return []
    
    def App_Comment(self,comments):
        if (comments.__class__.__name__!="list"):
            comments=[ comments ]

        html=""
        for comment in comments:
            html=html+"<!-- **** "+self.App_Name+": "+comment+" -->\n"

        return html
    
    
    def Slides_CGI_Path(self):
        path=""
        if (self.__GET__.has_key("Path")):
            path=self.__GET__[ "Path" ]
            while (re.search('%2F',path)):
                path=re.sub('%2F',"/",path)
                
        return path
    
    def Slides_CGI_Paths(self):
        return self.Slides_CGI_Path().split("/")
    
    ##! 
    ##! Generates application main menu.
    ##!
    
    def HTML_Left_Menu(self):
        paths=self.Slides_CGI_Paths()
        paths.pop()

        return self.Slides_Menu_Pre(paths)+self.Slides_Menu(paths)+self.Slide_Cell_Phrase(paths)

    
    ##! 
    ##! Parse ENV vars: Path
    ##!
    
    def HTML_Parse_ENV(self,text,paths):
        path="/".join(["","Slides",]+paths)
        
        m=re.search("\$PATH",text, re.IGNORECASE)
        if (m!=None):
            text=re.sub("\$PATH",path,text,flags=re.IGNORECASE)
        return text
    ##! 
    ##! Simple parsing (on-same-line) for tex commands.
    ##!
    
    def HTML_Parse_Tex(self,tex):
        return tex
    
        texcommands={
            "textit": "I",
            "underline": "U",
            "texttt": "CODE",
            "textbf": "B",
            "chapter":       "H1",
            "section":       "H2",
            "subsection":    "H3",
            "subsubsection": "H4",
        }

        for texcommand in texcommands.keys():
            regexp='\\\\'+texcommand+'\{'+'([^\}]*)'+'\}'

            tag="<"+texcommands[ texcommand ]+">"
            endtag="</"+texcommands[ texcommand ]+">"
            
            m=re.search(regexp,tex)
            if (m!=None):
                tex=re.sub(regexp,tag+m.group(1)+endtag,tex)
                
                
        return tex
    
    ##! 
    ##! Final paring on generated HTML.
    ##!
    
    def HTML_Parse_Html(self,html,paths):
        for n in range(   len(html)   ):
            if (html[n].__class__.__name__=='list'):
                html[n]=self.HTML_Parse_Html(html[n],paths)
            elif (html[n].__class__.__name__=='str'):                
                html[n]=self.HTML_Parse_Tex(html[n])
                html[n]=self.HTML_Parse_ENV(html[n],paths)

        return html
    
    ##! 
    ##! Generates central screen.
    ##!
    
    def HTML_Central_Screen(self):
        paths=self.Slides_CGI_Paths()
        
        html=[]
        html=html+self.Slide_Cell(paths)

        html=self.HTML_Parse_Html(html,paths)

        return html
    ##! 
    ##! Override HTML head scripts, adding MathJax script headers
    ##!
    
    def HTML_Head_Script(self):
        html=[]
        for script in self.Scripts:
            html=html+[ self.XML_Tags("SCRIPT","",script) ]

    
        html=html+[
            self.XML_Tags(
                "SCRIPT",
                [
                    'MathJax = {',
                    '    tex: {',
                    "        inlineMath: "+
                    "[ "+
                    "['$', '$'], "+
                    "['[;',';]'], "+
                    "['\\\\(', '\\\\)'] "+
                    "] ",
                    
                    '    },',
                    '    svg: {',
                    '        fontCache: \'global\'',
                    '    }',
                    '};',
                ]
            ),
            self.XML_Tags(
                "SCRIPT",
                [
                ],
                {
                    'type': '"text/javascript"',
                    'id':   '"MathJax-script"',
                    'src':  '"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"',
                }                
            ),
        ]

        for script in self.Scripts:
            html=html+[ self.XML_Tags("SCRIPT","",script) ]

        return html
