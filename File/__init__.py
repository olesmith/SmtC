import os,datetime,time

from time import *
from Path import *
from System import *

class File(System):
    def File_Path_Create(self,fname):
        paths=fname.split('/')
        paths.pop()

        Path().Path_Create( "/".join(paths) )

    def File_BaseName(self,fname):
        paths=fname.split('/')

        return paths.pop()

    def File_PathName(self,fname):
        paths=fname.split('/')

        paths.pop()
        return "/".join(paths)

    def File_Exists(self,fname):
        return os.path.isfile(fname) or os.path.isdir(fname) or os.path.islink(fname)

    def File_MTime(self,fname):
        mtime=-1
        if (self.File_Exists(fname)):
            mtime=os.path.getmtime(fname)
     
        return mtime

    def Files_MTimes(self,files):
        mtimes=[]
        for fname in files:
            if (fname!=None):
                mtimes.append( self.File_MTime(fname) )
        
        return mtimes

    def Files_MTime(self,files):

        mtimes=self.Files_MTimes(files)

        mtime=0
        if ( len(mtimes)>0 ):
            mtime=max(mtimes)
            
        return mtime

    def Time_Show(self,mtime):
        info=localtime(mtime)
    
        return strftime("%d %b %Y, %H:%M:%S",info)

    def File_Path(self,file):
        paths=file.split('/')
        paths.pop()

        return "/".join(paths)

    def File_Read(self,fname):
        f=open(fname,"r" )
        lines=f.read()

        f.close()

        return lines
    
    def File_Writeable(self,fname):
        if (not self.File_Exists(fname)):
            path=self.File_PathName(fname)
            if (path==""): path="./"

            return os.access(path, os.W_OK)
            
        return os.access(fname, os.W_OK)

    def File_Read_Lines(self,fname):
        lines=self.File_Read(fname)

        return lines.split("\n")

    def File_Write(self,fname,lines,tell=False):        
        self.File_Path_Create(fname)
        f=open(fname,"w" )

        if (type(lines)!='list'):
            rlines=[lines]
        
        size=0
        for line in lines:
            f.write("%s\n" % line)
            size+=len(line)

        if (tell): 
            print str(size),"bytes written to",fname
            
        f.close()

        return size

    def Files_Make_Command(self,src_files,dest_files,commands,force=False,echo=False):
        src_time=File().Files_MTimes(src_files)
        dest_time=File().Files_MTimes(dest_files)

 
        res=-1
        if (force or dest_time<src_time):
            if (echo):
                print "Running command:","\t"+" ".join(commands)+":",
        
            res=System().System_Exec(commands)
            if (echo):
                print res
        else:
            if (echo): print "src_files are up to date"
            res=1
            
        return res

    
    def File_Rename(self,src,dest,echo=False):

        if (not self.File_Exists(src)):
            print "File_Rename: Source file:",src,"non-existent"
            exit()
            return -1
        
        if (not self.File_Writeable(dest)):
            print "File_Rename: Destination file:",dest,"not writable"
            exit()
            return -1
        
        if (echo): print "Moving",src,"->",dest
        
        return System().System_Exec([
            "/bin/mv",
            src,
            dest
        ])

    def Files_Unlink(self,files,echo=False):
        commands=[
            "/bin/rm",
            "-f",
        ]

        if (echo): print "Unlink:\n\t",'\n\t'.join(files)
        for fname in files:
            commands.append(fname)
             
        return self.System_Exec(commands,None,echo)
    
    def File_Unlink(self,fname,echo=False):
        commands=[
            "/bin/rm",
            "-f",
            fname
        ]

        if (echo): print "Unlink:\n\t",'\n\t'.fname

        return self.System_Exec(commands,None,echo)
            
            
        return res
def File_Read(name):
    fobj=File().File_Read(name)
    
def File_Write(name,lines,tell=False):
    fobj=File().File_Write(name,lines,tell)
    
def File_Exists(name):
    return File().File_Exists(name)
    
def File_Size(name):
    statinfo = os.stat(fname)
    return os.path.getsize(fname)
    return statinfo.st_size
    
