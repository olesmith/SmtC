from os import environ
import os,sys,cgi,re

__Header_Send__=False
from POST        import CGI_POST

class CGI(CGI_POST):

    __CGI__=[]
    __POST__={}
    __POST_Read__=False
    __GET__={}
    
    def CGI_ENV_Get(self,varname):
        value=""
        if (environ.has_key(varname)):
            value=environ[ varname ]
            
        return value
    
    def CGI_ENV_Vars(self):
        return environ.keys()
    
    def CGI_ENV_Show(self):
        for varname in environ.keys():
            print varname+":"+self.CGI_ENV_Get(varname)+"<BR>"
            
    def CGI_Host_Name(self):
        return self.CGI_ENV_Get("HTTP_HOST")
    
    def CGI_Host_Name_Qualified(self):
        return "http://"+self.CGI_Host_Name()
    
    def CGI_Is(self):
        value=self.CGI_ENV_Get("REQUEST_URI")

        res=False
        if (value):
            res=True
            
        return res
    
    def CGI_Doc_Root(self):
        return self.CGI_ENV_Get("DOCUMENT_ROOT")
    
    def CGI_Script_Name(self):
        return self.CGI_ENV_Get("SCRIPT_NAME")
    
    def CGI_Query_String(self):
        query=self.CGI_ENV_Get("QUERY_STRING")
        if (not query):
            if ( len(sys.argv)>1 ):
                query=sys.argv[1]

        return query
    
    def CGI_Query_Path(self):
        query=self.CGI_Query_String()
        comps=query.split('&')

        return comps[0]
    
    def CGI_Query_File(self):
        query=self.CGI_Query_String()
        comps=query.split('&')

        qfile=""
        if ( len(comps)>1 ):
            qfile=comps[1]
            comps=qfile.split('=')
            qfile=comps[ len(comps)-1 ]
            
        return qfile
    
    def CGI_HTTP_Header(self,content_type="html",attachment=None):
        content_type=re.sub('\n',"",content_type)

        headers={
            "text": "text/plain",
            "html": "text/html",
            "svg": "image/svg+xml",
            "pdf": "application/pdf",
            "png": "image/png",
            "tgz": "application/gzip",
        }

        if (headers.has_key(content_type)):
            content_type=headers[ content_type ]
        
        html="Content-Type: "+content_type+"\n"

        if (False):
            print "Content-Type: text/html\n\n"
            print "Attach",attachment,"cnt",content_type,"<BR>"
            print "Attach",attachment,"cnt",content_type
            exit()
        
        if (attachment!=None):
            attachment=re.sub('\n',"",attachment)
            html=html+"Content-Disposition: "
            html=html+"attachment; filename="
            html=html+os.path.basename(attachment)+"\n"

        return html

    
    def CGI_HTTP_Header_Print(self,content_type="html",attachment=None):
        global __Header_Send__

        if (self.CGI_Is() and not __Header_Send__):
            
            print self.CGI_HTTP_Header(content_type,attachment)

            __Header_Send__=True
    
    def CGI_Init_GET(self):
        self.__GET__={}
        args=os.getenv("QUERY_STRING")

        self.__GET__={}
        if (not args):
            return False
        
        args=args.split("&")
        for arg in args: 
            t=arg.split('=')
            if len(t)>1:
                k,v=arg.split('=')
                self.__GET__[k]=v

    def CGI_GET(self):
        self.CGI_Init_GET()
            
        return self.__GET__
    
    def CGI_Init(self):
        self.CGI_Init_GET()
        #self.CGI_Init_POST()

        
    def CGI_GET_Text(self,key):
        self.CGI_Init_GET()
        value=re.sub('%2F',"/",self.__GET__[ key ])
        
        return value
    
    def CGI_File_Send(self,fname):
        f=open(fname,"rb")
        print f.read()
        f.close()
       
