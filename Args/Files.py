import re

#global for all classes to share.
__Files__=[]

##! 
##! Adds files to __Files__
##!
    
def Args_Files_Add(files):
    global __Files__
    __Files__=__Files__+files
    
##! 
##! Gets files in __Files__
##!
    
def Args_Files_Get():
    
    global __Files__
    return __Files__
    ##! 
    ##! Parse file for usable object switch/attribute values
    ##!
    
class Args_Files():

    
    def File_2_Obj(self,file):
        f=open(file,'r')
        lines=f.read()
        lines=lines.splitlines()
        for line in lines:
            comps=re.split(r'\s*[:=]\s*', line)
            if (len(comps)==2):
                attr=comps[0]
                attr=re.sub(r'\s+',"",attr)
                value=comps[1]
                value=re.sub(r'^\s+',"",value)
                value=re.sub(r'\s+$',"",value)
                value=re.sub(r',$',"",value)

                if (hasattr(self,attr)):
                    objvalue=getattr(self,attr)
                    type=objvalue.__class__.__name__
                    
                    self.Value_2_Attr(attr,type,value,file)

    ##! 
    ##! Parse files for usable object switch/attribute values
    ##!
    
    def Files_2_Obj(self,files):
        for file in files:
            self.File_2_Obj(file)
                
