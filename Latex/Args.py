import re,sys,argparse

class Latex_Args():
    __Parser__=None
    __Args__=None
    __Test__=False
    
    __Verbose__=False
    __NoClean__=False
    __Clean__=True
    __Silent__=False
    __Force__=False
    __Log__=False
    __Warnings__=False
    
    __Figs__=False
    
    __T__=False
    
    __TexFiles__=[]
    
    ##!
    ##! 
    ##!
   
    def Latex_Args_Init(self):
        if (self.CGI_Is()):
            self.Latex_Args_Init_CGI()
        else:
            self.Latex_Args_Init_CLI()
        
    ##!
    ##! 
    ##!
   
    def Latex_Args_Init_CLI(self):
        self.__Parser__=argparse.ArgumentParser(
            description='Generate PDF or SVG/PNG from LaTeX/TiKZ',
                add_help=True
        )

        #texfiles arguments: all remaining
        self.__Parser__.add_argument(
            dest='tex_files',
            metavar='tex_files',
            help='Files to process',
            nargs='+'
        )

        args=(
            {
                "option": 'v',
                "dest": 'Verbose',
                "action": 'store_true',
                "help": 'Verbose Echo actions taken.',
            },
            {
                "option": 's',
                "dest": 'Silent',
                "action": 'store_true',
                "help": 'Be silent.',
            },
            {
                "option": 'n',
                "dest": 'NoClean',
                "action": 'store_true',
                "help": 'Do NOT delete created files on exit.',
            },
            {
                "option": 'f',
                "dest": 'Force',
                "action": 'store_true',
                "help": 'Force regeneration even if destination files are newer.',
            },
            {
                "option": 'ff',
                "dest": 'Figs',
                "action": 'store_true',
                "help": 'Try to detect figs (<use ...>) files from log.',
            },
            {
                "option": 'l',
                "dest": 'Log',
                "action": 'store_true',
                "help": 'Display latex log on stdout.',
            },
            {
                "option": 'w',
                "dest": 'Warnings',
                "action": 'store_true',
                "help": 'Display LaTeX warnings.',
            },
            {
                "option": 't',
                "dest": 'T',
                "action": 'store',
                "help": 'Value of Parameter t, include a \\tikzmath{\T=t;} line.',
            },
            #{
            #    "option": 'o',
            #    "dest": 'OutName',
            #    "action": 'store_true',
            #    "help": 'Name of output file(s).',
            #},
            {
                "option": 'x',
                "dest": 'Exit',
                "action": 'store_true',
                "help": 'Show Arguments and Exit.',
            },
        )

        self.Latex_Args_Add(args)
        

        self.__Args__=self.__Parser__.parse_args()
            
        self.__TexFiles__=[]
        if (self.__Args__.tex_files):
            self.__TexFiles__=self.__Args__.tex_files


        self.Latex_Args_Set(args)
        if (self.__T__!=None):
            self.__Force__=True
                

        if (self.__Exit__):
            self.Latex_Args_Show(args)
            

    ##!
    ##! Show argument values
    ##!
   
    def Latex_Args_Show(self,args):
        print "Passed arguments:"
        
        for arg in args:
            attr="__"+arg[ "dest" ]+"__"

            if (hasattr(self,attr)):
                print " ".join([
                    "\t",
                    arg[ "dest" ]+":",
                    str(getattr(self,attr)),
                ])

        print "Input Files:",", ".join(self.__TexFiles__),"- Exited"
        exit()
            
    ##!
    ##! Add arguments
    ##!
   
    def Latex_Args_Add(self,args):
        for arg in args:
            self.Latex_Arg_Add(arg)
        
    ##!
    ##! Setas arguments
    ##!
   
    def Latex_Args_Set(self,args):
        for arg in args:
            self.Latex_Arg_Set(arg)
        

    ##!
    ##! 
    ##!
   
    def Latex_Arg_Add(self,arg):
        if (not arg.has_key("nargs")):
            arg[ "nargs" ]='?'
            
        self.__Parser__.add_argument(
            "-"+arg[ "option" ],
            "--"+arg[ "dest" ],
            dest=arg[ "dest" ],
            action=arg[ "action" ],
            help=arg[ "help" ]
        )
    ##!
    ##! 
    ##!
   
    def Latex_Arg_Set(self,arg):
        value=arg[ "dest" ]
        value=getattr(self.__Args__,value)
        
        setattr(self,"__"+arg[ "dest" ]+"__",value)
         
    ##!
    ##! 
    ##!
   
    def Latex_Args_Init_CGI(self):
        self.__TexFiles__=[
            "/".join([
                "/usr/local",
                self.CGI_POST("Src"),
            ])
        ]

        if (self.CGI_POST_Int("Force")==1):
            self.__Force__=True

        if (self.CGI_POST_Int("Verbose")==1):
            self.__Verbose__=True
                

        if (self.CGI_POST_Int("NoClean")==1):
            self.__NoClean___=True
                
        
    ##!
    ##! 
    ##!
   
    def Latex_Args_Test(self):
        return self.__Test__
    
    ##!
    ##! 
    ##!
   
    def Latex_Args_Tex_Files(self):
        return self.__TexFiles__

          
    ##!
    ##! 
    ##!
   
    def Latex_Args_Verbose(self):
        return self.__Verbose__
    
    ##!
    ##! 
    ##!
   
    def Latex_Args_Message(self,message,message1="",message2="",message3="",message4=""):
        if (self.Latex_Args_Verbose()):
            print message,message1,message2,message3,message4
            
    ##!
    ##! 
    ##!
   
    def Latex_Args_Force(self):
        return self.__Force__
    ##!
    ##! 
    ##!
   
    def Latex_Args_Silent(self):
        return self.__Silent__
    ##!
    ##! 
    ##!
   
    def Latex_Args_NoClean(self):
        return self.__NoClean__
    
    ##!
    ##! 
    ##!
   
    def Latex_Args_Clean(self):
        return not self.__NoClean__
