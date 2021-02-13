import re

class Latex_Input():
    ##!
    ##! Scan \input{file}'s in fname.
    ##! Return list of files.
    ##!
   
    def Latex_Inputs(self,tex_file,latex):
        files=self.Latex_Input_Files(tex_file,latex)
        
        self.Latex_Args_Message("Scanning input's"," ".join(files))
        
        return files
    ##!
    ##! Scan \input{file}'s in fname.
    ##! Return list of files.
    ##! Called recursively.
    ##!
   
    def Latex_Input_Files(self,tex_file,latex=None):
        if (latex==None):
            latex=self.File_Read_Lines(tex_file)

            
        path=self.Latex_Process_File_Path(tex_file)

        
        files=[tex_file]
        for line in latex:
            regex=re.search(r'\input\{([^\}]*)\}',line)
            if (not regex):
                regex=re.search(r'\include\{([^\}]*)\}',line)

            if (regex):
                rtex_file=regex.group(1)
                rtex_file=re.sub('\\\\TiKZPath',"/usr/local/tikz",rtex_file)
                rtex_file=re.sub('\\\\Path',path,rtex_file)
            
                if (not self.File_Exists(rtex_file)):
                    rtex_file=rtex_file+'.tex'
            
                msg="nonexistent"
                if (self.File_Exists(rtex_file)):
                    files=files+self.Latex_Input_Files(rtex_file)
                    msg="included"
                else:
                    msg="non-existent"
                
                self.Latex_Args_Message("\t",rtex_file,msg,line)
                
        return files
