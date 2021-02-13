import re,os

from System import System

from Carousel      import Slides_Slide_Cell_Carousel
from Code          import Slides_Slide_Cell_Code
from Exec          import Slides_Slide_Cell_Exec
from Phrase        import Slides_Slide_Cell_Phrase
from Subdirs       import Slides_Slide_Cell_Subdirs
from Latex         import Slides_Slide_Cell_Latex
from Curve2        import Slides_Slide_Cell_Curve2
from Image         import Slides_Slide_Cell_Image 
from Images        import Slides_Slide_Cell_Images 
from List          import Slides_Slide_Cell_List 
from Include       import Slides_Slide_Cell_Include
from Link          import Slides_Slide_Cell_Link

class Slides_Slide_Cell(
        System,
        Slides_Slide_Cell_Carousel,
        Slides_Slide_Cell_Code,
        Slides_Slide_Cell_Exec,
        Slides_Slide_Cell_Phrase,
        Slides_Slide_Cell_Subdirs,
        Slides_Slide_Cell_List,
        Slides_Slide_Cell_List,
        Slides_Slide_Cell_Latex,
        Slides_Slide_Cell_Image,
        Slides_Slide_Cell_Images,
        Slides_Slide_Cell_Include,
        Slides_Slide_Cell_Link,
        Slides_Slide_Cell_Curve2,
):
    ##!
    ##! Generate the center/middle slide cell.
    ##!
    
    def Slide_Cell(self,paths):
        html=[ self.Anchor("TOP") ]
        html=html+self.Slide_Cell_Titles(paths)

        contents=self.Slides_Search(
            paths
        )+self.Slide_Cell_Contents_Parse(
            paths,
            self.Slide_Contents_Get(paths)
        )

        contents=contents+self.Slide_Cell_Items_List(paths)
            
        contents=contents+self.Slide_Cell_Tail(paths)
        return self.Div(
            self.Slide_Cell_Navigator_Menues(paths,contents),
            { "class": 'Slide_Cell', }
        )

    ##!
    ##! Titles recursively downward, from the basepath, untill paths.
    ##!
    
    def Slide_Cell_Titles(self,paths):
        hlevel=1
        html=[]
        
        tpaths=[]
        for path in paths:
            tpaths.append( path )
            title=self.Slide_Title_Get(tpaths)
            html.append( self.H(hlevel,title) )

            hlevel+=1
        return html

    ##!
    ##! Titles recursively downward, from the basepath, untill paths.
    ##!
    
    def Slide_Cell_Tail(self,paths):
        path=self.Slides_Menu_Path(paths)
        fname="/".join([path,"Tail.html"])

        contents=[]
        if (self.File_Exists(fname)):
            contents=self.File_Read_Lines(fname)

        return self.Slide_Cell_Contents_Parse(paths,contents)
    
    ##!
    ##! Titles recursively downward, from the basepath, untill paths.
    ##!
    
    def Slide_Cell_Items_List(self,paths):
        return []
        path=self.Slides_Menu_Path(paths)

        files=self.Path_Files(path,'^\d+\S*\.(html|tex)$')

        hlist=[]
        for fname in files:
            contents=self.File_Read_Lines(fname)

            hlist.append(
                self.Slide_Cell_Contents_Parse(paths,contents)
            )

        return self.HTML_List(hlist,"UL")

    
    ##!
    ##! Parse contents, must be a list of strings
    ##!
    
    def Slide_Cell_Contents_Parse(self,paths,contents):
        ncarousels=0
        delay=500

        if (contents.__class__.__name__=='str'):
            contents=[contents]

        for n in range( len(contents) ):

            contents[n]=self.Slide_Cell_Item_Line_Parse(paths,contents[n])
            
            if ( re.search('\s*@Carousel\s+',contents[n]) ):
                args=re.sub(r'@Carousel\s+',"",contents[n])
                args=re.sub(r'^\s+',"",args)
                
                args=re.compile("\s").split(args)
                if ( len(args)>2 ):
                    delay=args[2]
                    
                contents[n]=self.Slide_Cell_Carroussel_Insert(
                    contents[n],
                    paths,
                    ncarousels
                )
                ncarousels+=1
                


            elif ( re.search('\s*@Code\s+',contents[n], re.IGNORECASE) ):
                 contents[n]=self.Slide_Cell_Code_Insert(contents[n],paths)
                 
            elif ( re.search('\s*@Exec\s+',contents[n], re.IGNORECASE) ):
                 contents[n]=self.Slide_Cell_Code_Exec(contents[n],paths)
                 
            elif ( re.search('\s*@SubdirsList\s*(\S*)',contents[n], re.IGNORECASE) ):
                 contents[n]=self.Slide_Cell_SubdirList(contents[n],paths)
                 
                 
            elif ( re.search('\s*@(List|Items)',contents[n], re.IGNORECASE) ):                
                contents[n]=self.Slide_Cell_List_Insert(contents[n],paths)
                 
            elif ( re.search('\s*@Latex',contents[n], re.IGNORECASE) ):
                 contents[n]=self.Slide_Cell_Latex(contents[n],paths)
                 
            elif ( re.search('\s*@Curve2',contents[n], re.IGNORECASE) ):
                 contents[n]=self.Slide_Cell_Curve2(contents[n],paths)

            elif ( re.search('\s*@Image\s+',contents[n], re.IGNORECASE) ):                
                contents[n]=self.Slide_Cell_Image_Insert(contents[n],paths)

            elif ( re.search('\s*@Link',contents[n], re.IGNORECASE) ):                
                contents[n]=self.Slide_Cell_Link_Insert(contents[n],paths)

            elif ( re.search('\s*@Images\s+',contents[n], re.IGNORECASE) ):                
                contents[n]=self.Slide_Cell_Images_Insert(contents[n],paths)
                
            elif ( re.search('\s*@Include\s+',contents[n], re.IGNORECASE) ):                
                contents[n]=self.Slide_Cell_Include(contents[n],paths)
                
            elif ( re.search('\s*@Link',contents[n], re.IGNORECASE) ):                
                contents[n]=self.Slide_Cell_Link_Insert(contents[n],paths)
                
            
        if (ncarousels>0):
            contents=contents+self.HTML_Carousel_JS(delay,ncarousels)
            contents=self.XML_Tags(
                "DIV",
                contents,
                { "class": "w3-content w3-section" }
            )
            
        return contents

    ##!
    ##! Scan latexstyle {}'s arguments.
    ##!
    
    def Arguments_Scan(self,content):
        l=0
        args=[]
        comps=re.split(r'}{',content)

        comp=""
        for comp in comps:
            comp=re.sub(r'^[^{}]*{',"",comp)
            comp=re.sub(r'}[^{}]*$',"",comp)

            comp=re.sub('^\s*',"",comp)
            comp=re.sub('\s*$',"",comp)
            
            args.append(comp)

            
        return args
    
    ##!
    ##! Titles recursively downward, from the basepath, untill paths.
    ##!
    
    def Slide_Cell_Item_Line_Parse(self,paths,content):

        regexp='@URL'
        reobj=re.search(regexp+'{.*}',content)
        
        if ( reobj ):
            args=self.Arguments_Scan(content)

            if (len(args)>0):
                link=args[0]

                name=link
                if (re.search('^/',link)):
                    name=os.path.basename(link)
                    
                if (len(args)>1):
                    name=args[1]
                
                options={}
                if (not re.search('^http',link)):

                    if (not re.search('^/',link)):
                        link="/".join(
                            ["/Slides"]+paths+[""]
                        )+link
                    
                    link="/cgi-bin/Download?File="+link

                options[ "TARGET"]='_blank_'
                options[ "HREF"]=link
                options[ "TITLE"]="Access "+args[0]
                
                rcontent=self.XML_Tag_Start("A",options)+name+self.XML_Tag_End("A")

                content=re.sub(regexp+'{.*}',rcontent,content)
                
        return content
