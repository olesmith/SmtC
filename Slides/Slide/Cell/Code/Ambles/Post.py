
class Slide_Cell_Code_Ambles_Post():
    ##!
    ##! Document style accessor
    ##!
    
    def Slide_Cell_Code_Ambles_Post(self):
        return self._Doc_Ambles_Post_Default_
        
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Ambles_Post_Rows(self):
        return [
            [
                self.Span(
                    "%%! Postamble",
                    {
                        "class": "Edit_Doc_Options"
                    }
                )                
            ],
            self.Slide_Cell_Code_Ambles_Post_Div()
        ]
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Ambles_Post_Div(self):
        return [
            self.Div(
                self.XML_Tags(
                    "CODE",
                    self.Slide_Cell_Code_Ambles_Post(),
                    {
                        "class": ["Edit_Form","Edit_Input","Edit_Doc_PostAmble_Div","Center"],
                    }
                )
            )
        ]
