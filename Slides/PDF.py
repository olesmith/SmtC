import os

class Slides_PDF():

    ##!
    ##! Send cookies, should be overriden
    ##!
    
    def Slides_PDF(self):
        path=self.DocRoot+"/"+self.Slides_CGI_Path()
        cwd=os.getcwd()

        os.chdir(path)

        latex=self.Slides_Latex()
        os.chdir(cwd)
        
