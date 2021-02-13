import re

from File import *
from Path import *
from System import *
from CGI import *

from Pre_Amble    import Latex_Pre_Amble
from Table        import Latex_Table
from Document     import Latex_Document
from TiKZ         import Latex_TiKZ
from Input        import Latex_Input
from Run          import Latex_Run
from Process      import Latex_Process
from Args         import Latex_Args
from Log          import Latex_Log

class Latex(
        File,Path,System,CGI,
        
        Latex_Pre_Amble,
        Latex_Table,
        Latex_Document,
        Latex_TiKZ,
        Latex_Input,
        Latex_Run,
        Latex_Process,
        Latex_Args,
        Latex_Log,
):
    __Latex__={
        "Formula": {
            "Left": "\\[",
            "Right": "\\]",
        },
        "Table": {
            "Defaults": {
                "Specs": None,
                "SpecSep": "",
                "Spec": "c",
                "ColSep": "&",
                "RowSep": "\\\\",
                "Pre": "   ",
            },
        }
    }

    pdflatexbin="/usr/bin/pdflatex"
    chroot="/chroot/"
    bibtexbin="/usr/bin/bibtex"
    tmp_path="/tmp/Slides"
    #??latex_pre_file="PreAmble.tex"
    tikz_pre_file=".tikz.tex"
    latex_pre_paths=[
        ".",
        "~/",
        "/etc",
    ]

    ##!
    ##!
    ##!
   
    def Latex_Vector(self,r,parms=""):
        return "\\underline{\\mathbf{"+r+"}}"+parms

    ##!
    ##!
    ##!
   
    def Latex_vect(self,r,align="c"):
        latex=[]
        for x in r:
            latex.append("   "+x)

            
        latex=[
            "\\left(\\begin{array}{"+align+"}",
            "\\\\\n".join(latex),
            "\\end{array}\\right)",
        ]
            
        return "\n".join(latex)
    
    def Latex_Left_Right(self,latex,ldelimiter="("):
        rdelimiter="???"
        if   (ldelimiter=="("):   rdelimiter=")"
        elif (ldelimiter=="["):   rdelimiter="]"
        elif (ldelimiter=="\\{"): rdelimiter="\\}"

        if (latex.__class__.__name__=='list'):
            latex=" ".join(latex)
        
        return "\\left"+ldelimiter+"  "+latex+"   \\right"+rdelimiter
    
    ##!
    ##!
    ##!
   
    def Latex_Formula(self,latex):
        if (latex.__class__.__name__=='list'):
            latex=";\\quad\n".join(latex)
            
        latex=re.sub(r'\n',"\n   ",latex)
        left=self.__Latex__[ "Formula" ][ "Left" ]
        right=self.__Latex__[ "Formula" ][ "Right" ]

        latex=left+"\n   "+latex+"\n"+right+"\n"
        
        return latex
    
 
           
    
