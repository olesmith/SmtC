import re,glob

class Slides_Slide_Cell_Images():

    def Slide_Cell_Images_Insert(self,content,paths):
        if ( re.search('@Images\s+',content, re.IGNORECASE) ):
            rootpath="/var/www/html/"
            args=re.sub(r'@Images\s+',"",content, flags=re.IGNORECASE)
            args=re.sub(r'^\s+',"",args)
                
            args=re.compile("\s").split(args)

            globpath=""
            if ( len(args)>0 ):
                globpath=args[0]

            ncols=3
            if ( len(args)>1 ):
                ncols=int(args[1])
                    
            options={}
            if ( len(args)>2 ):
                options[ "width" ]=args[2]

                                        
            svgfiles=self.Slide_Cell_Carroussel_Files(paths,rootpath,globpath)

            content=self.HTML_Images_Display(rootpath,globpath,svgfiles,ncols,options)


        return content
