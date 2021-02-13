import re,sys

class Latex_TiKZ():
    def Latex_TikZ_Should(self,tex_file,tikz=None):
        if (tikz==None):
            tikz=False
            if (re.search('tikz2',sys.argv[0])):
                tikz=True
            elif (re.search('\.tikz',tex_file)):
                lines=self.File_Read(tex_file)
                if (re.search('documentclass\{standalone\}',lines)):
                    tikz=True
        return tikz
    
    ##!
    ##!
    ##!
   
    def Latex_TikZ_Picture(self,tikz):
        hastikzpicture=False
        for tikzline in tikz:
            if (re.search('tikzpicture',tikzline)):
                hastikzpicture=True
                break
            
        if (not hastikzpicture):
            tikz=[
                '\\begin{tikzpicture}%[trig format=rad]',
            ]+tikz+[
                '\\end{tikzpicture}',
            ]

        return tikz
       
