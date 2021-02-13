

class HTML_Icon():
    HTML_Icon_Color_Default_Display='inline'
    HTML_Icon_Color_Default_Show='blue'
    HTML_Icon_Color_Default_Hide='grey'
    HTML_Icon_Size_Default=0
    
    HTML_Icon_Sizes=[
        '',
        'fa-lg',
        'fa-2x',
        'fa-xs','fa-sm',
        'fa-3x','fa-5x','fa-7x','fa-10x',            
    ]
            
    ##! 
    ##! 
    ##!
    
    def HTML_Icon(self,icon,color=None,size=None,options=None,style=None):
        if (options==None): options={}
        if (style==None):   style={}
            
        if (options.has_key("style")):
            style.update(options[ "style" ])
        
        return self.XML_Tags(
            "I","",
            self.HTML_Icon_Options(icon,color,size,options,style)         
        )

    
    ##! 
    ##!
    ##!
    
    def HTML_Icon_Options(self,icon,color,size,options,style):
        if (not options.has_key("class")):
            options[ "class" ]=[]
        
        options[ "class" ]=options[ "class" ]+self.HTML_Icon_Classes(icon,color,size,options,style)
        options[ "style" ]=self.HTML_Icon_Style(icon,color,size,options,style)
        
        return options
    ##! 
    ##! 
    ##!
    
    def HTML_Icon_Classes(self,icon,color,size,options,style):
        return [
            icon,
            self.HTML_Icon_Size(icon,color,size,options,style),
            "nowrap"
        ]
    ##! 
    ##! 
    ##!
    
    def HTML_Icon_Size(self,icon,color,size,options,style):
        if (size==None):
            size=self.HTML_Icon_Size_Default

        if (isinstance(size, int)):
            size=self.HTML_Icon_Sizes[ size ]

        return size
    
    ##! 
    ##! 
    ##!
    
    def HTML_Icon_Style(self,icon,color,size,options,style):
        style[ "color" ]=self.HTML_Icon_Color(icon,color,size,options,style)
        style[ "background-color" ]="white"
        
        return style
    
    ##! 
    ##! 
    ##!
    
    def HTML_Icon_Color(self,icon,color,size,options,style):
        if (color==None):
            color=self.HTML_Icon_Color_Default_Show
            if (style.has_key("color")):
               color=style[ "color" ]

        return color
        
