import re,os

class Slide_Cell_Code_Edit():
    
    ##!
    ##! Create toggable hidden entry on Edit Form
    ##!
    
    def Slide_Cell_Code_Edit_Frame(self,scriptfile,paths,args):
        return []
        if (not re.search('\.tex$',scriptfile)):
            return []

        display='none'
        if (self.CGI_POST_Int("Save")):
            display='block'
        
        return self.HTML_Frame(
            self.Slide_Cell_Code_Edit_Form(scriptfile,paths,args),
            {
                "title": "Edit "+scriptfile,
                "class": "Table_Frame Code",
                "id":    "Table_Frame_Code",

            },
            {
                "border": "1px solid black",
                "display": display,
            }
        )
    
    ##!
    ##! Edit Form for tex files
    ##!
    
    def Slide_Cell_Code_Edit_Form(self,scriptfile,paths,args):        
        contents=self.File_Read_Lines(
            "/".join(
                [self.DocRoot]+
                paths+
                [scriptfile]
            )
        )

        return self.HTML_Form(
            1,
            #id
            "Edit_"+scriptfile,

            self.Slide_Cell_Code_Edit_Form_Url(scriptfile,paths,contents),
            self.Slide_Cell_Code_Edit_Html(scriptfile,paths,contents),
            {
                "class": "Edit",
            }
        )
    
    ##!
    ##! File info entry for file
    ##!
    
    def Slide_Cell_Code_Edit_Form_Url(self,scriptfile,paths,contents):
        return "".join([
            "?Path=",
            "/".join(paths),
            "&File=",
            scriptfile,
            "#"+"Table_Frame_Code",
        ])


    
    ##!
    ##! File info entry for file
    ##!
    
    def Slide_Cell_Code_Edit_Html(self,scriptfile,paths,contents):
        return  [
            self.Slide_Cell_Code_Doc_Span("Hide Form"),
            self.HTML_Table(
                self.Slide_Cell_Code_Edit_Table(
                    scriptfile,paths,contents
                ),[
                    self.H(5,"Edit $\LaTeX$ Doc: "+scriptfile)
                ]
            )
        ]
        
    ##!
    ##! File info entry for file
    ##!
    
    def Slide_Cell_Code_Edit_Table(self,scriptfile,paths,contents):

        contents=self.Slide_Cell_Code_Edit_Doc_Class_Get(scriptfile,contents)
        
        self.Slide_Cell_Code_Ambles_Pre_Get(contents)

        rows=self.Slide_Cell_Code_Edit_Doc_Class_Rows()

        rows=rows+self.Slide_Cell_Code_Ambles_Pre_Rows()
        
        rows=rows+self.Slide_Cell_Code_Doc_Body_Rows()

        rows=rows+self.Slide_Cell_Code_Ambles_Post_Rows()
        
        return rows+[
            self.Slide_Cell_Code_Edit_Buttons_Row()
        ]
    
    ##!
    ##! Formats delimiters ([]{})
    ##!
    
    def Slide_Cell_Code_Edit_Buttons_Row(self):

        return [
            self.Center(
                self.HTML_Button(
                    "Save","Save",
                    "Save",
                    1,
                    'submit',
                    {
                        "class": ["Edit_Doc_Buttons"],
                    }
                )+self.HTML_Button(
                    "PDF","PDF",
                    "PDF",
                    1,
                    'submit',
                    {
                        "class": ["Edit_Doc_Buttons"],
                    }
                )+self.HTML_Button(
                    "Reset","Reset",
                    "Reset",
                    1,
                    'reset',
                    {
                        "class": ["Edit_Doc_Buttons"],
                    }
                )
            )
        ]
    
    ##!
    ##! Formats delimiters ([]{})
    ##!
    
    def Slide_Cell_Code_Doc_Limiter(self,limiter,right):
        classes=[ "Edit_Limiter" ]
        if (right):
            classes.append("Edit_Limiter_Right")
        else:
            classes.append("Edit_Limiter_Left")
        
        return self.Span(
            limiter,
            {
                "class": [ "Edit_Limiter","","", ]
            }
        )

    ##!
    ##! Removes leading and trailing empty lines.
    ##!
    
    def Slide_Cell_Code_Doc_Contents_Trim(self,contents):
        n=0
        for n in range(len(contents)):
            if (re.search('\S',contents[n])):
                break

        body=contents[n:]
        
        for n in range(len(body)-1,-1,-1):
            if (re.search('\S',contents[n])):
                break

        body=body[:n+2]

        return body
    ##!
    ##! Removes leading and trailing empty lines.
    ##!
    
    def Slide_Cell_Code_Doc_Contents_MaxLen(self,contents):
        maxlen=20
        for content in contents:
            if (len(content)>maxlen): maxlen=len(content)

        return maxlen
        
             
    ##!
    ##! Removes leading and trailing empty lines.
    ##!
    
    def Slide_Cell_Code_Doc_Span(self,title):
        return self.Span(
            title,
            {
                "onclick": "Toggle_Element_By_ID('Table_Frame_Code','block');"
            },
            {
                "background-color": "white",
                "text-decoration": "underline",
            }
        )
    
    ##!
    ##! File info entry for file
    ##!
    
    def Slide_Cell_Code_Edit_TEXTAREA_NCols(self):        
        return self.Slide_Cell_Code_Doc_Contents_MaxLen(
            self.Slide_Cell_Code_Ambles_Pre()+
            self.Slide_Cell_Code_Doc_Body()
        )
    
