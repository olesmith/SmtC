import re


class Slides_Search_Results():
    ##!
    ##! Genrate Search Results
    ##!
    
    def Slides_Search_Results(self,paths):
        if (self.Slides_Search_Hide(paths)): return []
        
        spaths=self.Slides_Search_Results_Paths(paths)
        if (len(spaths)==0):
            return [self.B("No matches")]

        count=str(len(spaths))
        
        return [
            self.BR(),
            self.Div(
                [
                    self.B(
                        count+" Hits for '"+self.CGI_POST_Text("Search")+"':"
                    ),
                    self.HTML_Table
                    (
                        self.Slides_Search_Results_Table(spaths),
                        [],[],
                        {
                            #"class": "Search",
                        }
                    ),
                ],
                {
                    "class": "Search Hide",
                }
            )
        ]

    
    ##!
    ##! Genrate Search Results table
    ##!
    
    def Slides_Search_Results_Paths(self,paths):
        return self.Path_Tree_Paths(
            self.DocRoot,
            '\.(html|tex|py|php)$',
            self.CGI_POST_Text("Search")
        )
    
    ##!
    ##! Genrate Search Results table
    ##!
    
    def Slides_Search_Results_Table_Titles(self,paths):
        return [
            self.B("No."),
            self.B("Title"),
            self.B("Link")
        ]
    
    ##!
    ##! Generate Search Results table
    ##!
    
    def Slides_Search_Results_Path_Include(self,path):
        for fname in ("Name","Title","Contents"):
            fullname=[path,fname+".html"]
            if (self.File_Exists( "/".join(fullname) ) ):
                return True

            return False
    ##!
    ##! Generate Search Results table
    ##!
    
    def Slides_Search_Results_Table(self,spaths):
        table=[
            self.Slides_Search_Results_Table_Titles(spaths)
        ]

        n=0
        for path in spaths:
                if (self.Slides_Search_Results_Path_Include(path)):
                    n+=1
                    table.append(
                        self.Slides_Search_Results_Table_Row(n,path)
                    )

            
        return table
    ##!
    ##! Genrate Search Results table row
    ##!
    
    def Slides_Search_Results_Table_Row(self,n,path):
        path=re.sub(self.DocRoot+"/?","",path)
        paths=path.split("/")
        return [
            self.B(n),
            self.Slide_Title_Get(paths),
            self.Slide_Cell_Navigator_Link(paths,"","")
        ]
        
    ##!
    ##! Genrate Search Results table row Title Cell
    ##!
    
    def Slides_Search_Results_Table_Row_Title(self,paths):
        paths="/".split()
        self.Slide_Name_Get(paths)
