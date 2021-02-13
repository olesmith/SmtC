import re

class GPIO_Pin():
    ##! 
    ##! Read pin from pinline
    ##!
    
    def GPIO_Pin_Read(self,host,pinline):
        comps=pinline.split("\t")

        pin={}
        for key in ["No","Status","State","Type","Neutral","File","Place"]:
            pin[ key ]=""
            if ( len(comps)>0 ):
                pin[ key ]=comps.pop(0)

        host[ "Pins" ].append(pin)

        return pin
    
    ##! 
    ##! Reads hdt11 status from host/pin.
    ##!
    
    def GPIO_Pin_HDT_Detect(self,host,pin):
        output=self.System_SSH_Pipe(
            host,
            self.GPIO_Pin_HDT11_Command(pin)
        )
        output=re.compile("\s").split(output)

        messages=[]
        if ( len(output)>0 ):
            messages.append(output[0]+"&ordm;C")
            
        if ( len(output)>1 ):
            messages.append(output[1]+"%")
            
        return [ " ".join(messages) ]
    ##! 
    ##! Reads status from host/pin.
    ##!
    
    def GPIO_Pin_Status_Detect(self,host,pin):
        output=self.System_SSH_Pipe(
            host,
            self.GPIO_Pin_Status_Command(pin)
        )
        output=int(output)

        status="??"
        if (output==1):
            status=False
        elif (output==0):
            status=True

        pin[ "Status" ]=status

        return 1-pin[ "Status" ]
    
    ##! 
    ##! Generates row for pin table
    ##!
    
    def GPIO_Pin_Table_Row(self,host,pin):
        row=[]
        if (pin[ "Type" ]=="gpio"):
            for key in self.GPIO_Pins_Table_Datas:
                row.append( pin[ key ] )
            
            row.append( self.GPIO_Pin_Status_Text(host,pin) )
            row.append( self.GPIO_Pin_Status_Change(host,pin) )
                    
        return row
    
    ##! 
    ##! Generates pins table title row
    ##!
    
    def GPIO_Pins_Table_Titles(self):
        row=[]
        for key in self.GPIO_Pins_Table_Datas:
            row.append( self.B( key ) )
            
        row.append("")
        row.append("")
        
        return row
    
    ##! 
    ##! Creates pins all on/off row for host.
    ##!
    
    def GPIO_Pins_Table_All_Row(self,host):
        row=[]
        for key in self.GPIO_Pins_Table_Datas:
            row.append( "---")

        row.append( "---" )
        row.append(
            self.GPIO_Pins_All_On_Cell(host)+" "+self.GPIO_Pins_All_Off_Cell(host)
        )

        return row
    
    
    ##! 
    ##! Returns status icon according to pin[ "State" ]
    ##!
    
    def GPIO_Pin_Status_Icon(self,host,pin):
        icon="??"

        if (int(pin[ "Status" ])==0):
            if (pin.has_key("Neutral") and int(pin[ "Neutral" ])==0):
                icon="on.jpg"
            else:
                icon="off.jpg"
        elif (int(pin[ "Status" ])==1):
            if (pin.has_key("Neutral") and int(pin[ "Neutral" ])==0):
                icon="off.jpg"
            else:
                icon="on.jpg"
            
        return icon
    ##! 
    ##! Returns status text for pin: icon link to alter
    ##!
    
    def GPIO_Pin_Status_Text(self,host,pin):
        text="??"
        if ( int(pin[ "Status" ])==0):
            text="HIGH"
        elif ( int(pin[ "Status" ])==1):
            text="LOW"

        return text
    ##! 
    ##! Returns status title according to pin[ "State" ]
    ##!
    
    def GPIO_Pin_Status_Title(self,host,pin):
        text="Switch On"
        if (pin[ "Status" ]):
            text="Switch Off"

        return text
    ##! 
    ##! Returns status image according to pin[ "State" ]
    ##!
    
    def GPIO_Pin_Status_IMG(self,host,pin):
        icon=self.GPIO_Pin_Status_Icon(host,pin)
        return self.IMG(
            "/".join( [ self.HTML_Icons,icon ] ),
            icon,
            {
                "height": self.Icon_Size,
                "width": self.Icon_Size,
            }
        )
        
    ##! 
    ##! Returns status url according to pin[ "State" ]
    ##!
    
    def GPIO_Pin_Status_URL(self,host,pin):
        status=int(pin[ "Status" ])

        args=[]
        if ( 'Host' in host.keys() ):
            args.append( "Host=" + host[ "Host" ] )
            
        if ( 'No' in pin.keys() ):
            args.append( "Pin=" + pin[ "No" ] )
        if ( 'All' in pin.keys() ):
            args.append( "All=1" )
            
            
        if (status==1):
            args.append( "Status=1" )
        elif (status==0):
            args.append( "Status=0" )

            
        return "?"+"&".join(args)
    ##! 
    ##! Returns status icon link for pin: icon link to alter
    ##!
    
    def GPIO_Pin_Status_Change(self,host,pin):
        return self.A(
            self.GPIO_Pin_Status_URL(host,pin),
            self.GPIO_Pin_Status_IMG(host,pin),
            { "title": self.GPIO_Pin_Status_Title(host,pin), }
        )
        
    ##! 
    ##! Returns status read command for pin
    ##!
    
    def GPIO_Pin_Status_Command(self,pin):
        commands=[]
        commands.append(
            "/".join( [
                self.GPIO_Path,self.GPIO_Pin_State_Command
            ] )
        )
        commands.append( pin[ "No" ] )
       
        return commands
  
    ##! 
    ##! Returns status read command for pin
    ##!
    
    def GPIO_Pin_HDT11_Command(self,pin):
        commands=[]
        commands.append(
            "/".join( [
                self.GPIO_Path,self.GPIO_Pin_HDT_Command
            ] )
        )
        
        commands.append( pin[ "No" ] )
       
        return commands
  
    
