import re


class Latex_Log():
    ##!
    ##! Detect <use filename> entries in log file.
    ##* Create parallel Doc.Figs.tex with figure entries.
    ##!
   
    def Latex_Log_Use_Files(self,texfile,logfile,echo,clean):
        log=self.File_Read_Lines(logfile)


        figsfile=re.sub('\.tex$',".Figs.tex",texfile)
        
        latex=self.Latex_Log_Use_Files_Latex(texfile,logfile,figsfile,echo)

        if (len(latex)==0):
            return []
        
        self.File_Write(figsfile,latex)
        
        if (echo): print "Running pdflatex on figs file:",figsfile,
        res=self.Latex_Run_pdflatex(figsfile)
        if (echo): print res

        pdffile=re.sub('\.tex',".pdf",figsfile)

            
        self.Latex_Run_After_Move(figsfile,pdffile,echo,clean)

        
        return latex
        
    ##!
    ##! Detect <use filename> entries in log file.
    ##* Create parallel Doc.Figs.tex with figure entries.
    ##!
   
    def Latex_Log_Use_Files_Latex(self,texfile,logfile,figsfile,echo):
        files=self.Latex_Log_Use_Files_Find(logfile)
        
         
        if (len(files)==0):
            if (echo): print "No use (fig) files"
            return []

        latex=[
            "\\documentclass{report}",
            "\\usepackage{graphicx,float}\n",
            "\\newcommand{\\Fig}[2]",
            "{",
            "   \\begin{figure}[H]",
            "       \\centering{\includegraphics{#1}}",
            "       \\caption{#2.}",
            "   \\end{figure}",
            "}\n",


            "\\begin{document}",
            "\n\n",
        ]
        
        for filename in files:
            latex_filename=re.sub('_',"\_",filename)

            latex_line="\\Fig{"+filename+"}{"+latex_filename+"}"
            
            if (echo): print filename
            
            latex.append(latex_line)

        latex=latex+[
            "\n\n",
            "\\end{document}",
        ]
        
        if (echo):
            print len(files)," files written to",figsfile

        return latex
    ##!
    ##!
    ##!
   
    def Latex_Log_Error_Locate(self,log):
        rlog=[]
        include=False

        regex="|".join([
            '! LaTeX\s+(Error|Warning)',
            '! I can.t write on',
            '! Undefined control sequence',
            'Runaway argument?',
        ])
        
        for line in log:
            if (re.search('('+regex+')',line)):
                include=True
                
            if (include):
                rlog.append(line)

        return rlog
        
    ##!
    ##!
    ##!
   
    def Latex_Log_Show(self,texfile,logfile,res,sep="%",width=None):
        log=self.File_Read_Lines(logfile)
        rlog=self.Latex_Log_Error_Locate(log)


        if (width==None): width=len(logfile)+50

        sep=sep*width
        
        text=[
            sep,
            "\tpdflatex logfile: "+logfile,
            "\tReturn code:      "+str(res),
            sep+"\n",
        ]
        
        for n in range(len(log)):
            nn="%03d" % (n+1)
            
            text.append(str(nn)+": "+log[n])
        
        text=text+[
            sep,
            "\tLatex source file: "+texfile,
            "\tReturn code:     "+str(res),
            "\tI think it starts here:     ",
            sep,
        ]
        
       
        for n in range(len(rlog)):
            nn="%02d" % (n+1)
            
            text.append(str(nn)+": "+rlog[n])

            
        text=text+[
            sep,
        ]

        return text

        
    ##!
    ##! Detect <use filename> entries in log file.
    ##* Create parallel Doc.Figs.tex with figure entries.
    ##!
   
    def Latex_Log_Use_Files_Find(self,logfile):
        log=self.File_Read_Lines(logfile)

        files=[]
        for n in range(len(log)):
            regex=re.search('<use\s+([^>]+)',log[n])
            
            if (regex):
                filename=regex.group(1)
                files.append(filename)
                    

        return files
        
