#from Main      import Args
from Files     import *
from Switches  import Args_Switches
from Arg       import Args_Arg


#The class my put files to parse here
   
class Args(Args_Switches,Args_Files,Args_Arg):
    __Switches__={}
    __Args__=[]

    echo=False
    
    ##! 
    ##! Take attribute type value..
    ##!
    
    def Type_2_Value(self,type,value):
        if (type=="int"):
            value=int(value)
        elif (type=="float"):
            value=float(value)
        elif (type=="str"):
            value=str(value)
        elif (type=="bool"):
            if (value.__class__.__name__=="str"):
                if (value=="True"):
                    value=True
                else:
                    value=False
            else:     
                if (value or value=="True"):
                    value=True
                else:
                    value=False

        return value

    
    ##! 
    ##! Take attribute type value..
    ##!
    
    def Value_2_Attr(self,attr,type,value,src):
        oldval=value
        value=self.Type_2_Value(type,value)

        objval=getattr(self,attr)
        if (objval!=value):
            setattr(self,attr,value)
            if (self.echo):
                print self.__class__.__name__,src+":","Set",attr,type,objval,"-->",value

            newval=getattr(self,attr)
            if (newval!=value):
                print self.__class__.__name__,src+":","Set Error!",attr,type,value,oldval,objval,newval

                
    def HasArgs(self):
        print sys.argv
        if (len(sys.argv)>1):
            return True

        return False
    
    def CLI2Obj(self):
        #Ignore puthon file name
        pos=1
        args=[]
        switches={}
        files=Args_Files_Get()
        
        while (pos<len(sys.argv)):
            value=sys.argv[pos]
            if (re.search('^-',value)):
                switch=re.sub('^-',"",value)
                value=sys.argv[pos+1]
                
                switches[ switch ]=value
                pos+=1
            elif (os.path.isfile(value)):
                 files.append(value)
                
            else:
                args.append(value)
                
            pos+=1
            
        self.Files_2_Obj(files)
        self.Args_2_Obj(args)
        self.Switches_2_Obj(switches)
