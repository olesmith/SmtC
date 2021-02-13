import re

from Input   import Slides_Search_Input
from Results import Slides_Search_Results

class Slides_Search(
        Slides_Search_Input,
        Slides_Search_Results,
):
    
    ##!
    ##! Create html necessary for Searching
    ##!
    
    def Slides_Search(self,paths):
        return [
            self.Slides_Search_Form(paths),
        ]
    
    ##!
    ##! Create search input form
    ##!
    
    def Slides_Search_Form(self,paths):
        return self.HTML_Form(
            1,"Search",
            self.Slides_Search_Url(paths),[
                
                self.Slides_Search_Field(paths),
                self.Slides_Search_Results(paths),
                
            ]
        )

    
    ##!
    ##! Create search input field
    ##!
    
    def Slides_Search_Field(self,paths):
        return [
            self.Slides_Search_Icons(paths),
            self.Slides_Search_Input_Field(paths),
            self.HTML_Button(
                "Search_Button",
                "GO",
                "Search!",
                1,
                "submit",
                self.Slides_Search_Options(paths)
            ),
        ]
    
    ##!
    ##! Options common for search elements
    ##!
    
    def Slides_Search_Options(self,paths):
        options={
            "class": "Search Hide",
            "style": self.Slides_Search_Style(paths),
        }

        return options
    
    ##!
    ##! Should we display Search hidens: True or False
    ##!
    
    def Slides_Search_Hide(self,paths):
        go=self.CGI_POST_Int("GO")

        res=False     
        if (go==1):
            res=True

        return not res
    
    ##!
    ##! Style for search elements
    ##!
    
    def Slides_Search_Style(self,paths):
        style={}        
        if (self.Slides_Search_Hide(paths)):
            style[ "display" ]="none"
        
        return style

    
    ##!
    ##! Show/Hide Icons
    ##!
    
    def Slides_Search_Url(self,paths):
        return "?Path="+"/".join(paths)

    
    ##!
    ##! Show/Hide Icons
    ##!
    
    def Slides_Search_Icons(self,paths):
        return self.HTML_Icons_Toggle(
            "Search",
            "fas fa-search",
            self.Slides_Search_Hide(paths),
            None,None,None,
            {
                "title": "Search for Contents"
            }
        )
    
