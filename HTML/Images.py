import os,glob,re


from Base import *


class HTML_Images():
    ##! 
    ##! Generates Images table (as html)
    ##!
    
    def HTML_Images_Display(self,basepath,globpath,svgfiles,ncols,options):        
        table=[]
        img_row=[]
        tit_row=[]
        for svgfile in svgfiles:
            img=self.HTML_Carousel_Image(svgfile,options)
            img_row.append(img)

            
            tit_row.append(os.path.basename(svgfile))

            if (len(img_row)>=ncols):
                table.append(img_row)
                table.append(tit_row)
                img_row=list()
                tit_row=list()

        if (len(img_row)>0):
            table.append(img_row)
            table.append(tit_row)

            
        return self.HTML_Table(table)
    
