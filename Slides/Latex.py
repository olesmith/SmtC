import os,re


class Slides_Latex():
    chroot="/usr/local/Slides/"

    ##!
    ##! 
    ##!
    
    def Slides_Latex(self):
        return
        latex=self.Slides_Latex_Doc_Latex()

        regexp='input\{([^\{\}]+)\}'
        
        for n in range(len(latex)):
            matches=re.findall(regexp,latex[n])
            if (matches):
                for match in matches:
                    print "Match",match,"<BR>"
                    if (not re.search('\.tex$',match)):
                        
                        latex[n]=re.sub(
                            'input\{'+match+'\}',
                            'input{'+match+'.tex}',
                            latex[n]
                        )
        
        if (latex):
            self.Slides_Latex_Doc_Latex_Run(latex)

    ##!
    ##! 
    ##!
    
    def Slides_Latex_Doc_Latex_Run(self,latex):
        tmp_tex_file=self.Slides_Latex_Doc_Latex_Temp_File_Write(latex)
 
        pdf_file=re.sub('\.tex',".pdf",tmp_tex_file)

        res=self.Latex_Run(tmp_tex_file,pdf_file)
        
        if (self.File_Exists(pdf_file)):
            self.CGI_HTTP_Header_Print(
                "pdf",
                re.sub('\.tex$',".pdf",self.CGI_GET_Text("File"))
            )
            print self.File_Read(pdf_file)

            self.Files_Unlink([pdf_file])
            exit()
            
        self.CGI_HTTP_Header_Print("text")
        print "Nonexistent pdffile:",pdf_file+":",res
        exit()
            
    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def Slides_Latex_Doc_Latex_Temp_File_Write(self,latex):
        tmp_file=self.Slides_Latex_Doc_Latex_Temp_File()
        
        self.File_Write(tmp_file,latex)

        return tmp_file
            
    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def Slides_Latex_Doc_Latex_Temp_Path(self):
        path=self.tmp_path
        if (not os.path.exists(path)):
            os.mkdir(path)

        return path
    
        
    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def Slides_Latex_Doc_Latex_Temp_File(self):
        path=self.Slides_Latex_Doc_Latex_Temp_Path()

        fname=self.CGI_GET_Text("File")
        extension=""
        
        regex=re.search('(\S+)(\.\S+)$',fname)
        if (regex):
            matches=regex.groups()
            fname=matches[0]
            extension=matches[1]

        fname="_".join([
            fname,
            self.Time_Text(),
            str(os.getpid()) #make unique adding pid
        ])+extension

        return "/".join([path,fname])
    
    
        
    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def Slides_Latex_Doc_Latex(self):

        self.Doc_Class=self.CGI_POST_Text(self._Doc_Class_CGI_)
        self.Doc_Class_Options=self.CGI_POST_Text(self._Doc_Class_Options_CGI_)

        if (self.Doc_Class==None):
            self.Doc_Class=self._Doc_Class_Default_

            
        if (self.Doc_Class_Options==None):
            self.Doc_Class_Options=self._Doc_Class_Options_Default_

        latex=self.Slides_Latex_Doc_Class()

        latex=latex+self.Slides_Latex_Doc_Pre_Amble()
        
        latex=latex+["\\begin{document}",]
        
        latex=latex+self.Slides_Latex_Doc_Body()
        
        latex=latex+["\\end{document}",]
        
        return latex
        
    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def Slides_Latex_Doc_Class(self):
        
        docclass=[
            "\\documentclass",
            "[",
            self.Doc_Class_Options,
            "]",
            "{",
            self.Doc_Class,
            "}",
        ]

        return ["".join(docclass)]
    
    ##!
    ##! 
    ##!
    
    def Slides_Latex_Doc_Pre_Amble(self,doinclude=False):
        latex=[]
        
        for pre_amble in self._Doc_Ambles_:
            fname="/".join([
                self._Doc_Ambles_Root_,
                pre_amble
            ])

            file_exists=self.File_Exists(fname)
            if (file_exists and doinclude):
                pre_amble=self.Slides_Latex_Comment(
                    fname+" inserted, start:"
                )+self.File_Read_Lines(fname)+self.Slides_Latex_Comment(
                    fname+" inserted, end."
                )
                
            else:
                pre_amble=[]
                if (not file_exists):
                    pre_amble=["%%!!! Not found: "+fname]
                    
                pre_amble=pre_amble+["\\input{"+fname+"}"]

            latex=latex+pre_amble

        if (len(latex)>0): latex=["","%%! Added:"]+latex+["","%%! Original:"]
        
        latex=latex+self.Slide_Cell_Code_CGI_Pre_Amble_Values()
        
        if (len(latex)>0): latex=latex+["",""]       

        return latex
    ##!
    ##! 
    ##!
    
    def Slides_Latex_Comment(self,comment,leading="%%!",space=" "):
        return [
            leading+space,
            leading+space+comment,
            leading+space,
            "\n",
        ]
    
        
    ##!
    ##! 
    ##!
    
    def Slides_Latex_Doc_Body(self):
        
        latex=self.Slide_Cell_Code_CGI_Body_Values()
        
        return latex
