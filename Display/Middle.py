import os

class Display_Middle():
    
    ##! 
    ##! Generates Middle row
    ##!
    
    def Display_Middle(self):
        html=[]

        html=html+[ self.XML_Tag_Start("TR") ]   
        
        html=html+[ self.Display_Cell("Middle","Left") ]  
        html=html+[ self.Display_Cell("Middle","Center") ]  
        html=html+[ self.Display_Cell("Middle","Right") ]  
        
        html=html+[ self.XML_Tag_End("TR")+"\n" ]  

        rhtml=[ self.Display_Middle_Geometry_Frame() ]  
        rhtml=[ self.XML_Tags("TD",rhtml,{ "colspan": 3, }) ]  
        rhtml=[ self.XML_Tags("TR",rhtml) ]  
        
        return html+rhtml


    
    ##! 
    ##! Generates Middle row left cell.
    ##!
    
    def Display_Middle_Left_Cell(self):
        return self.HTML_Middle_Left()

    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def Display_Middle_Center_Cell(self):
        return self.HTML_Middle_Center()

    ##! 
    ##! Generates Middle row right cell.
    ##!
    
    def Display_Middle_Right_Cell(self):
        return self.HTML_Middle_Right()
    
  
