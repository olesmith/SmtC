import re,os

class Slides_Slide_Cell_Exec():
    
    ##!
    ##! Insert output of executed file of code.
    ##
    
    def Slide_Cell_Code_Exec(self,content,paths):
        if ( re.search('@Exec\s+',content, re.IGNORECASE) ):
            args=re.sub(r'@Exec\s+',"",content, flags=re.IGNORECASE)
            args=re.sub(r'^\s+',"",args)
                
            args=re.compile("\s").split(args)

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

                        
            scriptfile=""
            if ( len(args)>0 ):
                scriptfile=args[0]
                command=None
                if (re.search('\.py$',scriptfile) ):
                    command="/usr/bin/python"
                elif (re.search('\.pl$',scriptfile) ):
                    command="/usr/bin/perl"
                elif (re.search('\.php$',scriptfile) ):
                    command="/usr/bin/php"
                elif (re.search('\.sh$',scriptfile) ):
                    command="/bin/bash"

                paths=[self.DocRoot]+paths
                
                #Relative path to script file.
                rscriptfile="/".join(paths)+"/"+scriptfile

                if (not self.File_Exists(rscriptfile)):
                    return "@Exec: "+rscriptfile+" non existent"
                    
                commands=[
                    "cd",
                    "/".join(paths)+";",
                    command,
                    scriptfile,
                ]

                content=self.System_Pipe(commands)
                content=re.sub('\t',"    ",content)
                content=content.split("\n")
                
                if (len(args)>1 and re.search('^\d+$',args[1])):
                    maxlen=int(args[1])
                    if (maxlen<len(content)):
                        content=content[0:maxlen]
                        
                options={
                    "CLASS": 'Code',
                    "id":    re.sub('\.',"",os.path.basename(scriptfile)),
                    "STYLE": {},
                }

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
        
                content=[
                    "\n".join(content),
                    self.Div("Output from: "+command+" "+scriptfile,{ "class": "Code_Title", }),
                ]

        return self.HTML_Frame(content)
