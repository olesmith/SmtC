import time,re

#move with Command_
import subprocess

from System import System
from CGI import *
from HTML import HTML

from Hosts import GPIO_Hosts
from Host import GPIO_Host
from Pins import GPIO_Pins
from Pin import GPIO_Pin

class GPIO(
        System,CGI,HTML,
        GPIO_Host,
        GPIO_Hosts,
        GPIO_Pin,
        GPIO_Pins
    ):

    
    CSSs=[ "/W3.css","/GPIO.css", ]

    App_Name="My GPIO Control"
    DocRoot="/usr/local/gpio"
    Title="GPIO Control"
    Titles=[
        "GPIO Control",
        "Ole Peter Smith",
        "Instituto de Matem&aacute;tica e Estat&iacute;stica",
        "Universidade Federal de Goi&aacute;s",
    ]

    HostsFile="/etc/gpio_hosts"
    Hosts=[]
    Icon_Size="20px"
    
    HTML_Top_Logos=[
        "/icons/ufg.png",
        "/icons/cora.png"
    ]
    
    HTML_Bottom_Logos=[
        "/icons/sade_owl.png",
        "/icons/kierkegaard.png",
        "/icons/sade_owl.png"
    ]

    Hosts_Per_Line=1

    SSH_Public_Key_Dir="/var/www/.ssh"
    SSH_Public_Key_File="id_rsa.pub"
    SSH_Host_File="known_hosts"
    Pins_Conf_File="/etc/gpio_pins"
    Pins_User="pi"
    
    GPIO_Path="/usr/local/gpio"
    GPIO_Pin_Up_Command="up"
    GPIO_Pin_Down_Command="down"
    GPIO_Pin_State_Command="state"
    GPIO_Pin_HDT_Command="dht"

    
    GPIO_Pins_High_Command="high"
    GPIO_Pins_Low_Command="low"
    
    GPIO_Pin_Table_Command="state_table"

    GPIO_Pins_Table_Datas=["No", "Type","Place", "State", "Status", "Neutral","File" ]
    
    def __init__(self):
        self.CGI_HTTP_Header_Print()
        self.CGI_Init()
        agent=self.CGI_ENV_Get('HTTP_USER_AGENT')
        if (re.search('Android',agent) or self.CGI_POST_Int("Cell")==1):
            self.Body_Matrix=[
                [ "Middle_Center", ],
            ]
    
            self.Body_Matrix_CSS=[
                [ "MiddleCenter", ],
            ]
    
            self.Body_Matrix_TR_CSS=[ "MiddleRow", ]
            self.Body_Matrix_TR_Heights=[ "100%" ]
    
            self.Body_Matrix_TD_CSS=[ "CenterCol" ]
            self.Body_Matrix_TD_Widths=[ "100%" ]
            self.Cell_Mode=True
            self.GPIO_Pins_Table_Datas=["No", "Place", "State", "Status" ]
            self.Icon_Size="100px"
        return

    def App_Comment(self,comments):
        if (comments.__class__.__name__!="list"):
            comments=[ comments ]

        html=""
        for comment in comments:
            html=html+"<!-- **** "+self.App_Name+": "+comment+" -->\n"

        return html
    
    
    def GPIO_CGI_Path(self):
        return self.__GET__[ "Path" ]
    
    def GPIO_CGI_Paths(self):
        return self.GPIO_CGI_Path().split("/")
        
    def Run_old(self):
        html=""

        html=html+self.App_Comment("HTML_Header START")
        html=html+self.HTML_Header()
        html=html+self.App_Comment("HTML_Header END")
        
        html=html+self.App_Comment("HTML_Body START")
        html=html+self.HTML_Body()
        html=html+self.App_Comment("HTML_Body END")

        html=html+self.App_Comment("HTML_Tailer START")
        html=html+self.HTML_Tailer()
        html=html+self.App_Comment("HTML_Tailer END")
        

        print html
        return

    
    ##! 
    ##! Generates application main menu.
    ##!
    
    def HTML_Left_Menu(self):
        hlist=[]
        for host in self.GPIO_Hosts():
            hlist.append( self.GPIO_Host_Menu_Text(host) )

        return [self.H(1,"List of Hosts")]+self.HTML_List(hlist)

    
    ##! 
    ##! Generates video section. Off.
    ##!
    
    def HTML_Central_Video(self):
        videoargs={
            "width": '320',
            "height": '240',
            "controls": '',
        }
        sourceargs={
            "src": 'http://127.0.0.1/cam2.mpg',
            "type": 'video/mp4', #; codecs="avc1.42E01E, mp4a.40.2"',
        }

        
        
        html=[
            self.XML_Tag_Start("VIDEO",videoargs),
            self.XML_Tag_Start("SOURCE",sourceargs),
            'Your browser does not support the video tag.\n',
            self.XML_Tag_End("VIDEO")+"\n",
        ]

        return html
    
    ##! 
    ##! Generates localhost SSH key path message
    ##!
    
    def HTML_Local_Host_Path_Message(self):
        msg=self.SSH_Public_Key_Dir+": OK"
        if (not self.Path_Exists(self.SSH_Public_Key_Dir) ):
            msg="<BR>".join(
                    self.System_SSH_Local_Host_Dir_Error_Messages()
            )

        return msg

    ##! 
    ##! Generates localhost SSH key file message
    ##!
    
    def HTML_Local_Host_File_Message(self):
        msg=self.System_SSH_Local_Host_Key_File()+": OK"
        if (not self.File_Exists(self.System_SSH_Local_Host_Key_File() ) ):
            msg="<BR>".join(
                self.System_SSH_Local_Host_File_Error_Messages()
            )
 
        return msg
    
    ##! 
    ##! Generates localhost info table
    ##!
    
    def HTML_Local_Host_Info_Table(self):
        return [
            [
                self.B("Host:"),
                self.System_Host_Name(),
            ],
            [
                self.B("IP:"),
                self.System_Host_IP(),
            ],
            [
                self.B("Local User:"),
                self.System_User_Name(),
            ],
            [
                self.B("CGI User:"),
                self.CGI_ENV_Get("REMOTE_USER"),
            ],
            [
                self.B("Public Key Dir:"),
                self.HTML_Local_Host_Path_Message()
            ],
            [
                self.B("Public Key File:"),
                self.HTML_Local_Host_File_Message()
            ]
        ]

    ##! 
    ##! Generates localhost info
    ##!
    def HTML_Local_Host_Info(self):
    
        return self.HTML_Table(
            self.HTML_Local_Host_Info_Table(),
            [],[],
            {
                "border": "1px",
                "align": 'center',
                "width": "50%",
            }
        )
    
    ##! 
    ##! Generates host info table
    ##!
    
    def HTML_Host_Info_Table(self,host):
        return [
            [
                self.B("CGI Host/IP:"),
                host[ "Hostname" ]+self.B(".")+host[ "Domain" ]+": "+host[ "IP" ],
            ],
            [
                self.B("SSH Connect:"),
                self.System_SSH_Host_Error_Message(host)
            ]
        ]
    
    ##! 
    ##! Generates host info
    ##!
    def HTML_Host_Info(self,host):
        return self.HTML_Table(
            self.HTML_Host_Info_Table(host),
            [],[],
            {
                "border": "1px",
                "align": 'center',
                "width": "100%",
            }
        )
    
    ##! 
    ##! Generates central screen.
    ##!
    
    def HTML_Central_Screen(self):
        html=[]
        html=html+[
            self.H(1,"GPIO CGI Host: Raspberries"),
        ]
        
        for host in self.GPIO_Hosts():
            html=html+[
                self.HTML_Table(
                    [
                        [
                            self.H(2,host[ "Host" ]),
                            ],
                        [
                            self.H(3,self.GPIO_HDT11_Message(host)),
                        ],
                        self.GPIO_Host_Table(host),
                        [ self.HTML_Host_Info(host) ],
                    ],
                    [],[],
                    {
                        "border": "1px",
                        "align": 'center',
                    }
                )+["<BR>"]
            ]
                  
        if (not self.Cell_Mode):
            html=html+self.Commands_HTML()
            
        html=html+[
            self.HTML_Local_Host_Info()
        ]
        

        return html
        
