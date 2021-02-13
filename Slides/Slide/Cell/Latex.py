import re

class Slides_Slide_Cell_Latex():
    ##!
    ##! Insert latex, converting via mathmlmath
    ##!
    
    def Slide_Cell_Latex(self,content,paths):
        if ( re.search('@Latex\s+',content, re.IGNORECASE) ):
            content=re.sub(r'@Latex\s+',"\(",content)+"\)"
        return content

    
