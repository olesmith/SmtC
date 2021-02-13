import re

class Slide_Cell_Code_Body():
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Doc_Body_Rows(self):
        return [
            [
                self.Span(
                    "\\begin{document}",
                    {
                        "class": "Edit_Doc_Options"
                    }
                )
            ],
            [
                self.Span(
                    "%%! Body",
                    {
                        "class": "Edit_Doc_Options"
                    }
                )
            ],
            self.Slide_Cell_Code_Doc_Body_Div(),
            [
                self.Span(
                    "\\end{document}",
                    {
                        "class": "Edit_Doc_Options"
                    }
                )
            ],
        ]
    
    
    ##!
    ##! Document style accessor
    ##!
    
    def Slide_Cell_Code_Doc_Body(self):
        return self.Slide_Cell_Code_CGI_Body_Values()
        
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Doc_Body_Div(self):
        return [
            self.Div(
                self.Slide_Cell_Code_Doc_Body_Input(),
                {
                    "class": ["Edit_Form","Edit_Input","Edit_Doc_Body_Div"],
                }
            )
        ]
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Doc_Body_Input(self):
        cgi_key=self.Slide_Cell_Code_CGI_Body_Key()
        cgi_values=self.Slide_Cell_Code_Doc_Body()
        

        cols=self.Slide_Cell_Code_Edit_TEXTAREA_NCols()
        rows=len(self.Slide_Cell_Code_Doc_Body())+3
        
        return self.HTML_Input(
            cgi_key,cgi_key,
            cgi_values,
            "area",
            {
                "title": "Body",
                "class": ["Edit_Form","Edit_Input","Edit_Doc_Body_Input"],
                "cols": cols,
                "rows": rows,
                #"wrap": "hard",
            }
        )
