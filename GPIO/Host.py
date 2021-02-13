import os,re


class GPIO_Host():
    ##! 
    ##! Updates host according to cgi.
    ##!
    
    def GPIO_Host_Update(self,host):
        cgihost=self.CGI_POST("Host")
        if (cgihost==host[ "Host" ]):
            self.GPIO_Pins_Update(host)

        return
    
    ##! 
    ##! Adds a host to the host list, according to input hostline.
    ##!
    
    def GPIO_Host_Add(self,hostline):
        records=hostline.split(":")

        host={}
        if ( len(records)>0 and records[0]):
            host[ "Host" ]=records[0]
            if ( len(records)>1 ):
                host[ "Title" ]=records[1]
                
            comps=re.compile("\.").split(host[ "Host" ])
            host[ "Hostname" ]=comps.pop(0)
            host[ "Domain" ]=".".join(comps)
            
            host[ "Title" ]=""
                
                        
            host[ "IP" ]=self.System_Host_IP(host[ "Host" ])
            
            self.Hosts.append( host )
            self.GPIO_Host_Alive_Detect(host)
            self.GPIO_Host_Read(host)

            self.GPIO_Host_Update(host)
        
        return host
    
    ##! 
    ##! Tries to obtain host info via SSH
    ##!
    def GPIO_Host_Read(self,host):
        self.GPIO_Pins_Read(host)
    
    ##! 
    ##! Returns text to show for host in left menu.
    ##!
    
    def GPIO_Host_Menu_Text(self,host):
        text=[
            host[ "Title" ],
            "("+host[ "Host" ]+"): ",
            self.GPIO_Host_Alive_Text(host)
        ]
        return " ".join(text)
    
    ##! 
    ##! Tests if host is alive
    ##!
    
    def GPIO_Host_Alive_Command(self,host):
        commands=list(self.Ping_Command)
        commands.append( "-W"+str(self.Ping_TTL) )
        commands.append( host[ "Host" ] )
        commands.append( ">" )
        commands.append( "/dev/null 2>&1;" )
        
        return " ".join( commands )
    
    ##! 
    ##! Tests if host is alive
    ##!
    
    def GPIO_Host_Alive_Detect(self,host):
        host[ "Alive" ]=False
        command=self.GPIO_Host_Alive_Command(host)
        res=os.system( command )

        if (res==0):
            host[ "Alive" ]=True
        else:
            print "Host '"+host[ "Host" ]+"' unreachable: "+str(res)
            print "Command: "+command
            exit()
        
        return host[ "Alive" ]
    
    ##! 
    ##! Returns up/down for host
    ##!
    
    def GPIO_Host_Alive_Text(self,host):
        cell="Down"
        if ( host[ "Alive" ] ):
            cell="Up"
            
        return cell
    
    ##! 
    ##! Generates HTML pins table for host
    ##!
    
    def GPIO_Host_Table(self,host):
        html=[]
        html=html+[
            self.HTML_Table(
                self.GPIO_Pins_Table(host),
                self.GPIO_Pins_Table_Titles(),
                [],
                {},
                {},
                { "align": 'center', }
            )
        ]
            
        return html
