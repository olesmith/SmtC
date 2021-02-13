

class Display_Body():
    
    ##! 
    ##! Generates HTML BODY.
    ##!
    
    def Display_Body(self):
        html=[]
        
        html=html+[ self.XML_Tag_Start("BODY") ]
        
        args={
            "width": "100%",
            "border": "1",
        }

        html=html+[ self.XML_Tag_Start("TABLE",args) ]   

        html=html+self.Display_Top()
        html=html+self.Display_Middle()
        html=html+self.Display_Bottom()
        
        html=html+[ self.XML_Tag_End("TABLE") ]
        
        html=html+[ self.XML_Tag_End("BODY") ]

        return html
    
    def Display_Cell(self,horisontal,vertical):
        html=[]

        ##hack to make css classes become right
        if (horisontal=="Top"):      n=0
        elif (horisontal=="Middle"): n=1
        else:                        n=2
        
        if (horisontal=="Left"):     m=0
        elif (horisontal=="Center"): m=1
        else:                        m=2

        widths={
            "Left":   "20%",
            "Center": "70%",
            "Right":  "10%",
        }

        args={
            "width": widths[ vertical ],
            #"class": horisontal+"_"+vertical
            "class": " ".join([
                self.Body_Matrix_TR_CSS[ n ]+" "+self.Body_Matrix_TD_CSS[ m ],
            ]),
        }
        
        html=html+[ self.XML_Tag_Start("TD",args) ]     

        method="Display_"+horisontal+"_"+vertical+"_Cell"
        if (hasattr(self,method)):
            method=getattr(self,method)
            html=html+method()
        else:
            html=html+[ horisontal+"_"+vertical ]
            
        
        html=html+[ self.XML_Tag_End("TD") ]       
        

        return html
