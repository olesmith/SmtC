import re,sys,os,time

class Latex_Process():
    ##!
    ##! 
    ##!
   
    def Latex_Process_Files(self):
        self.Latex_Args_Init()

        tex_files=self.Latex_Args_Tex_Files()
        
        more_than_one=False
        if (len(tex_files)>1): more_than_one=True

        n=0
        for tex_file in tex_files:
            if (self.File_Exists(tex_file)):
                n+=1
                self.Time=time.time()
                
                self.Latex_Process_File(more_than_one,tex_file,n)
            else:
                print "No such file: ",tex_file

    ##!
    ##! 
    ##!
   
    def Latex_Process_File(self,more_than_one,tex_file,n):
        path=self.Latex_Process_File_Path(tex_file)
        pdf_out_file=self.Latex_Process_File_PDF(tex_file)
        
        if (not self.File_Exists(tex_file)):
            System_Error_And_Die([
                "No such file: "+tex_file,
                sys.argv[0]+",usage syntax:",
                "\t"+sys.argv[0]+"file.tikz.tex"
            ])
            
        dest_time=self.File_MTime(pdf_out_file)
        
        #Generate
        self.Latex_Args_Message("Latex_Process_File:",tex_file)
        
        tikz=False
        if (re.search('tikz\.tex$',tex_file)):
            tikz=True

            
        #Generate document parts
        latex=self.Latex_Document(tex_file)

        files=self.Latex_Inputs(tex_file,latex)
        
        self.Latex_Args_Message("Files:","\t".join(files))
        should=self.System_Make_Test(files,[pdf_out_file])


        
        res=-1
        if (self.Latex_Args_Force() or should):
            #Run LaTex
            tmp_tex_file="/".join([
                self.tmp_path,
                re.sub(
                    '\.tikz\.tex',
                    ".tex",
                    self.File_BaseName(tex_file)
                )
            ])

            if (self.CGI_Is()):
                os.chdir(path)

                
            res=self.Latex_Run_After_Save(
                tmp_tex_file,
                latex,
                pdf_out_file,
                self.Latex_Args_Verbose(),self.Latex_Args_Clean()
            )

            if (self.__Figs__):
                #Move back Figs PDF
                figsfile=re.sub('\.tex$',".Figs.pdf",tmp_tex_file)
                rpdffile=re.sub('\.tex$',".Figs.pdf",tex_file)

                self.File_Rename(figsfile,rpdffile,self.Latex_Args_Verbose())
                
                #Move back Figs tex
                #figsfile=re.sub('\.tex$',".Figs.tex",tmp_tex_file)
                #rpdffile=re.sub('\.tex$',".Figs.tex",tex_file)

                #self.File_Rename(figsfile,rpdffile,self.Latex_Args_Verbose())
                
                
            
        elif (self.Latex_Args_Verbose()):
            print self.Latex_Process_File_PDF(tex_file),
            print "is newer than",tex_file," - omitted"

        if (not self.Latex_Args_Silent()):
            if (more_than_one):
                print str(n),
                
            print pdf_out_file,
            if (res==0):
                if (dest_time>0): print "updated",
                else:             print "created",

                time_elapsed=time.time()-self.Time
                print str(time_elapsed)+"s"
            else:                 print "uptodate"
                    
        res=0
        if (self.File_Exists(pdf_out_file)):
            #Move back from tmp dir, if necessary
            #self.Latex_Process_2_PDF(tex_file,tmp_tex_file)
            
            res=res+self.Latex_Process_2_SVG(tex_file)
                        
            res=res+self.Latex_Process_2_PNG(tex_file)

        if (res>=0):
            res=self.Latex_Process_CGI_Send(tex_file)

        return res

    ##!
    ##! Path to tex_file
    ##!
   
    def Latex_Process_File_Path(self,tex_file):
        path=self.File_Path(tex_file)
        if (path): path=path+"/"
    
        return path
        
    ##!
    ##! Name of PDF file from tex_file
    ##!
   
    def Latex_Process_File_PDF(self,tex_file,ext="pdf"):
        return self.Latex_Process_File_Path(
            tex_file
        )+re.sub(
            '(\.tikz)?\.tex',
            "."+ext,
            self.File_BaseName(tex_file)
        )
    ##!
    ##! Name of PDF file from tex_file
    ##!
   
    def Latex_Process_File_SVG(self,tex_file):
        return self.Latex_Process_File_PDF(tex_file,"svg")
    
    ##!
    ##! Name of PDF file from tex_file
    ##!
   
    def Latex_Process_File_Log(self,tex_file):
        return self.Latex_Process_File_PDF(tex_file,"log")
    
    ##!
    ##! Name of PDF file from tex_file
    ##!
   
    def Latex_Process_File_PNG(self,tex_file):
        return self.Latex_Process_File_PDF(tex_file,"png")
    
   
    ##!
    ##! Generate SVG from pdf.
    ##!
   
    def Latex_Process_2_PDF(self,tex_file,tmp_tex_file):
        if (self.CGI_Is()): return

        if (tex_file==tmp_tex_file): return

        print "PDF!!"
        exit()
        
        
    ##!
    ##! Generate SVG from pdf.
    ##!
   
    def Latex_Process_2_SVG(self,tex_file):
        res=0
        pdf_out_file=self.Latex_Process_File_PDF(tex_file)
        svg_out_file=self.Latex_Process_File_SVG(tex_file)
        dest_time=self.File_MTime(svg_out_file)
        if (re.search('svg$',sys.argv[0])):
        
            res=self.Files_Make_Command(
                [
                    self.Latex_Process_File_PDF(tex_file)
                ],
                [ svg_out_file ],
                [
                    "/usr/bin/pdf2svg",
                    pdf_out_file,
                    svg_out_file,
                ],
                self.Latex_Args_Force(),self.Latex_Args_Verbose()
            )
            
            if (not self.Latex_Args_Silent()):
                print svg_out_file,
            
                if (res==0):
                    if (dest_time==0): print "created"
                    else:              print "updated"
                else:                  print "uptodate"

        return res
       
    ##!
    ##! Generate PNG from pdf isong Ghostscript.
    ##!
   
    def Latex_Process_2_PNG(self,tex_file):
        res=0
        pdf_file=self.Latex_Process_File_PDF(tex_file)
        png_out_file=self.Latex_Process_File_PNG(tex_file)
        log_out_file=self.Latex_Process_File_Log(tex_file)
        
        dest_time=self.File_MTime(png_out_file)
        
        if (re.search('png$',sys.argv[0])):
        
            res=self.Files_Make_Command(
                [
                    self.Latex_Process_File_PDF(tex_file)
                ],
                [ png_out_file ],
                #[
                #    "/usr/bin/gs",
                #    "-sDEVICE=png256",
                #    "-q",
                #    "-dBATCH",
                #    "-dNOPAUSE",
                #    "-sOutputFile="+png_out_file,
                #    pdf_file,
                #],
                [
                    "/usr/bin/inkscape",
                    "--export-png="+png_out_file,
                    pdf_file,
                    ">"+log_out_file,
                    "2>&1"
                ],
                self.Latex_Args_Force(),self.Latex_Args_Verbose()
            )

            if (self.Latex_Args_Clean() and self.File_Exists(log_out_file)):
                self.File_Unlink(log_out_file)
                
            if (not self.Latex_Args_Silent()):
                print png_out_file,
            
                if (res==0):
                    if (dest_time==0): print "created"
                    else:              print "updated"
                else:                  print "uptodate"

        return res
        
    ##!
    ##! Send CGI output.
    ##!
   
    def Latex_Process_CGI_Send(self,tex_file):
        if (not self.CGI_Is()): return -1

        output_file=None
        ouput=None
        
        ##Send SVG?
        if (re.search('svg$',sys.argv[0])):
            output_file=self.Latex_Process_File_SVG(tex_file)
            output="svg"
                    
        ##Send PNG??
        elif (re.search('png$',sys.argv[0])):
            output_file=self.Latex_Process_File_PNG(tex_file)
            output="png"
                
        ##Send PDF??
        elif (re.search('pdf$',sys.argv[0])):
            output_file=self.Latex_Process_File_PDF(tex_file)
            output="pdf"
             

        #Sendheader
        if (output_file!=None and self.File_Exists(output_file)):
            self.CGI_HTTP_Header_Print(output,output_file)
            self.CGI_File_Send(output_file)
        else:
           self.CGI_HTTP_Header_Print("html")
           print "No such file:",output_file


