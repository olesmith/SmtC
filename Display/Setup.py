from Base import *

import os

class Display_Setup():
    ##! 
    ##! Path to setup file.
    ##!
    
    def Display_Setup_Path(self):
        path=self.CGI_Query_Path()
        comps=path.split('/')
        rcomps=[]
        if (len(comps)>0):
            rcomps.append( comps[0] )
        if (len(comps)>1):
            rcomps.append( comps[1] )
            
        return "/".join( [ self.FS_Root ]+rcomps )

    ##! 
    ##! Full path of setup file.
    ##!
    
    def Display_Setup_File(self,path=None):
        if (not path):
            path=self.Display_Setup_Path()

        
        if (not os.path.isdir(path)):
            path="/".join(   [ self.FS_Root,path ] )
        
        return "/".join( [ path,"Setup.inf" ] )
    
    ##! 
    ##! Read setup file (infos)
    ##!
    
    def Display_Setup_File_Read(self,path):
        setup={}
        setupfile=self.Display_Setup_File(path)
        if (os.path.isfile(setupfile)):
            setup=self.File_2_Dict(setupfile)
            setup[ "File" ]=setupfile
                
        return setup

    ##! 
    ##! Read setup file (infos)
    ##!
    
    def Display_Setup_Read(self,path=None):
        if (not self.Setup):
            setupfile=self.Display_Setup_File(path)
            if (os.path.isfile(setupfile)):
                self.Setup=self.Display_Setup_File_Read(path)
        return self.Setup

    ##! 
    ##! Read setup file (infos)
    ##!
    
    def Display_Setup_Key(self,key):

        value=""
        if (self.Setup.has_key(key)):
            value=self.Setup[ key ]
        return value
