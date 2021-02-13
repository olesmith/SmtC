import re,glob

class Slides_Slide_Cell_Link():
    def Slide_Cell_Command_Detect_Args(self,command,content):
        regexp='@'+command+'{'

        args=[]
        if ( re.search(regexp,content, re.IGNORECASE) ):
            args=re.sub(regexp,"",content, flags=re.IGNORECASE)
            args=re.sub('}\s*$',"",args)
            args=re.compile("}{").split(args)

        return args
    
    def Slide_Cell_Link_Insert(self,content,paths):

        args=self.Slide_Cell_Command_Detect_Args("Link",content)
        
        if ( len(args)>=1):
            filename=args[0]
                    
            title=filename
            if ( len(args)>1 ):
                title=args[1]

            paths=[filename]

            if (not re.search('^http(s)?://',filename)):
                paths=[
                    "/cgi-bin/Download?File=/Slides",
                ]+paths+[filename]
                

            uri="/".join(paths)
            content=[
                self.XML_Tags(
                    "A",
                    title,
                    {
                        "HREF": uri,
                        "TARGET": "_",
                    }
                )
            ]


        return self.Center(content)
