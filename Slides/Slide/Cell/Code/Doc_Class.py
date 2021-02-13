import re

class Slide_Cell_Code_Doc_Class():
    
    ##!
    ##! Scans contents for document type
    ##!
    
    def Slide_Cell_Code_Edit_Doc_Class_Get(self,scriptfile,contents):
        for n in range(len(contents)):
            regex=re.search('documentclass(\[.*\])?\{(\S*)\}',contents[n])
            
            if (regex):
                matches=regex.groups()
                if (matches[0]!=None):
                    self._Doc_Class_Options_Default_=matches[0]
                    self._Doc_Class_Options_Default_=re.sub(
                        '[\[\]]',"",
                        self._Doc_Class_Options_Default_
                    )
                self._Doc_Class_Default_=matches[1]

                contents.pop(n)
                break

        

        return contents
                
    ##!
    ##! Document style accessor
    ##!
    
    def Slide_Cell_Code_Edit_Doc_Class(self):
        return self.Slide_Cell_Code_CGI_Value()

    ##!
    ##! Document style optionsaccessor
    ##!
    
    def Slide_Cell_Code_Edit_Doc_Class_Options(self):
        return self.Slide_Cell_Code_CGI_Options_Value()

    ##!
    ##! Creates Document Style row(s)
    ##!
    
    def Slide_Cell_Code_Edit_Doc_Class_Rows(self):
        return [
            [
                self.Span(
                    "\\documentclass",
                    {
                        "class": "Edit_Doc_Options"
                    }
                )+
                self.Slide_Cell_Code_Edit_Doc_Class_Options_Input()
                +
                self.Slide_Cell_Code_Edit_Doc_Class_Input()
            ],
        ]
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Edit_Doc_Class_Cells(self,limiters,cgi_key,cgi_value,css_class,title):
        return [
            self.Slide_Cell_Code_Doc_Limiter(
                limiters[0],
                False
            ),

            
            self.HTML_Input(
                cgi_key,
                cgi_key,
                cgi_value,
                "text",
                {
                    "title": title,
                    "class": ["Edit_Form","Edit_Input",css_class]
                }
            ),

            
            self.Slide_Cell_Code_Doc_Limiter(
                limiters[1],
                True
            ),
        ]
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Edit_Doc_Class_Options_Input(self):
        return self.Slide_Cell_Code_Edit_Doc_Class_Cells(
            "[]",
            self.Slide_Cell_Code_CGI_Options_Key(),
            self.Slide_Cell_Code_CGI_Options_Value(),
            "Edit_Doc_Options",
            "Documentstyle optional arguments ([...])"
        )

    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Edit_Doc_Class_Input(self):
        return self.Slide_Cell_Code_Edit_Doc_Class_Cells(
            "{}",
            self.Slide_Cell_Code_CGI_Key(),
            self.Slide_Cell_Code_CGI_Value(),
            "Edit_Doc_Class",
            "Documentstyle ({})"
        )
    
