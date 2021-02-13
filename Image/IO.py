import gd,os

from File import *
from Base import *
from XML import XML

class Image_IO(XML):
    def Image_Rewrite(self):
        self.SVG=self.SVG_Head()+self.SVG_Header(self)

        if (int(self.Verbose)>0):
            print "Image,",self.Name,"initialized",self.Resolution
            
    

    def Image_Write(self):
        self.Image_SVG_Append( self.SVG_Close() )

        fname=self.Image_File()

        self.File_Path_Create(fname)
        
        size=self.File_Write(fname,self.SVG)
        if (int(self.Verbose)>0):
            print "Image:",self.Name,size,"bytes written to:",fname,"(svg)"
        
        return self.Image_File()
    
