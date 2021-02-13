#!/usr/bin/python

from Display import Display
import re,sys

execname=sys.argv[0]
execname=execname.split('/')
execname=execname.pop()


display=Display()
if (re.search('Display(.py)?$',execname)):
    display.Display_Generate()
    
elif (execname=="SVG"):
    display.Display_SVG()
    
elif (execname=="PNG"):
    display.Display_PNG()
    
elif (execname=="PDF"):
    display.Display_PDF()
    
elif (execname=="Frame"):
    display.Display_Frame()
    
#elif (execname=="Carousel"):
#    display.Display_Carousel()
        
