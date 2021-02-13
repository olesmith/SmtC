from File      import Slides_Slide_File
from Cell      import Slides_Slide_Cell
from Navegator import Slides_Slide_Navegator

class Slides_Slide(
        Slides_Slide_File,
        Slides_Slide_Cell,
        Slides_Slide_Navegator
):
    
    def Slide_Name_Get(self,paths):
        name=str.rstrip( self.Slide_File_Content(paths,"Name.html") )
        return str.rstrip( self.Slide_File_Content(paths,"Name.html") )

    def Slide_Title_Get(self,paths):
        return str.rstrip( self.Slide_File_Content(paths,"Title.html") )
    
    def Slide_Contents_Get(self,paths):
        return self.Slide_File_Contents(paths,"Contents.html")
    
    def Slide_Show_Should(self,paths):
        return self.Slide_File_Contents_Exists(paths,"Name.html")
    
    def Slide_Link_Should(self,paths):
        return self.Slide_File_Contents_Exists(paths,"Contents.html")
