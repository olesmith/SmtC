import subprocess,os,pwd,socket

from SSH import System_SSH

class System(
        System_SSH
    ):
    chroot_bin="/usr/sbin/chroot"
    
    Ping_TTL=2
    Ping_Command=["/bin/ping","-c 1"]
    Ping_Command=["/bin/ping","-c 1"]

    #Command history
    __Commands__=[]
    
    def __init__(self):
        return
    
    def System_Add(self,commands):
        self.__Commands__.append( " ".join(commands) )
        
    def Commands_HTML(self):
        return [ self.B("Commands: ") ]+self.HTML_List(self.__Commands__)

    
    def System_Exec_PREV(self,commands):
        self.System_Add(commands)

        try:
            output=os.system(commands)
        except:
            output="Warning! Unable to execute system command: "+" ".join(commands)
        
        return output
    
    def System_Exec(self,commands,cd=None,echo=False):
        cwd=os.getcwd()
        if (cd!=None):
            os.chdir(cd)

        if (echo):
            print "Running command:"," ".join(commands)+":",

        try:
            output=os.system(" ".join(commands))
        except:
            output="Warning! Unable to execute system command: "+" ".join(commands)

        if (echo):
            print output

        if (cd!=None):
            os.chdir(cwd)

        return output

    def System_Execs(self,commands,cd=None,echo=False):
        cwd=os.getcwd()
        if (cd!=None):
            os.chdir(cd)

        res=0
        for command in commands:        
            res=res+self.System_Exec(command,None,echo)

        if (cd!=None):
            os.chdir(cwd)

        return res

    def System_Pipe(self,commands):
        self.System_Add(commands)

        output=""
        try:
            output=subprocess.check_output(
                #commands,
                [" ".join(commands)],
                shell=True,
                #stdin=p1.stdout,
                #stdout=subprocess.PIPE
            )
        except:
            output="Warning! Unable to pipe system command: "+" ".join(commands)
        
        return output
    
    def System_User_Name(self):
        return pwd.getpwuid( os.getuid() )[0]
    
    def System_Host_Name(self,host=""):
        if (not host): host=os.uname()[1]

        return socket.gethostbyaddr(host)[0]
    
    def System_Host_IP(self,host=""):
        if (not host): host=self.System_Host_Name()
        
        return socket.gethostbyaddr(host)[2][0]

    
    def System_Error_And_Die(self,msgs):
        print "\n".join(msgs)
        exit(1)
    
    def System_Make_Test(self,srcfiles,destfiles):
        src_time=self.Files_MTime(srcfiles)
        dest_time=self.Files_MTime(destfiles)

        res=True
        if (dest_time>src_time):
            res=False

        return res
        
