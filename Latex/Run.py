import re


from Timer import Timer

class Latex_Run():
    ##!
    ##!
    ##!
   
    def Latex_Clean_Extensions(self):
        return [
            "tex",
            "log","bib.log","aux",
            "lot","lof",
            "nav","out","snm","toc",
            "Figs.tex"
        ]
        
    ##!
    ##!
    ##!
   
    def Latex_Run(self,texfile,pdfresfile=None,echo=False,clean=True):
        path=self.File_Path(texfile)

        pdffile=re.sub('\.tex',".pdf",texfile)
        logfile=re.sub('\.tex',".log",texfile)
        auxfile=re.sub('\.tex',".aux",texfile)
        lotfile=re.sub('\.tex',".lot",texfile)
        loffile=re.sub('\.tex',".lof",texfile)
        rlogfile=re.sub('\.log$',".bib.log",logfile)

        #Filename without extension .tex
        rtexfile=re.sub('\.tex$',"",texfile)
        
        #self.CGI_HTTP_Header_Print("text")
        if (echo): print "Running pdflatex:",

        latex_times=2
        latex_bibs=True
        if (re.search('\.tikz\.tex$',texfile)):
            latex_times=1
            latex_bibs=False
        
        res=None
        bres=True
        for i in (1,latex_times):

            time=Timer("Processing "+texfile+": "+str(i),echo)

            res=self.Latex_Run_pdflatex(texfile)
            
            #Don't rerun on error
            if (res): break

            if (latex_bibs):
                bres=self.Latex_Run_bibtex(texfile)
                    
        if (echo): print res,bres

        #res,bres: Sucess: 0, Failure: 1
        if (res or self.__Log__):
            self.CGI_HTTP_Header_Print("text")

            print "\n".join(
                self.Latex_Log_Show(texfile,logfile,res)
                +
                self.Latex_Show(texfile)
            )
            
        if (self.__Figs__):
            self.Latex_Log_Use_Files(texfile,logfile,echo,clean)

        #Error running pdflatex, exit
        if (res): exit(1)


        self.Latex_Run_After_Move(texfile,pdfresfile,echo)


            
        return res

    ##!
    ##!
    ##!
   
    def Latex_Run_After_Move(self,texfile,pdfresfile,echo=False,clean=True):
        pdffile=re.sub('\.tex',".pdf",texfile)
        clean_extensions=self.Latex_Clean_Extensions()
        
        clean_files=[]
        stripped_name=re.sub('\.tex$',"",texfile)
            
        for extension in clean_extensions:
            clean_files.append(stripped_name+"."+extension)
                
        if (clean):
            self.Files_Unlink(clean_files,echo)
        elif (echo):
            print "\t"+"\n\t".join(clean_files),"\n left intact"
        
        #Move back generated files
        if (pdfresfile!=None and self.File_Exists(pdffile)):
            if (pdfresfile!=pdffile):
                self.File_Rename(pdffile,pdfresfile,echo)
                for ext in clean_extensions:
                    if (ext=="tex"): continue
                    
                    filename=re.sub('pdf$',ext,pdffile)
                    
                    if (self.File_Exists(filename)):
                        rfilename=re.sub('pdf$',ext,pdfresfile)
                        self.File_Rename(filename,rfilename,echo)
                             
    
    ##!
    ##!
    ##!
   
    def Latex_Run_After_Save(self,texfile,latex,pdfresfile,echo=False,clean=True):
        self.File_Write(texfile,latex,echo)

        return self.Latex_Run(
            texfile,
            pdfresfile,
            echo,clean
        )
    ##!
    ##!
    ##!
   
    def Latex_Run_pdflatex(self,texfile):
        logfile=re.sub('\.tex',".log",texfile)

        return self.System_Exec([
            self.pdflatexbin,
            "-halt-on-error",
            "-interaction nonstopmode",
            "-output-directory",
            self.tmp_path,
            texfile,
            ">",
            logfile,
            #"2>&1"
        ])
    
    ##!
    ##!
    ##!
   
    def Latex_Run_bibtex(self,texfile):
        logfile=re.sub('\.tex',".bib.log",texfile)

        return self.System_Exec([
            self.pdflatexbin,
            "-output-directory",
            self.tmp_path,
            texfile,
            ">",
            logfile,
            #"2>&1"
        ])
            
    ##!
    ##!
    ##!
   
    def Latex_Show(self,texfile,sep="#",width=None):
        latex=self.File_Read_Lines(texfile)

        nchars=0
        for tex in latex: nchars+=len(tex)

        if (width==None): width=len(texfile)+10
        
        sep=sep*width

        text=[
            sep,
            "\tLatex source file: "+texfile,
            "\tNo of lines/chars: %d, %d chars" % (len(latex),nchars),
            sep,
        ]
        
        for n in range(len(latex)):
            nn="%03d" % (n+1)
            
            text.append(str(nn)+": "+latex[n])
        text.append(sep)

        return text
        
