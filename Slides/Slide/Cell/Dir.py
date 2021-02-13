import re,os

class Slides_Slide_Cell_Dir():
    
    ##!
    ##! Insert output of executed file of code.
    ##
    
    def Slide_Cell_Code_Dir(self,content,paths):
        if ( re.search('@Dir\s+',content, re.IGNORECASE) ):
            args=re.sub(r'@Dir\s+',"",content, flags=re.IGNORECASE)
            args=re.sub(r'^\s+',"",args)
                
            args=re.compile("\s").split(args)
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
                    
                content=[
                    "\n".join(content),
                    self.Div("Output from: "+command+" "+scriptfile,{ "class": "Code_Title", }),
                ]

        return self.HTML_Frame(content)
