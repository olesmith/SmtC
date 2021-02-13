

class Display_Top():

    ##! 
    ##! Generates TOP row
    ##!
    
    def Display_Top(self):
        html=[]
        indent=3
        
        html=html+[ self.XML_Tag_Start("TR") ]
        
        html=html+[ self.Display_Cell("Top","Left") ]
        html=html+[ self.Display_Cell("Top","Center") ]
        html=html+[ self.Display_Cell("Top","Right") ]

        html=html+[ self.XML_Tag_End("TR")  ]
        
        return html



    ##! 
    ##! Generates TOP row left cell.
    ##!
    
    def Display_Top_Left_Cell(self):
        return self.HTML_Top_Left()

    ##! 
    ##! Generates TOP row center cell.
    ##!
    
    def Display_Top_Center_Cell(self):
        return self.HTML_Top_Center()

    
    ##! 
    ##! Generates TOP row left cell.
    ##!
    
    def Display_Top_Right_Cell(self):
        return self.HTML_Top_Right()
