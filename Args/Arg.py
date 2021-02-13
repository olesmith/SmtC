import sys

class Args_Arg():
    ##! 
    ##! self.__Args__ acessor.
    ##!
    
    def Args_Get(self,argno=-1,key=None):
        if (argno>=0):
            if (argno<len(self.__Args__)):
                if (key):
                    if (self.__Args__[ argno ].has_key(key)):
                        return self.__Args__[ argno ][ key ]
                    
                else:
                    return self.__Args__[ argno ]
        else:
            return self.__Args__

        return None
    
    ##! 
    ##! Returns attribute name associated with argno
    ##!
    
    def Arg_2_Attr(self,argno):
        return self.Args_Get(argno,"Attr")
    
    ##! 
    ##! Returns text (user info) associated with argno
    ##!
    
    def Arg_2_Text(self,argno):
        return self.Args_Get(argno,"Text")
    
    ##! 
    ##! Returns type associated with argno: int, float, str and bool
    ##!
    
    def Arg_2_Type(self,argno):
        return self.Args_Get(argno,"Type")
    
    ##! 
    ##! Parse args for usable object switch/attribute values
    ##!
    
    def Args_2_Obj(self,args):
        for argno in range( len(args) ):
            hash=self.Args_Get(argno)
            if (hash):
                type=self.Arg_2_Type(argno)
                attr=self.Arg_2_Attr(argno)
                
                value=args[ argno ]
                
                self.Value_2_Attr(attr,type,value,"Arg "+str(argno))

    def CLI_Get(self):
        args=sys.argv
        args.insert(0, "/usr/bin/python")
        return " ".join(sys.argv)
            
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
        
    def Obj2Args(self):
        print "Class:",self.__class__.__name__+":"
        
        if ( len(self.__Switches__)>0 ):
            print "\tCommand Switches:"
            for switch in self.__Switches__.keys():
                name=self.__Switches__[ switch ]

                print switch,name
                name=getattr(self,name)
               
                print "\t\t-"+switch," --> ",self.__Switches__[ switch ],"\n\t\tDefault: ",name

                if (self.__Switches_Text__.has_key(switch)):
                    print "\t\t"+self.__Switches_Text__[ switch ]

        if ( len(self.__Args__)>0 ):
            print "\tCommand Arguments:"
            i=0
            for arg in self.__Args__:
                value=getattr(self,arg)
                print "\t\t"+arg,"\n\t\tDefault: ",value
                if ( len(self.__Args_Text__)>i ):
                    print "\t\t"+self.__Args_Text__[ i ]

                i+=1
