import re,sys

sys.path[ len(sys.path)-1 ]='/usr/local/python'

from Curves2 import *

class Slides_Slide_Cell_Curve2():
    ##!
    ##! Insert Curve2 html
    ##!
    
    def Slide_Cell_Curve2(self,content,paths):
        if ( re.search('@Curve2\s+',content) ):
            curvename=re.sub(r'@Curve2\s+',"",content)

            curves2=Curves2(False,curvename)
            curve=curves2.Curves2_Curve(curvename)
            self.Cookies_Obj=curve
            
            html=curves2.Curve.Curve_Html(curves2)

        return html

    
