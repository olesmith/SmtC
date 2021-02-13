from subprocess import call
import os,sys,re,glob

def Format_Real(t):
    return "%.6f" % t


def Max(x1,x2):
    if (x2>x1):
        return x2

    return x1

def Min(x1,x2):
    if (x2<x1):
        return x2

    return x1

def Intervals(t1,t2,n):
    dt=(t2-t1)/(1.0*n)
    t=t1
    ts=[]
    for i in range( n+1 ):
        ts.append(t)
        t+=dt
        
    return ts

def t2Interval(ts,t):
    j=-1
    for k in range(1, len(ts) ):
        if (t>=ts[k-1] and t<ts[k]):
            j=k

    return j


def Convex(v,w,eta):
    return v*(1.0-eta) +w*eta
    
def System(command,switches,args1,args2=[]):
    for switch in switches:
        if (switches[ switch ].__class__.__name__=="int"):
            switches[ switch ]=str(switches[ switch ])
        command+=" "+switch+" "+switches[ switch ]

    for arg in args1:
        command+=" "+arg
        
    for arg in args2:
        command+=" "+arg

    os.system(command)
    return command
    
def List_Slice(items,n):
    ritems=[[]]
    current=0
    for item in items:
        ritems[ current ].append(item)
        if ( len(ritems[ current ])>=n ):
            ritems.append([])
            current+=1
        
    return ritems

from Args import Args
from File import File
from Path import Path

class Base(Args,File,Path):

    ClassName=""
   
    def __init__(self):
        return

    
    def GetClassName(self):
        print "ClassName",self.ClassName
        value=self.ClassName
        if (value==""):
            self.ClassName=self.__class__.__name__

        return self.ClassName


    def Hash2Obj(self,vals):
        for x in vals:
            setattr(self, x, vals[x] )

    ##! ??? defunct
    
    def get_class_members(self,klass):
        print "9999999999999999",klass
        
        ret = dir(klass)
        if hasattr(klass,'__bases__'):
            print "9999999999999999",klass.__bases__
            for base in klass.__bases__:
                ret = ret + get_class_members(base)
        return
    
    def File_2_Dict(self,file):
        f=open(file,'r')
        lines=f.read()
        f.close()
        lines=lines.splitlines()

        dict={}
        for line in lines:
            comps=re.split(r'\s*[:=]\s*', line)
            if (len(comps)==2):
                attr=comps[0]
                attr=re.sub(r'\s+',"",attr)
                value=comps[1]
                value=re.sub(r'^\s+',"",value)
                value=re.sub(r'\s+$',"",value)
                value=re.sub(r',$',"",value)
                dict[ attr ]=value
        return dict

    
    ##!
    ##! Color Convex Combination
    ##!
    
    def Color_Convex(self,t,color1,color2):
        color=color1*(1.0-t)+color2*t
        for i in range( len(color) ):
            color[i]=str(int(color[i]))
            
        return "rgb("+",".join(color)+")"
    
