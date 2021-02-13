

class Display_Bottom():
    def Display_Bottom(self):         
        html=[]

        html=html+[ self.XML_Tag_Start("TR") ]   
        
        
        html=html+[ self.Display_Cell("Bottom","Left") ]   
        html=html+[ self.Display_Cell("Bottom","Center") ]   
        html=html+[ self.Display_Cell("Bottom","Right") ]   

        html=html+[ self.XML_Tag_End("TR") ]

        return html


    
    ##! 
    ##! Generates Bottom row left cell.
    ##!
    

    def Display_Bottom_Left_Cell(self):
        return self.HTML_Bottom_Left()

    ##! 
    ##! Generates Bottom row center cell.
    ##!
    
    def Display_Bottom_Center_Cell(self):        
        return self.HTML_Bottom_Center()

    ##! 
    ##! Generates Bottom row right cell.
    ##!
    
    def Display_Bottom_Right_Cell(self):
        return self.HTML_Bottom_Right()

    
    
