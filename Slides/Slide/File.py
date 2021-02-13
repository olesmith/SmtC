import os,re


class Slides_Slide_File():
    def Slide_File_Name(self,paths,fname):
        return self.DocRoot+"/"+"/".join(paths)+"/"+fname

    
    def Slide_File_Content(self,paths,fname,fname1="Name.html"):
        fname=self.Slide_File_Name(paths,fname)
        fname1=self.Slide_File_Name(paths,fname1)

        value=fname
        if (os.path.isfile(fname)):
            value=self.File_Read(fname)
        elif (os.path.isfile(fname1)):
            value=self.File_Read(fname1)
        else:
            value=paths[ len(paths)-1 ]
        
        return value
 
    def Slide_File_Contents_Exists(self,paths,fname):
        return os.path.isfile(
            self.Slide_File_Name(paths,fname)
        )
        
    def Slide_File_Contents(self,paths,fname):
        value=""
        if (self.Slide_File_Contents_Exists(paths,fname)):
            value=self.File_Read_Lines(
                self.Slide_File_Name(paths,fname)
            )
        
        return value
    
