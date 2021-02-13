import re

class Slide_Cell_Code_Ambles_Pre():
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Ambles_Pre_Get(self,contents):
        hasbegindoc=False
        n=self.Slide_Cell_Code_Ambles_Pre_Get_N(contents)

        self._Doc_Body_Default_=[]
        for n in range(n,len(contents)):
            if (re.search('\\\\end\{document\}',contents[n])):
                break

            if (not re.search('\\\\(begin|end)\{document\}',contents[n])):
                self._Doc_Body_Default_.append(contents[n])
            
        self._Doc_Ambles_Post_Default_=[]

        for n in range(n+1,len(contents)):
            self._Doc_Ambles_Post_Default_.append(contents[n])
      

        #Trim content entities
        self._Doc_Ambles_Pre_Default_=self.Slide_Cell_Code_Doc_Contents_Trim(
            self._Doc_Ambles_Pre_Default_
        )
        
        self._Doc_Body_Default_=self.Slide_Cell_Code_Doc_Contents_Trim(
            self._Doc_Body_Default_
        )
        
        self._Doc_Ambles_Post_Default_=self.Slide_Cell_Code_Doc_Contents_Trim(
            self._Doc_Ambles_Post_Default_
        )

    ##!
    ##! Document style accessor
    ##!
    
    def Slide_Cell_Code_Ambles_Pre(self):
        return self.Slide_Cell_Code_CGI_Pre_Amble_Values()
        
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Ambles_Pre_Get_N(self,contents):        
        begindoc_has=False
        self._Doc_Ambles_Pre_Default_=[]
        
        n=0
        for n in range(len(contents)):
            if (re.search('begin\{document\}',contents[n])):
                begindoc_has=True
                break

            self._Doc_Ambles_Pre_Default_.append(contents[n])

        if (not begindoc_has):
            n=0
            self._Doc_Ambles_Pre_Default_=[]
            

        return n

    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Ambles_Pre_Rows(self):
        return [
            [
                self.Span(
                    "%%! Preamble",
                    {
                        "class": "Edit_Doc_Options"
                    }
                )                
            ],
            self.Slide_Cell_Code_Ambles_Pre_Div()
        ]
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Ambles_Pre_Div(self):
        return [
            self.Div(
                self.Slide_Cell_Code_Ambles_Pre_Input(),
                {
                    "class": ["Edit_Form","Edit_Input","Edit_Doc_PreAmble_Div","Center"],
                }
            )
        ]
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Ambles_Pre_Input(self):
        cgi_key=self.Slide_Cell_Code_Pre_Amble_Key()

        cols=self.Slide_Cell_Code_Edit_TEXTAREA_NCols()

        rows=len(self.Slide_Cell_Code_Ambles_Pre())+3
        
        return self.HTML_Input(
            cgi_key,cgi_key,
            self.Slide_Cell_Code_Ambles_Pre(),
            "area",
            {
                "title": "Preamble",
                "class": ["Edit_Form","Edit_Input","Edit_Doc_PreAmble_Input"],
                "cols": cols,
                "rows": rows,
                #"wrap": "hard",
            }
        )
    
 
