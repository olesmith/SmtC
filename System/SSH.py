import subprocess,os,re

class System_SSH():
    SSH_Commands=["/usr/bin/ssh" ]
    
    def System_SSH_Host(self,host):
        return self.Pins_User+"@"+host[ "Host" ]
    
    def System_SSH_Quote(self,commands):
        return " ".join(commands)
        #Does not proceed
        #return "'"+" ".join(commands)+"'"
    
    def System_SSH_Pipe(self,host,commands):
        output=""
        if ( host[ "Alive" ] ):
            
            scommands=list( self.SSH_Commands )
            scommands.append( self.System_SSH_Host(host) )
            scommands.append( self.System_SSH_Quote(commands) )
        
            output=self.System_Pipe(scommands)

        return output
    
    def System_SSH_Remote_File_Read(self,host,srcfile):
        return self.System_SSH_Pipe(
            host,
            [
                "/bin/cat",
                self.Pins_Conf_File,
            ]
        )
    
    def System_SSH_User_At_Local_Host(self,host="",user=""):
        if (not user): user=self.System_User_Name()
        if (not host): host=self.System_Host_Name()
        
        return user+"@"+host
    
    def System_SSH_Local_Host_Key_File(self):
        return "/".join( [ self.SSH_Public_Key_Dir,self.SSH_Public_Key_File ] )

    
    def System_SSH_Local_Host_Dir_Error_Messages(self):
        return [
            "No SSH Public Key directory found: "+self.SSH_Public_Key_Dir,
            " ".join( [ "/bin/mkdir",self.SSH_Public_Key_Dir ] )
        ]
        
    def System_SSH_Local_Host_File_Error_Messages(self):
        return [
            "No SSH Public Key found, in:",
            "",
            self.System_SSH_Local_Host_Key_File(),
            "",
            "To generate, please run as user:",
            "",
            self.System_SSH_User_At_Local_Host()+"):",
            " ".join([
                "/usr/bin/ssh-keygen",
                "-G",self.System_SSH_Local_Host_Key_File(),
                "-t","rsa",
                "-C",
                self.System_SSH_User_At_Local_Host()
            ])
        ]
        
    def System_SSH_Local_Host_Test(self):
        if (not self.Path_Exists(self.SSH_Public_Key_Dir) ):
            print "<BR>".join(
                self.System_SSH_Local_Host_Dir_Error_Messages()
            )
            
        if (not self.File_Exists( self.System_SSH_Local_Host_Key_File() ) ):
            print "<BR>".join(
                self.System_SSH_Local_Host_File_Error_Messages()
            )
            

        
    def System_SSH_Local_Host_Public_Key_Error_Messages(self,host,output):
        return [
            output,
            "Probably local SSH public key has not been transfered to board",
            "To transfer the key, as "+self.System_SSH_User_At_Local_Host()+", run:",
            " ".join( [
                "usr/bin/ssh-copy-id",
                "-i","/".join( [
                    self.SSH_Public_Key_Dir,
                    self.SSH_Public_Key_File,
                ] ),
                self.System_SSH_User_At_Local_Host(),
            ] )
        ]
            
        
    def System_SSH_Host_Error_Message(self,host):
        hostsfile="/".join( [self.SSH_Public_Key_Dir,self.SSH_Host_File] )

        msgs=[ hostsfile+": OK" ]
        if (self.File_Exists(hostsfile) ):
            lines=self.File_Read(hostsfile)
            print host.keys()
            
            if (not re.search(host[ "Hostname" ],lines) ):
                msgs=[
                    hostsfile+" exists, but cannot detect presence of host",
                    "This may occur, if HashKnownHosts is off in /etc/ssh/ssh_config"
                ]
        else:
            msgs=[ hostsfile+": non-existent" ]
                
        return "<BR>".join( msgs)
 
