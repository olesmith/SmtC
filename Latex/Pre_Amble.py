import re

class Latex_Pre_Amble():
    
    ##!
    ##! If first line in tex_file is NOT documentclass,
    ##! return list with preamble-file as only item.
    ##! If not, return empty list
    ##!
   
    def Latex_Pre_Amble(self,tex_file):
        lines=self.File_Read(tex_file)

        res=False
        if (re.search('documentclass',lines)):
            res=True

        files=[]
        if (not res):
            files=[self.Latex_Pre_Amble_TikZ(tex_file)]

        return files
        
    ##!
    ##! Locate first self.tikz_pre_file in self.tikz_pre_paths.
    ##!
   
    def Latex_Pre_Amble_TikZ(self,tex_file):
        pre_files=None
        if (re.search('\.tikz\.tex$',tex_file)):
            pre_files=self.tikz_pre_file
            
        if (pre_files==None): return None
        
        for pre_path in self.latex_pre_paths:
            filename="/".join([
                pre_path,pre_files
            ])

            if (self.File_Exists(filename)):
                pre_files=filename
                break

        #if (pre_file==None):
        #    print "No TikZ PreAmble file",self.tikz_pre_file,
        #    print " found in:",", ".join(self.latex_pre_paths)
        #    exit()

        return pre_files
