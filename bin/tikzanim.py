#!/usr/bin/python

import sys,argparse,os

sys.path.append("/usr/local/Python")

from File import *
from Path import *
from System import *
from Latex import *
from CGI import *



##
## Generates SVG animation from tikz.tex.



if (CGI().CGI_Is()):
    import cgitb
    cgitb.enable()


class Animation(File,Path,System):
    
    def __init__(self):

        self.Animation_Args_Init_CLI()
        self.Animation_Run()
        
    ##!
    ##! 
    ##!
   
    def Animation_Args_Init_CLI(self):
        self.__Parser__=argparse.ArgumentParser(
            description='Generate SVG using TikZ',
                add_help=True
        )

        #tex/tikz file
        self.__Parser__.add_argument(
            dest='Files',
            metavar='Files',
            help='File(s) to process',
            nargs='+'
        )

        self.Files=[];
        self.path="./Images";
        self.t1=0.0;
        self.t2=1.0;
        self.n=5;

        args=(
            {
                "option": 'p',
                "dest": 'path',
                "default": self.path,
                "action": 'store',
                "help": 'Path to store images in (default: '+self.path+').',
            },
            {
                "option": 't1',
                "dest": 't1',
                "default": self.t1,
                "action": 'store',
                "help": 'First value of Parameter t.',
            },
            {
                "option": 't2',
                "dest": 't2',
                "default": self.t2,
                "action": 'store',
                "help": 'Last value of Parameter t.',
            },
            {
                "option": 'n',
                "dest": 'n',
                "default": self.n,
                "action": 'store',
                "help": 'Number of frames.',
            },
            {
                "option": 'x',
                "dest": 'Exit',
                "action": 'store_true',
                "help": 'Show Arguments and Exit.',
                
            },
        )

        self.Animation_Args_Add(args)
        

        self.__Args__=self.__Parser__.parse_args()
            
        self.Files=[]
        if (self.__Args__.Files):
            self.Files=self.__Args__.Files


        self.Animation_Args_Set(args)                

        if (self.Exit):
            self.Animation_Args_Show(args)
            

    ##!
    ##! Show argument values
    ##!
   
    def Animation_Args_Show(self,args):
        print "Passed arguments:"
        
        for arg in args:
            attr=arg[ "dest" ]

            if (hasattr(self,attr)):
                print " ".join([
                    "\t",
                    arg[ "dest" ]+":",
                    str(getattr(self,attr)),
                ])

        print "Input Files:",", ".join(self.Files),"- Exited"
        exit()
            
    ##!
    ##! Add arguments
    ##!
   
    def Animation_Args_Add(self,args):
        for arg in args:
            self.Animation_Arg_Add(arg)
        
    ##!
    ##! Setas arguments
    ##!
   
    def Animation_Args_Set(self,args):
        for arg in args:
            self.Animation_Arg_Set(arg)
        

    ##!
    ##! 
    ##!
   
    def Animation_Arg_Add(self,arg):            
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
   
    def Animation_Arg_Set(self,arg):
        value=arg[ "dest" ]
        value=getattr(self.__Args__,value)

        if (value==None and arg.has_key("default")):
            value=arg[ "default" ]
        
        setattr(self,arg[ "dest" ],value)
         
    ##!
    ##! 
    ##!
   
    def Animation_Run(self):
        command=[
            "/usr/local/bin/tikz2svg",
            "-n",
        ]
        
        if (not self.Path_Exists(self.path)):
            self.Path_Create(self.path)

        tex_name=self.Files[0]
        base_name=re.sub('(\.tikz)?\.tex$',"",tex_name)
        
        self.t1=float(self.t1)
        self.t2=float(self.t2)
        self.n=int(self.n)

        self.dt=(self.t2-self.t1)/(1.0*(self.n-1))
        print self.path,",",tex_name,":",self.t1,"-",self.t2,":",self.n
        for n in range(self.n):
            self.t=self.t1+n*self.dt
            
            rcommand=command+[
                "-t",
                str(self.t)
            ]+self.Files

            res=self.System_Exec(rcommand,None,True)

            if (res): exit()
            
            n_sort="%03d" % n
            out_name=base_name+"-"+n_sort

            for extension in ["svg"]:
                if (self.File_Exists(base_name+"."+extension)):
                    self.System_Exec(
                        [
                            "cp -p",
                            base_name+"."+extension,
                            "/".join([
                                self.path,
                                out_name+"."+extension
                            ])
                        ],
                        None,True
                    )
        

anim=Animation()
