class HTML_Tags():
    Default_Anchor=""
    
    def A(self,url,content,options={},title="",anchor=None):
        if (anchor==None): anchor=self.Default_Anchor
        
        options[ "href" ]=url+"#"+anchor
        if (title):
            options[ "title" ]=title
            
        return self.XML_Tag("A",options)+content+self.XML_Tag_End("A")

    
    def HTML_A(self,url,content,options={},title="",anchor=None):
        if (anchor==None): anchor=self.Default_Anchor
        
        options[ "href" ]=url+"#"+anchor
        if (title):
            options[ "title" ]=title
            
        return self.XML_Tags("A",content,options)
    
    def Anchor(self,anchor,options={}):
        options[ "name" ]=anchor
        return self.XML_Tag("A",options)+self.XML_Tag_End("A")
    

    def B(self,content,options={}):
        roptions=self.HTML_AddClass("B",options)
        
        return self.XML_Tags("SPAN",content,roptions)
    
    def I(self,content,options={}):
        roptions=self.HTML_AddClass("I",options)
        
        return self.XML_Tags("SPAN",content,roptions)
    
    def U(self,content,options={}):
        roptions=self.HTML_AddClass("U",options)
        
        return self.XML_Tags("SPAN",content,roptions)
    
    def Center(self,content,options={}):
        roptions=self.HTML_AddClass("Center",options)
        
        return self.XML_Tags("DIV",content,roptions)
    
    def IMG(self,img,alttext="",options={}):
        options[ "src" ]=img
        
        return self.XML_Tag_Start("IMG",options)
    
    def Icon(self,icon,size=None,options={}):
        if (size==None):
            size="fa-3x"
            
        if (size!=None):
            icon=icon+" "+size
            
        roptions=self.HTML_AddClass(icon,options)
        
        return self.XML_Tag("I",roptions)+self.XML_Tag_End("I")
    
    ##! 
    ##! Create title tag <Hn>
    ##!
    
    def H(self,n,title,options={}):
        roptions=self.HTML_AddClass("H"+str(n),options)
        
        return self.XML_Tags("DIV",title,roptions)
    
    ##! 
    ##! Create list of title tags: H1,H2,...
    ##!
    
    def Hs(self,titles,options={}):
        for n in range( len(titles) ):
            titles[n]=self.H(n+1,titles[n],options)
            
        return titles

    def BR(self,options={}):
        return self.XML_Tag_Start("BR",options)
    
    def HR(self,options={}):
        return self.XML_Tag_Start("HR",options)
    
    def Span(self,content,options={},style=None):
        if (style!=None): options[ "style" ]=style
        
        return self.XML_Tags("SPAN",content,options)
    
    def Div(self,content,options={},style=None):
        if (style!=None): options[ "style" ]=style

        return self.XML_Tags("DIV",content,options)
    
    def IFrame(self,url,options={}):
        options[ "src" ]=url
        return self.XML_Tags("IFRAME","",options)
    
    def HTML_List_Old(self,items,options={},lioptions={}):
        items=self.XML_Tags_List("LI",items,lioptions)

        return self.XML_Tags(
            "UL",
            "\n".join(items)+"\n",
            options
        )
    
    def HTML_List(self,items,ul="UL",options={},lioptions={}):
        html=[]
        html=html+[ self.XML_Tag_Start(ul,options) ]

        rhtml=[]
        for item in items:
            rhtml=rhtml+[ self.XML_Tags("LI",item,lioptions) ]

        html=html+[ rhtml ]
        html=html+[ self.XML_Tag_End(ul) ]
        
        return html
    
    def HTML_Frame(self,content,options=None,style=None):
        if (options==None):
            options={
                "class": "Table_Frame Code",
            }

        if (style!=None):
            options[ "style" ]=style
            
        return self.XML_Tags(
            "CENTER",
            self.XML_Tags(
                "TABLE",
                self.XML_Tags(
                    "TR",
                    self.XML_Tags(
                        "TD",
                        content,
                        options
                    )
                )
            )
        )
    

