import re,glob

class Slides_Slide_Cell_Carousel():    
    def Slide_Cell_Carroussel_Files(self,paths,rootpath,globpath):
        if (re.match('^\@?',globpath)):
            globpath=re.sub('^\@?',"",globpath)
            globpath="/".join(
                [self.DocRoot ]+paths+[globpath]
            )
            
        imgfiles=glob.glob(globpath)

        imgfiles=glob.glob(globpath)
        #print rootpath+globpath,len(imgfiles),"<BR>"

        imgfiles.sort()

        return imgfiles
       
    def Slide_Cell_Carroussel_Insert(self,content,paths,ncarousel):
        if ( re.search('@Carousel\s+',content) ):
            rootpath="/var/www/html/"
            rootpath="/usr/local/"
            args=re.sub(r'@Carousel\s+',"",content, flags=re.IGNORECASE)
            args=re.sub(r'^\s+',"",args)
                
            args=re.compile("\s").split(args)

            globpath=""
            if ( len(args)>0 ):
                globpath=args[0]

            every=1
            if ( len(args)>1 ):
                every=int(args[1])
                    
            delay=200
            if ( len(args)>2 ):
                delay=args[2]

            options={}
            if ( len(args)>3 ):
                options[ "width" ]=args[3]
            if ( len(args)>4 ):
                options[ "height" ]=options[ "width" ]
                options[ "width" ]=args[4]

                        
            imgfiles=self.Slide_Cell_Carroussel_Files(paths,rootpath,globpath)


            for n in range( len(imgfiles) ):
                imgfiles[n]=re.sub(rootpath,"",imgfiles[n])

            content=self.HTML_Carousel_Display(rootpath,globpath,imgfiles,every,options,ncarousel)


        return content
