import pwd,os

class GPIO_Hosts():
    
    ##! 
    ##! Reads GPIO hosts from conf.
    ##!
    
    def GPIO_Hosts(self):        
        if ( len(self.Hosts)==0 ):
            hostlines=self.File_Read_Lines( self.HostsFile )
            for hostline in hostlines:
                self.GPIO_Host_Add(hostline)

        return self.Hosts

