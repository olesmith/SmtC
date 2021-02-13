#!/usr/bin/python

import sys,os,time,re


import RPi.GPIO as GPIO

#State: Detected from board
#Status: Detected from stat file

global Debug
Debug=0

global Conf_File
Conf_File="/etc/gpio_pins"

global Var_Path
Var_Path="/var/lib/gpio"

global Pins_Data
Pins_Data=["No","Place",]


global Table_Keys
Table_Keys=["No","Status","State","File","Place"]


################ Read a file ################

def File_Read(fname):
    f=open(fname,"r" )
    lines=f.read()
    f.close()
    
    return lines.split('\n')

def GPIO_Name(value):
    value=int(value)
    if (value==GPIO.LOW):  return "LOW"
    if (value==GPIO.HIGH): return "HIGH"

    return "?"
    



################ Read pins configuration ################

def Pins_Conf_Read():
    lines=File_Read(Conf_File)
    
    pins={}
    for line in lines:
        if (line):
            if (re.search('^\d',line)):
                pin=Pin_Conf_Read(line)
                pins[ pin[ "No" ] ]=pin
            
    return pins

def Pin_Conf_Read(line):
    n=0

    pin={}
    for value in line.split(":"):
        key=Pins_Data[ n ]
        pin[ key ]=value 
        n+=1

    pin[ "File" ]=Var_Path+"/"+pin[ "No" ]
        
    return pin



################ Centralized setup (gpio setup call), input and output calls. ################

def GPIO_Setup(pins):
    global Debug
    
    for pinno in pins.keys():
        pin=pins[ pinno ]
        
        if (Debug):
            print "setup",pin[ "No" ]
        GPIO.setup(int(pin[ "No" ]), GPIO.OUT)
        

def GPIO_Input(pin):
    value=GPIO.input(int(pin[ "No" ]))

    global Debug
    if (Debug):
        print "input",pin[ "No" ]
    
    return value

def GPIO_Output(pin,value):
    GPIO.output(int(pin[ "No" ]),value)
       
    global Debug
    if (Debug):
        print "output",pin[ "No" ],value
        
    return 1-value


############## Set one pin ##############

def Pin_Set(pin,value,force=False):
    value=int(value)

    #Read previous value from file
    prev=Pin_State_File_Read(pin)
    
    text=GPIO_Name(value)+" PIN "+pin[ "No" ]+": "+GPIO_Name(prev)

    #(Double)Check if we should update
    if (   int(value) != int(prev) or force  ):
        
        #Set board value
        GPIO_Output(pin,value)

        #Write value to file
        curr=Pin_State_File_Read(pin)
        Pin_State_Write(pin,value)

        #Save in pin dictionary
        pin[ "State" ]=value
        
        text=text+" => "+GPIO_Name(curr)
    else:
        text=text+" Ignored"

    return text+" "+pin[ "Place" ]

############## Set several pins ##############

def Pins_High_Set(pinnos):
    for pinno in pinnos:
        if ( pins.has_key(pinno) ):
            pin=pins[ pinno ]
            Pin_Set(pin,GPIO.HIGH)
                           
def Pins_Low_Set(pinnos):
    for pinno in pinnos:
        if ( pins.has_key(pinno) ):
            pin=pins[ pinno ]
            Pin_Set(pin,GPIO.LOW)

################ Read, write and set State ################

def Pin_State_File(pin):
    global Var_Path
    return Var_Path+"/"+pin[ "No" ]

def Pin_State_File_Read(pin):
    pfile=Pin_State_File(pin)
    content=File_Read(pfile)
    return content[0]

def Pin_State_Write(pin,value):
    file=Pin_State_File(pin)
    os.system( "echo "+str(value)+" > "+Pin_State_File(pin) )

def Pin_State_Detect(pin):
    return GPIO_Input(pin)

def Pin_State_Read(pin):
    pin[ "State" ]=Pin_State_Detect(pin)
    pin[ "Status" ]=Pin_State_File_Read(pin)

    
def Pins_State_Read(pins):
    for pinno in pins.keys():
        Pin_State_Read(pins[ pinno ])

############## Restoring state ##############


def Pin_State_Restore(pin):
    global Debug
    
    if ( int(pin[ "Status" ])!=int(pin[ "State" ]) ):
        text=Pin_Set(pin,pin[ "Status" ],force=True)
        print text

def Pins_State_Restore(pins):
    global Debug
    if (Debug):
        print "State Restore...."
        
    for pinkey in pins.keys():
        Pin_State_Restore(pins[ pinkey ])
            
    if (Debug):
        print "State Restore done."

        
############## Printing ##############

        
def Pin_Print(pin):
    global Var_Path
    outfile=Pin_State_File(pin)
    
    row=[
        pin[ "No" ],
        GPIO_Name(pin[ "State" ]),
        GPIO_Name(pin[ "Status" ]),
        outfile
    ]
    print "\t".join( row )
                           
def Pins_Print(pins):
    print "Pin\tState\tStatus\tIn File"
    for pinkey in pins.keys():
        pin=pins[ pinkey ]
        Pin_Print(pin)
                           
def Pin_Table_Print(pin):
    global Var_Path
    global Table_Keys
    
    statfile=Var_Path+"/"+pin[ "No" ]
    row=[]
    for key in Table_Keys:
        row.append( str(pin[ key ]) )
    print "\t".join( row )
                           
def Pins_Table_Print(pins):
    global Table_Keys
    print "\t".join(Table_Keys)
    for pinkey in pins.keys():
        pin=pins[ pinkey ]
        Pin_Table_Print(pin)



############### Execution begin ###########################

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

command=sys.argv[0]
command=command.split("/")
command=command.pop()

pinnos=list(sys.argv)
pinnos.pop(0)

pins=Pins_Conf_Read()
GPIO_Setup(pins)
Pins_State_Read(pins)

if (command=="state_restore"):
    Pins_State_Restore(pins)
    Pins_Print(pins)
    
elif (command=="state_show"):
    Pins_Print(pins)

elif (command=="state_table"):
    Pins_Table_Print(pins)

elif (command=="high" or command=="low"):
    if (command=="high"):
        Pins_High_Set(pinnos)
    else:
        Pins_Low_Set(pinnos)
        
    pins=Pins_Conf_Read()
    Pins_State_Read(pins)
    
    Pins_Table_Print(pins)

#Uncommented, as it seems to reset changes done in this script.
#GPIO.cleanup()

exit()

