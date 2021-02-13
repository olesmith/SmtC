import re

class Slides_Slide_Cell_Include():
    
    ##!
    ##! Insert output of executed file of code.
    ##
    
    def Slide_Cell_Include(self,content,paths):
        if ( re.search('@Include\s+',content,re.IGNORECASE) ):
            args=re.sub(r'@Include\s+',"",content, flags=re.IGNORECASE)
            args=re.sub(r'^\s+',"",args)
                
            args=re.compile("\s").split(args)

            fname=""
            if ( len(args)>0 ):
                fname="/".join([self.DocRoot]+paths+[args[0]])

                if (self.File_Exists(fname)):
                    content=self.File_Read_Lines(fname)

                    if (re.search('\.tex$',fname)):
                        for n in range(len(content)):
                            if (re.search('documentclass',content[n])):
                                content[n]=""
                            elif (re.search('usepackage',content[n])):
                                content[n]=""
                            elif (re.search('(begin|end)\s*{document}',content[n])):
                                content[n]=""

        return content
