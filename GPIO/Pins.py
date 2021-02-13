import re

class GPIO_Pins():

    ##! 
    ##! Reads all pins on host
    ##!
    
    def GPIO_Pins_Read(self,host):
        host[ "Pins" ]=[]
        if ( host[ "Alive" ] ):
            cell="Up"
            commands=[
                "/".join( [ self.GPIO_Path,self.GPIO_Pin_Table_Command ] )
            ]
            
            #Runs system call to generate 
            pinlines=self.System_SSH_Pipe(host,commands)
            pinlines=pinlines.split('\n')

            rpinlines=[]
            for pinline in pinlines:
                rpinline=str(pinline)

                if (   re.search('^\d+',pinline)   ):
                    rpinlines.append( rpinline )

            for pinline in rpinlines:
                 if (pinline):
                    self.GPIO_Pin_Read(host,pinline)

        
        return host[ "Pins" ]
    
    ##! 
    ##! Updates host[ "Pins" ] according to cgi.
    ##!
    
    def GPIO_Pins_Update(self,host):
        cgipin=self.CGI_POST_Int("Pin")
        all=self.CGI_POST_Int("All")

        cgipins=[]
        if (all==1):
            for pin in host[ "Pins" ]:
                cgipins.append( pin[ "No" ] )

        elif (cgipin):
            cgipin=str(cgipin)
            for pin in host[ "Pins" ]:
                if ( pin[ "No" ]==cgipin ):
                    cgipins.append( cgipin )
                    
        if (not cgipins):
            return False

        status=self.CGI_POST_Int("Status")
        if (status==0):
            self.GPIO_Pins_High_Set(host,cgipins)
            
        if (status==1):
            self.GPIO_Pins_Low_Set(host,cgipins)
            
        self.GPIO_Pins_Read(host)
        return True

    
    ##! 
    ##! Creates pins table for host.
    ##!
    
    def GPIO_HDT11_Pin(self,host):
        for pin in host[ "Pins" ]:
            if (pin[ "Type" ]=="hdt11"):
                return pin

        return None
                
    ##! 
    ##! Creates pins table for host.
    ##!
    
    def GPIO_HDT11_Message(self,host):
        pin=self.GPIO_HDT11_Pin(host)

        message="-"
        if (pin!=None):
            message=self.GPIO_Pin_HDT_Detect(host,pin)

        return message
    
    ##! 
    ##! Creates pins table for host.
    ##!
    
    def GPIO_Pins_Table(self,host):
        table=[]
        
        pins={}
        for pin in host[ "Pins" ]:
            pins[ pin[ "Place" ] ]=pin

        rpins=pins.keys()
        rpins.sort()

        dht11pin=None
        haspins=False
        for rpin in rpins:
            pin=pins[ rpin ]
            if (pin[ "Type" ]=="gpio"):
                haspins=True
                table.append( self.GPIO_Pin_Table_Row(host,pin) )
                
        #if (haspins):
        #    table.append( self.GPIO_Pins_Table_All_Row(host) )
            
        return table
    
    ##! 
    ##! Creates pins all off cell for host.
    ##!
    
    def GPIO_Pins_All_Off_Cell(self,host):
        return self.GPIO_Pin_Status_Change(
            host,
            {
                "Status": False,
                "All": "1",
            }
        )
    
    ##! 
    ##! Creates pins all on cell for host.
    ##!
    
    def GPIO_Pins_All_On_Cell(self,host):
        return self.GPIO_Pin_Status_Change(
            host,
            {
                "Status": True,
                "All": "1",
            }
        )
    
    ##! 
    ##! Returns on command for pin
    ##!
    
    def GPIO_Pins_High_System_Get(self,host):
        commands=[]
        commands.append(
            "/".join( [
                self.GPIO_Path,self.GPIO_Pins_High_Command
            ] )
        )
        
        return commands
    
    ##! 
    ##! Turns on all host pins.
    ##!
    
    def GPIO_Pins_High_Set(self,host,cgipins):
        commands=self.GPIO_Pins_High_System_Get(host)
        commands=commands+cgipins

        res=self.System_SSH_Pipe(
            host,
            commands
        )
    
        self.HTML_Message_Add(
            [
                self.B("Host: ")+host[ "Host" ],
                self.B("Turned On:")+self.BR()+", ".join(cgipins),
            ]
        )

    ##! 
    ##! Returns on command for pin
    ##!
    
    def GPIO_Pins_Low_System_Get(self,host):
        commands=[]
        commands.append(
            "/".join( [
                self.GPIO_Path,self.GPIO_Pins_Low_Command
            ] )
        )
        
        return commands
    
    ##! 
    ##! Turns off all host pins.
    ##!
    
    def GPIO_Pins_Low_Set(self,host,cgipins):
        commands=self.GPIO_Pins_Low_System_Get(host)
        commands=commands+cgipins

        res=self.System_SSH_Pipe(
            host,
            commands
        )
        
        self.HTML_Message_Add(
            [
                self.B("Host: ")+host[ "Host" ],
                self.B("Turned Off:")+self.BR()+", ".join(cgipins),
            ]
        )
