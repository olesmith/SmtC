import re

class Slides_Slide_Navegator():    
    ##!
    ##! Sandwich contents between upper and lower navigator menu (identical).
    ##!
    
    def Slide_Cell_Navigator_Menues(self,paths,contents):
        nav_menu=self.Slide_Cell_Navigator_Menu(paths)

        return nav_menu+[contents]+nav_menu
    
    ##!
    ##! Generate navegator menu, anchor with a DIV.
    ##!
    
    def Slide_Cell_Navigator_Menu(self,paths):

        return [
            self.Anchor("Navigator_Menu"),
            self.Div(
                self.Slide_Cell_Navigator_Links(paths),
                {
                    "class": "Slide_Navegator_Menu",
                }
            )
        ]
    
    ##!
    ##! Generate navegator list of links
    ##!
    
    def Slide_Cell_Navigator_Links(self,paths):
        tree=self.Path_Tree(self.DocRoot,'^\d')

        links=[]
        prevpaths=self.Path_Tree_Subdirs_Previous(tree,paths)
        if ( len(prevpaths)>0 ):
            links.append(
                self.Slide_Cell_Navigator_Link(
                    prevpaths,
                    "&lt; ",""
                )
            )
        elif (len(paths)>0):
            paths.pop(len(paths)-1)

            links.append(
                self.Slide_Cell_Navigator_Link(
                    paths,
                    "&lt; ",""
                )
            )

        links.append(
           " | "+ self.Slide_Name_Get(paths)+" | "
        )
                
        nextpaths=self.Path_Tree_Subdirs_Next(tree,paths)
        if ( len(nextpaths)>0 ):
            links.append(
                self.Slide_Cell_Navigator_Link(
                    nextpaths,
                    ""," &gt;"
                )
            )
        elif (len(paths)>0):
            paths.pop(len(paths)-1)

            links.append(
                self.Slide_Cell_Navigator_Link(
                    paths,
                    ""," &gt;"
                )
            )

            
        return links
    
    ##!
    ##! Generate navegator link.
    ##!
    
    def Slide_Cell_Navigator_Link(self,paths,pretext,posttext):
        return [
            self.A(
                "?Path="+"/".join(paths),
                pretext+self.Slide_Name_Get(paths)+posttext,
                {
                    "class": "Slide_Navegator_Links",
                },
                self.Slide_Title_Get(paths)
            )
        ]
    
