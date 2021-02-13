import re,os

from Edit      import Slide_Cell_Code_Edit
from Doc_Class import Slide_Cell_Code_Doc_Class
from Ambles    import Slide_Cell_Code_Ambles
from Body      import Slide_Cell_Code_Body
from CGI       import Slide_Cell_Code_CGI

class Slides_Slide_Cell_Code(
        Slide_Cell_Code_Edit,
        Slide_Cell_Code_Doc_Class,
        Slide_Cell_Code_Ambles,
        Slide_Cell_Code_Body,
        Slide_Cell_Code_CGI,
):
    _Doc_Class_Default_="standalone"
    _Doc_Class_CGI_="Doc_Style"
    
    _Doc_Class_Options_Default_=""
    _Doc_Class_Options_CGI_="Doc_Options"
    
    _Doc_Ambles_Post_Default_=[]
    _Doc_Ambles_Pre_Default_=[]
    _Doc_Ambles_Pre_CGI_="Doc_Pre_Amble"

    _Doc_Body_Default_=[]
    _Doc_Body_CGI_="Doc_Body"

    _Doc_Ambles_Root_="/usr/local/Slides/PreAmbles"
    
    _Doc_Ambles_=[
        #"Base.tex",
        "TikZ.tex",
        #"Listings.tex",
        #"NewCommands.tex",
        #"Theorems.tex",
        #"MathOperators.tex",
    ]
    
    ##!
    ##! Insert file of code.
    ##!
    
    def Slide_Cell_Code_Lines_Read(self,scriptfile):
                
        contents=self.File_Read_Lines(scriptfile)

        #Leading empty lines
        first_not_empty=-1
        for n in range(len(contents)):
            if (re.search('\S',contents[n])):
                first_not_empty=n
                break
                
        #Trailing empty lines
        last_not_empty=0
        for n in range(len(contents)-1,0,-1):
            if (re.search('\S',contents[n])):
                last_not_empty=n
                break

        rcontents=[]
        for n in range( first_not_empty,last_not_empty+1):
            rcontents.append(contents[n])
        
        rcontents=self.Slide_Cell_Code_Parse(scriptfile,rcontents)
        
        return rcontents

        
    ##!
    ##! Do parsing for special types based on file extension:
    ##!
    ##! html|svg: change < resp. > to &lt; resp. &gt;
    ##* tex: replace \input's with links,
    ##* activating SMTC including addicional code field.
    ##!
    
    def Slide_Cell_Code_Parse(self,scriptfile,contents):
        
        if (re.search('.(html|svg)$',scriptfile)):
            self.Slide_Cell_Code_Parse_XML(scriptfile,contents)
        elif (re.search('.tex$',scriptfile)):
            self.Slide_Cell_Code_Parse_Tex(scriptfile,contents)

            
        return contents
    
    ##!
    ##! Parse contents as tex.
    ##!
    
    def Slide_Cell_Code_Parse_Tex(self,scriptfile,contents):
        url=self.CGI_Query_Path()
        for n in range( len(contents) ):
            reg=re.search('\\input\{([^\{\}]+)\}',contents[n])
            if (reg):
                fname=reg.group(1)
                if (not re.search('\.tex$',fname)):
                    fname=fname+'.tex'
                    
                fname=re.sub('\\\\TiKZPath',"/usr/local/tikz",fname)
                
                link=self.A(
                    "?"+url+"&Src="+fname,
                    '\input{'+re.sub('\.tex$',"",fname)+'}',
                    {},
                    "",
                    re.sub('\.',"",os.path.basename(fname)) #anchor
                )

                #Why is two \\ necessary?
                contents[n]=re.sub(
                    '\\\\input\{(\S+)\}',
                    link,
                    contents[n]
                )

            #\usetkzobj{all} error!
            reg=re.search('\\usetkzobj',contents[n])
            if (reg):
                contents[n]=re.sub(
                    '\\\\usetkzobj',
                    "%%!\n"+
                    "%%! For older versions of package tkz-euclide\n"+
                    "%%! you may need uncomment the following line:\n"+
                    "%   \\usetkzobj",
                    contents[n]
                )+"\n%%!\n"

            regex='\s*'.join([
                '\\\\pgfmathparse\{(.+)\}',
                '\\\\let(\S+)',
                '\\\\pgfmathresult'
            ])

            reg=re.search(regex,contents[n])
            while (reg):
                reg=re.search(regex,contents[n])
                expr=reg.group(1)
                while (re.search('\\\\',expr)):
                    expr=re.sub('\\\\',"&#92;",expr)
                                    
                tikzmath="\\\\tikzmath{\\"+reg.group(2)+"="+expr+";}"
                
                contents[n]=re.sub(
                    regex,
                    tikzmath,
                    contents[n]
                )
                reg=re.search(regex,contents[n])
                
            
        return contents

    ##!
    ##! Parse contents as xml (html|svg).
    ##!
    
    def Slide_Cell_Code_Parse_XML(self,scriptfile,contents):
        for n in range( len(contents) ):
            contents[n]=re.sub('<',"&lt;",contents[n])
            contents[n]=re.sub('>',"&gt;",contents[n])
                
        return contents

    ##!
    ##! Insert file of code.
    ##!
    
    def Slide_Cell_Code_Insert(self,content,paths,options={}):
        html=[]
        
        if ( re.search('@Code\s*',content, re.IGNORECASE) ):

            args=re.sub(r'@Code\s*',"",content, re.IGNORECASE)
            args=re.sub(r'^\s+',"",args)
                
            args=re.compile("\s").split(args)

            scriptfile=""
            if ( len(args)>0 ):
                #Name of script file
                scriptfile=args[0]

            content=self.Slide_Cell_Code_File(
                content,scriptfile,paths,
                args,options={}
            )
            
        src_file=self.CGI_POST("Src")
        if (src_file!=None):
            basename=os.path.dirname(scriptfile)
            if (re.search('\\TiKZPath',src_file)):
                src_file=re.sub(
                    '\\TiKZPath',
                    "/usr/local/tikz",
                    src_file
                )
                

            content=content+[
                self.Div(
                    "Showing "+src_file+":",
                    {
                        "id": re.sub('\.',"",os.path.basename(src_file)),
                    }
                ),
            ]

            content=content+self.Slide_Cell_Code_File(
                content,
                src_file,
                paths
            )

        return content
 
    ##!
    ##! Insert file of code.
    ##!
    
    def Slide_Cell_Code_File_Type(self,scriptfile,paths):
        #Code type from extension
        codetype="??"+scriptfile
        if (re.search('\.py$',scriptfile) ):
            codetype="Python"
        elif (re.search('\.html$',scriptfile) ):
            codetype="HTML"
        elif (re.search('\.pl$',scriptfile) ):
            codetype="Perl"
        elif (re.search('\.php$',scriptfile) ):
            codetype="PHP"
        elif (re.search('\.sh$',scriptfile) ):
            codetype="Shell Script"
        elif (re.search('\.svg$',scriptfile) ):
            codetype="SVG"
        elif (re.search('\.tikz.tex$',scriptfile) ):
            codetype="TiKZ"
        elif (re.search('\.tex$',scriptfile) ):
            codetype="LaTeX"

        if (codetype=="LaTeX"):
            if (self.Latex_TikZ_Should(
                    "/".join([self.DocRoot]+paths+[scriptfile])
            )):
                codetype="TiKZ"

        return codetype

    ##!
    ##! Insert file of code.
    ##!
    
    def Slide_Cell_Code_File(self,content,scriptfile,paths,args=[],options={}):
                    
        #Relative path to script file.
        rscriptfile=scriptfile

        if (not re.search('^/',rscriptfile)):
            rscriptfile="/".join(
                [self.DocRoot]+paths+[scriptfile]
            )

        if (self.File_Exists(rscriptfile+".tex")):
            scriptfile=scriptfile+".tex"
            rscriptfile=rscriptfile+".tex"

        if (not self.File_Exists(rscriptfile)):
            if (re.search('@Code',content)):
                content=re.sub('@Code\s',"",content)
                content=re.sub('\s',"&nbsp;",content)

            return [
                self.XML_Tags(
                    "CODE",
                    content,
                    {
                        "CLASS": "Code",
                    }
                ),
                "<BR>"
            ]
        
        content=self.Slide_Cell_Code_Lines_Read(rscriptfile)

        rargs=[]

        height=None
        width=None
                
        if (len(args)>1):
            for i in range(1,len(args)):
                if (re.search('^height=\d+',args[i])):
                    height=re.sub('^height=',"",args[i])
                elif (re.search('^width=\d+',args[i])):
                    width=re.sub('^width=',"",args[i])
                else:
                    rargs.append(args[i])


        #More arguments in args: name of functions to include.
        if (len(rargs)>0):

            content=self.Slide_Cell_Code_File_Index(
                scriptfile,content,rargs
            )
            
        options.update({
            "CLASS": 'Code',
            "id":    re.sub('\.',"",os.path.basename(scriptfile)),
        })

        if (not "STYLE" in options.keys()):
            options[ "STYLE" ]={}

        if (height!=None):
            options[ "STYLE" ][ "HEIGHT" ]=height
            options[ "STYLE" ][ "overflow-y" ]="scroll"
        if (width!=None):
            options[ "STYLE" ][ "WIDTH" ]=width
            options[ "STYLE" ][ "overflow-x" ]="scroll"

        code_options={
            "CLASS": 'Code',
        }

        #No newline to prevent newline after start tag
        #As it causes the browser to start text one line below
        
        content=self.XML_Tags_No_New_Line(
            "CODE",
            content,
            code_options
        )
        content=self.XML_Tags(
            "PRE",
            content,
            code_options
        )
        content=self.XML_Tags(
            "DIV",
            content,
            options
        )
        
        codetype=self.Slide_Cell_Code_File_Type(scriptfile,paths)

        
        
        #Format contents.
        content=[
            self.Div(
                self.Slide_Cell_Code_File_Info(scriptfile,paths,args),
                {
                    "class": "Code_Title",
                }
            ),
            "\n".join(content),
       ]

        return self.Slide_Cell_Code_Edit(content,scriptfile,paths,args)

    ##!
    ##! File info entry for file
    ##!
    
    def Slide_Cell_Code_Edit(self,content,scriptfile,paths,args=[]):
        
        return [
            self.Slide_Cell_Code_Edit_Frame(
                scriptfile,paths,args
            ),
            self.HTML_Frame(content),
        ]

    
    ##!
    ##! File info entry for file
    ##!
    
    def Slide_Cell_Code_File_Info(self,scriptfile,paths,args=[]):
                    
        codetype=self.Slide_Cell_Code_File_Type(scriptfile,paths)

        info=[
            codetype+" Listing: "+scriptfile+".",
        ]

        titles={}
        names={}
        if (codetype=="TiKZ"):
                
            titles={
                "pdf": "PDF",
                "svg": "SVG",
                "png": "PNG",
                "zip": "ZIP (Under Construction)",
            }
            names={
                "pdf": "PDF",
                "svg": "SVG",
                "png": "PNG",
                "zip": "ZIP*",
            }

        elif (codetype=="LaTeX"):
            titles={
                "pdf": "PDF",
                "zip": "ZIP (Under Construction)",
            }
            names={
                "pdf": "PDF",
                "zip": "ZIP*",
            }
            
        cgi="/cgi-bin/tikz2"
        if (codetype=="LaTeX"):
            cgi="/cgi-bin/latex2"
                
        scriptfile="/".join(
            [
                "Slides"
            ]+paths+[
                scriptfile,
            ]
        )

        keys=titles.keys()
        keys.sort()
        for key in keys:
            info.append(
                self.HTML_A(
                    cgi+key+"?Src="+scriptfile,
                    names[ key ],
                    {},
                    titles[ key ]
                )
            )
            info.append("&nbsp;")

        #info.append(
        #    self.Slide_Cell_Code_Doc_Span("Edit")
        #)
        
        return info
    
    ##!
    ##! File info entry for file
    ##!
    
    def Slide_Cell_Code_File_Index(self,scriptfile,contents,rargs):
        function_prefix="def"
        if (re.search('\.php$',function_prefix)):
            function_prefix="function"

        line_nos=[]
        functions={}
        for n in range(len(contents)):
            if (re.search(function_prefix+'\s+',contents[n])):
                function=re.sub(function_prefix+'\s+',"",contents[n])
                function=re.sub('\(.*',"",function)
                function=re.sub('^\s+',"",function)
                function=re.sub('\s+$',"",function)

                functions[ function ]=n
                line_nos.append(n)


        lines=[]
        for function in rargs:
            if (functions.has_key(function)):
                n=functions[ function ]

                i=-1
                while (i<len(line_nos)):
                    i+=1
                    m=line_nos[i]
                    if (m>n): break

                lines=lines+contents[n:m]
        
        return lines
        
                    
