import re


class Slides_Search_Input():
    ##!
    ##! Options for search input field
    ##!
    
    def Slides_Search_Input_Field(self,paths):
        return self.HTML_Input(
            "Search_Field",
            "Search",
            self.CGI_POST_Text("Search"),
            "text",
            self.Slides_Search_Input_Options(paths)
        )
    
    ##!
    ##! Options for search input field
    ##!
    
    def Slides_Search_Input_Options(self,paths):
        options=self.Slides_Search_Options(paths)
        options[ "placeholder" ]="Search for"
        options[ "name" ]="Search"

        
        return options
