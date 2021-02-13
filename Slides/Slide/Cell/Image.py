import re,glob

class Slides_Slide_Cell_Image():

    def Slide_Cell_Image_Insert(self,content,paths):
        if ( re.search('@Image\s+',content, re.IGNORECASE) ):
            args=re.sub(r'@Image\s+',"",content, flags=re.IGNORECASE)
            args=re.sub(r'^\s+',"",args)
            args=re.compile("\s").split(args)

            filename=""
            if ( len(args)>0 ):
                filename=args[0]

            rpaths=[filename]
            if (not re.search('^/',filename)):
                rpaths=paths+rpaths
                
            if (not re.search('^/Slides/',filename)):
                rpaths=["Slides"]+rpaths
                
            if (not re.search('cgi-bin',filename)):
                subpath="/cgi-bin/Download?File="
                if (re.search('\.tex',filename)):
                    subpath="/cgi-bin/tikz2svg?Src="
                    
                rpaths=[subpath]+rpaths
                
            uri="/".join(rpaths)
            img_options={
                "SRC": uri,
                "STYLE": {
                    "align":            "center",
                    "vertical-align":   "middle",
                    "background-color": "#EEEEEE",
                }
            }

            if ( len(args)>1 ):
                img_options[ "width" ]=args[1]

            if ( len(args)>2 ):
                img_options[ "height" ]=args[2]

                        
            content=[
                self.XML_Tags(
                    "A",
                    self.XML_Tag1("IMG",img_options),
                    {
                        "HREF": uri,
                        "TARGET": "_",
                    }
                )
            ]


        return self.Center(content)
