import cgi,sys,re

class CGI_POST():

    def CGI_Init_POST(self):
        if ( not self.__POST_Read__ ):
            self.__POST__={}
            if (self.CGI_Is()):
                self.CGI_Init_POST_HTTP()
            else:
                self.CGI_Init_POST_CLI()
                
            self.__POST_Read__=True
                
    def CGI_Init_POST_HTTP(self):
        args=cgi.FieldStorage()

        for arg in args.keys():
            self.__POST__[ arg ]=args[ arg ]
                
        
    def CGI_Init_POST_CLI(self):
        args=sys.argv
        for arg in args:
            if (not re.search('=',arg)): continue
                
            t=arg.split('=')
            if len(t)>1:
                k,v=arg.split('=')
                self.__POST__[k]=v
                
        
    def CGI_POST(self,key,default=None):
        self.CGI_Init_POST()
        form = cgi.FieldStorage() 

        value=default
        if self.__POST__.has_key(key):
            value=self.__POST__[ key ].value

        return value
    
    def CGI_POST_Int(self,key,default=None):
        value=self.CGI_POST(key,default)
        if (value==None): value=0
        
        return int( value )

    
    def CGI_POST_Text(self,key,default=None):
        value=self.CGI_POST(key,default)
        if (value==None): value=""

        return value

    def CGI_POST_List(self,key,default=None):
        value=self.CGI_POST(key,default)
        if (value==None): value=""

        if (value.__class__.__name__=='str'):
            value=value.split('\n')
        return value
