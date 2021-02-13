class HTML_Body():
    ##! 
    ##! Generates HTML BODY.
    ##!
    
    def HTML_Body(self):
        html=[]
        html=html+[ self.XML_Tag_Start("BODY") ]
        html=html+[ self.HTML_Body_Matrix() ]
        html=html+[ self.XML_Tag_End("BODY") ]

        return [html]
    
    ##! 
    ##! Generates HTML BODY.
    ##!
    
    def HTML_Body_Matrix(self):
        args={
            "class": "Body_Table",
        }
        
        html=[]
        html=html+[ self.XML_Tag_Start("TABLE",args) ]

        n=0
        rhtml=[]
        for cellmethods in self.Body_Matrix:
            rhtml=rhtml+[ self.HTML_Body_Row(n) ]         
            n+=1

        html=html+[ rhtml ]
        html=html+[ self.XML_Tag_End("TABLE") ]

        if (self.Cell_Mode):
            html=[ self.XML_Tag_Start("FONT",{"size": "+5", }) ]+html+[ self.XML_Tag_End("FONT") ]
        
        return html

    ##! 
    ##! Generates HTML BODY row no n.
    ##!
    
    def HTML_Body_Row(self,n):
        m=0
        args={
            #"height": self.Body_Matrix_TR_Heights[ n ],
            "class": self.Body_Matrix_TR_CSS[ n ],
        }
                
        html=[ self.XML_Tag_Start("TR",args) ]

        rhtml=[]
        for cellmethod in self.Body_Matrix[ n ]:
            rhtml=rhtml+[ self.HTML_Body_Row_Cell(n,m) ]

            m+=1
        html=html+[ rhtml ]
        html=html+[ self.XML_Tag_End("TR") ]

        return html
    
    ##! 
    ##! Generates HTML BODY row no n.
    ##!
    
    def HTML_Body_Row_Cell(self,n,m):
        cellmethod="HTML_"+self.Body_Matrix[ n ][ m ]
        cellcontent=cellmethod+": undef"
        if ( hasattr(self,cellmethod) ):
            method=getattr(self,cellmethod)
            cellcontent=method()

        args={
            "class": " ".join([
                self.Body_Matrix_TR_CSS[ n ]+" "+self.Body_Matrix_TD_CSS[ m ],
            ]),
        }
                
        html=[ self.XML_Tag_Start("TD",args) ]
        html=html+[ cellcontent ]
        html=html+[ self.XML_Tag_End("TD") ]

        return html

    ##! 
    ##! Generates TOP row left cell.
    ##!
    
    def HTML_Top_Left(self):
        html=[]
        args={
            "src": self.HTML_Top_Logos[0],
        }
        
        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html

    ##! 
    ##! Generates TOP row center cell.
    ##!
    
    def HTML_Top_Center(self):
        html=[]

        html=html+self.Hs(self.Titles)
        
        return html

    
    ##! 
    ##! Generates TOP row left cell.
    ##!
    
    def HTML_Top_Right(self):
        html=[]

        args={
            "src": self.HTML_Top_Logos[1],
        }

        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html


    
    ##! 
    ##! Generates Middle row left cell: Left navigation menu.
    ##!
    
    def HTML_Middle_Left(self):
        return self.HTML_Left_Menu()

    ##! 
    ##! Generates Middle row center cell.
    ##!
    
    def HTML_Middle_Center(self):
        return self.HTML_Central_Screen()

    ##! 
    ##! Generates Middle row right cell.
    ##!
    
    def HTML_Middle_Right(self):
        imgs=[]
        for logo in self.HTML_Middle_Right_Logos:
            url="/".join([ self.HTML_Icons,logo[ "Url" ] ])

            
            imgoptions={}
            imgoptions[ "src" ]=url
            imgoptions[ "title" ]=logo[ "Name" ]
            if (logo.has_key("Width")):
                imgoptions[ "width" ]=logo[ "Width" ]
            if (logo.has_key("Height")):
                imgoptions[ "height" ]=logo[ "Height" ]
            
            img=self.XML_Tag1("IMG",imgoptions)

            aoptions={}
            aoptions[ "target" ]="__blank"
            
            imgs.append( [ [ self.Center(self.A(logo[ "URL" ],img,aoptions)) ] ] )
                         
        html=[ self.HTML_Messages_Show() ]
        html=html+[ self.HTML_Table(imgs) ]

        return html
    
    ##! 
    ##! Generates Bottom row left cell.
    ##!
    
  
    def HTML_Bottom(self):         
        html=[]
        html=html+[ self.XML_Tag_Start("TR") ]   
        
        
        html=html+self.HTML_Cell("Bottom","Left")
        html=html+self.HTML_Cell("Bottom","Center")
        html=html+self.HTML_Cell("Bottom","Right")
        
        html=html+self.HTML_Indent(indent)
        html=html+self.XML_Tag_End("TR")+"\n" 

        return html


    
    ##! 
    ##! Generates Bottom row left cell.
    ##!
    

    def HTML_Bottom_Left(self):
        html=[]
        args={
            "src": self.HTML_Bottom_Logos[0],
            "align": "center",
            "height": "100px",
        }
        
        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html

    ##! 
    ##! Generates Bottom row center cell.
    ##!
    
    def HTML_Bottom_Center(self):        
        html=[]
        args={
            "src": self.HTML_Bottom_Logos[1],
            "align": "center",
            #"height": "824px",
            "width": "200px",
        }
        
        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html

    ##! 
    ##! Generates Bottom row right cell.
    ##!
    
    def HTML_Bottom_Right(self):
        html=[]
        args={
            "src": self.HTML_Bottom_Logos[2],
            "align": "center",
            "height": "100px",
        }
        
        html=html+[ self.XML_Tag_Start("IMG",args) ]

        return html

    
    

    ##! 
    ##! Generates Left menu.
    ##!
    
    def HTML_Left_Menu(self):        
        html=[]
        html=html+[ self.H(3,self.Title+":") ]

        return html


    ##! 
    ##! Generates central screen.
    ##!
    
    def HTML_Central_Screen(self):
        html=[]
        html=html+[ self.H(3,self.Title+":") ]

        return html
