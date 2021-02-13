import os,glob,re


from Base import *


class HTML_Carousel():
    Delay=200
    Carousel_No=0

        
    ##! 
    ##! Generates Carrousel java script as code.
    ##!
    
    def HTML_Carousel_JS(self,delay,n=1):
        js=[]
        js=js+self.HTML_Carousel_JS_Top(n)
        js=js+self.HTML_Carousel_JS_carousel_Function(delay,n)

        
        return self.XML_Tags("SCRIPT",[ js ])
    
    ##! 
    ##! Generates Carrousel java script top part.
    ##!
    
    def HTML_Carousel_JS_slideIndex(self,n,i):
        return 'slideIndex'+str(i)
    
    ##! 
    ##! Generates Carrousel java script top part.
    ##!
    
    def HTML_Carousel_JS_Top(self,n):
        js=[]
        for i in range(n):
            no=str(i)
            js=js+['var '+self.HTML_Carousel_JS_slideIndex(n,i)+' = 0;',]

        return js+['']


    ##! 
    ##! Generates Carrousel java script function.
    ##!
    
    def HTML_Carousel_JS_carousel_Function(self,delay,n):
        funcname='carousel'
        
        js=[
            funcname+'();',
            '',
            'function '+funcname+'() {',
            self.HTML_Carousel_JS_carousel_Function_Body(n)+[
                '',
                'setTimeout(carousel,'+str(delay)+'); // Change image every delay ms',
            ],
            '}',
        ]

        return js+['']

    ##! 
    ##! Generates Carrousel java script function.
    ##!
    
    def HTML_Carousel_JS_carousel_Function_Body(self,n):
        js=['var i;','',]
        js=js+self.HTML_Carousel_JS_carousel_UnDisplays_Loops(n,'mySlides','Text')
        
        js=js+self.HTML_Carousel_JS_carousel_Update_Indices_Loop(n)
        js=js+self.HTML_Carousel_JS_carousel_Displays_Loops(n)

        return js


    ##! 
    ##! Generates Carrousel java script function.
    ##!
    
    def HTML_Carousel_JS_carousel_UnDisplays_Loop(self,xname,classname):
        
        return [
            'var '+xname+' = document.getElementsByClassName("'+classname+'");',
            'for (i = 0; i < '+xname+'.length; i++) {',
            [
                '  '+xname+'[i].style.display = "none";',
            ],
            '}',
            '',
        ]
    
    ##! 
    ##! Generates Carrousel java script function.
    ##!
    
    def HTML_Carousel_JS_carousel_UnDisplays_Loops(self,n,classname,textclassname):
        js=[]
        for i in range(n):
            js=js+self.HTML_Carousel_JS_carousel_UnDisplays_Loop(
                'x1'+str(i),
                textclassname+str(i)
            )
            
            js=js+self.HTML_Carousel_JS_carousel_UnDisplays_Loop(
                'x2'+str(i),
                classname+str(i)
            )

        return js

    ##! 
    ##! Generates Carrousel java script function.
    ##!
    
    def HTML_Carousel_JS_carousel_Update_Indices_Loop(self,n):
        indexname='slideIndex'
        
        js=[]
        for i in range(n):
            js=js+[
                self.HTML_Carousel_JS_slideIndex(n,i)+'++;',
                'if ('+self.HTML_Carousel_JS_slideIndex(n,i)+' > x2'+str(i)+'.length) {',
                [
                    self.HTML_Carousel_JS_slideIndex(n,i)+'=1;',
                ],
                '}',
                '',
            ]
            
        return js
    
    ##! 
    ##! Generates Carrousel java script function.
    ##!
    
    ##! 
    ##! Generates Carrousel java script function.
    ##!
    
    def HTML_Carousel_JS_carousel_Displays_Loop(self,n,i):
        indexname='slideIndex'

        x1name='x1'+str(i)
        x2name='x2'+str(i)
        return [
            x1name+'['+self.HTML_Carousel_JS_slideIndex(n,i)+'-1].style.display = "block";',
            x2name+'['+self.HTML_Carousel_JS_slideIndex(n,i)+'-1].style.display = "block";', 
        ]

    ##! 
    ##! Generates Carrousel java script function.
    ##!
    
    def HTML_Carousel_JS_carousel_Displays_Loops(self,n):
        indexname='slideIndex'
        
        js=[]
        for i in range(n):
            x1name='x1'+str(i)
            x2name='x2'+str(i)
            
            js=js+self.HTML_Carousel_JS_carousel_Displays_Loop(n,i)
            
        return js









    
        
    ##! 
    ##! Returns Carrousel image src.
    ##!
    
    def HTML_Carousel_Image_SRC(self,svgfile):
        src="/".join( [ self.CGI_Host_Name_Qualified(),"cgi-bin","SVG" ] )
        svgfile=re.sub(self.FS_Root+'/?',"",svgfile)
        return src+"?"+svgfile
    
    ##! 
    ##! Generates Carrousel image entry.
    ##!
    
    def HTML_Carousel_Image(self,n,basepath,globpath,svgfile,args={}):
        #Keep changes local
        rargs=dict(args)
        rargs[ "src"]=self.HTML_Carousel_Image_SRC(svgfile)
        
        rargs[ "title"]=svgfile
        
        url=self.CGI_Query_Path()
        return self.HTML_A(
            "?"+url+"&Browse="+str(n),
            self.XML_Tag_Start("IMG",rargs),
            {},
            "",
            self.HTML_Carousel_Div_ID(basepath,globpath)
        )
    ##! 
    ##! Generates Carrousel image entries.
    ##!
    
    def HTML_Carousel_Images(self,basepath,globpath,svgfiles,args={},every=1,ncarousel=0):
        #Keep changes local
        no=str(self.Carousel_No)
        rargs=dict(args)
        rargs[ "class" ]="mySlides"+str(ncarousel)
        targs=dict(args)
        targs[ "class" ]="Text"+str(ncarousel)
        targs[ "style" ]="font-size: 12px;"


        html=[]
        for n in range( len(svgfiles) ):
            if ( (n % every)==0 ):
                html.append( self.HTML_Carousel_Image(n,basepath,globpath,svgfiles[n],rargs) )
                html.append( self.XML_Tags("DIV",svgfiles[n],targs) )
        
        return html
        
    ##! 
    ##! Returns list of Carrousel files.
    ##!
    
    def HTML_Carousel_Files(self,globpath):
        svgfiles=glob.glob(globpath+regex)

        svgfiles.sort()

        return svgfiles
    
    ##! 
    ##! Generates Carroussel entry (as html)
    ##!
    
    def HTML_Carousel_Generate(self,basepath,globpath,svgfiles,every=1,imgargs={},ncarousel=0):
        n=len(svgfiles)
        m=int(n/every)
        rsvgfiles=[]
        for svgfile in svgfiles:
            if (not re.search('^/',svgfile)):
                rsvgfiles.append(basepath+"/"+svgfile)
        
        html=[]
        html=html+[
            self.HTML_Carousel_Images(basepath,globpath,svgfiles,imgargs,every,ncarousel),
            self.XML_Tags(
                "DIV",
                "Generated: "+self.Time_Show( self.Files_MTime(rsvgfiles) ),
                {
                    "class": "Carousel_Info_Text",
                    "id":    self.HTML_Carousel_Div_ID(basepath,globpath),
                }
            ),
            self.XML_Tags("DIV",str(m)+" of "+str(n)+" images",{"class": "Carousel_Info_Text", }),
            self.XML_Tags("DIV","Base Path: "+basepath,{"class": "Carousel_Info_Text", }),
            self.XML_Tags("DIV","Glob Path: "+globpath,{"class": "Carousel_Info_Text", }),
        ]

        return  html

    ##! 
    ##! Generates Carroussel browsed: Ie shows image and browse menu
    ##!
    
    def HTML_Carousel_Browse(self,n,basepath,globpath,svgfiles,every=1,imgargs={},ncarousel=0):
        while (n>len(svgfiles)):
            n-=len(svgfiles)
            
        if (not re.search('^/',svgfiles[n])):
            rsvgfile=basepath+"/"+svgfiles[n]
        
        html=[]
        html=html+[
            self.HTML_Carousel_Image(n,basepath,globpath,svgfiles[n],imgargs),
            self.XML_Tags(
                "DIV",
                self.HTML_Carousel_Navigation_Menu(n,basepath,globpath,svgfiles),
                {
                    "class": "Carousel_Navegation_Menu",
                }
            ),
            self.XML_Tags(
                "DIV",
                "Generated: "+self.Time_Show( self.Files_MTime([rsvgfile]) ),
                {
                    "class": "Carousel_Info_Text",
                }
            ),
            self.XML_Tags(
                "DIV",
                str(n)+" of "+str(len(svgfiles))+" images",
                {
                    "class": "Carousel_Info_Text",
                }
            ),
            self.XML_Tags(
                "DIV",
                "Base Path: "+basepath,
                {
                    "class": "Carousel_Info_Text",
                }
            ),
            self.XML_Tags(
                "DIV",
                "Glob Path: "+globpath,
                {
                    "class": "Carousel_Info_Text",
                }
            ),
        ]

        return html
        
    ##! 
    ##! Generates Carroussel browsed: Ie shows image and browse menu
    ##!
    
    def HTML_Carousel_Navigation_Menu(self,n,basepath,globpath,svgfiles):
        ns={}
        first="%06d"%0
        last="%06d"%(len(svgfiles)-1)
        prev="%06d"%(n-1)
        curr="%06d"%n
        nexxt="%06d"%(n+1)
        
        ns[ first ]=0
        ns[ last  ]=len(svgfiles)-1
        ns[ prev  ]=n-1
        ns[ curr  ]=n
        ns[ nexxt ]=n+1
        
        for i in range(1, int( len(svgfiles)/10 )):
            ii=10*i
            
            ns[ "%06d"%ii ]=ii

        html=["Navegate Images:"]

        keys=ns.keys()
        keys.sort()
        
        for key in keys:
            i=ns[key]
            html.append(
                self.HTML_Carousel_Navigation_Item(
                    n,
                    basepath,globpath,
                    svgfiles,
                    i
                )
            )
        html=html+[
            self.BR(),
            self.A(
                "?"+self.CGI_Query_Path(),
                "Return to Carousel",
                self.HTML_Carousel_Navigation_Item_Options(n,basepath,globpath,svgfiles,i),
                "Return to Carousel Animation",
                self.HTML_Carousel_Div_ID(basepath,globpath)
            )
        ]

        return html
 
    ##! 
    ##! 
    ##!
    
    def HTML_Carousel_Navigation_Item_Name(self,n,basepath,globpath,svgfiles,i):
        name=""
        if (i==0):
            name="&lt;&lt;"
            
        elif (i==n-1):
            name="&lt;"
            
        elif (i==n+1):
            name="&gt;"
            
        elif (i==len(svgfiles)-1):
            name="&gt;&gt;"
            
        else:
            name=str(i)

        return name

    ##! 
    ##! 
    ##!
    
    def HTML_Carousel_Navigation_Item_Title(self,n,basepath,globpath,svgfiles,i):
        name=self.HTML_Carousel_Navigation_Item_Name(
            n,
            basepath,globpath,
            svgfiles,
            i
        )

        return "Image no: "+name+": "+svgfiles[i]

    
    ##! 
    ##! 
    ##!
    
    def HTML_Carousel_Navigation_Item_Options(self,n,basepath,globpath,svgfiles,i):
        options={}
        if (i==n):
            options={
                "class": "Carousel_Navegation_Active",
            }

        return options

    
     ##! 
    ##! 
    ##!
    
    def HTML_Carousel_Navigation_Item_URL(self,n,basepath,globpath,svgfiles,i):
        return "?"+self.CGI_Query_Path()+"&Browse="+str(i)

    
        
    ##! 
    ##! 
    ##!
    
    def HTML_Carousel_Navigation_Item(self,n,basepath,globpath,svgfiles,i):
        return self.A(
                self.HTML_Carousel_Navigation_Item_URL(n,basepath,globpath,svgfiles,i),
                self.HTML_Carousel_Navigation_Item_Name(n,basepath,globpath,svgfiles,i),
                self.HTML_Carousel_Navigation_Item_Options(n,basepath,globpath,svgfiles,i),
                self.HTML_Carousel_Navigation_Item_Title(n,basepath,globpath,svgfiles,i),
                self.HTML_Carousel_Div_ID(basepath,globpath)
            )

                
    ##! 
    ##! Generates Carroussel entry (as html)
    ##!
    
    def HTML_Carousel_Div_ID(self,basepath,globpath):
        return re.sub('[^A-Za-z0-9]+',"",globpath)
    
    ##! 
    ##! Generates Carroussel entry (as html)
    ##!
    
    def HTML_Carousel_Display(self,basepath,globpath,svgfiles,every=1,imgargs={},ncarousel=0):
        browse=self.CGI_POST("Browse")

        div_id=self.HTML_Carousel_Div_ID(basepath,globpath)
        
        
        html=[]
        if (not browse):
            html=self.HTML_Carousel_Generate(
                basepath,globpath,
                svgfiles,
                every,imgargs,ncarousel
            )
        else:
            html=self.HTML_Carousel_Browse(
                int(browse),
                basepath,globpath,
                svgfiles,
                every,imgargs,ncarousel
            )
        return self.XML_Tags("SPAN",html,{"id":  div_id,});
