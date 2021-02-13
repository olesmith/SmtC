

class HTML_Icons():
    ##! 
    ##! 
    ##!
    
    def HTML_Icons_Toggle(self,clss,icon,hidden=False,display=None,colors=None,size=None,options=None,style=None):
        if (colors==None):  colors=["blue","grey" ]
        if (options==None): options={}
        if (style==None):   style={}
        
        show_options=dict(options)
        hide_options=dict(options)

        show_options[ "class" ]=[self.HTML_Icons_Classes_Show(clss)]    
        hide_options[ "class" ]=[self.HTML_Icons_Classes_Hide(clss)]
        if (hide_options.has_key("title")):
            hide_options[ "title" ]="Hide "+hide_options[ "title" ]
        
        show_options[ "onclick" ]=self.HTML_Icons_OnClick_Hide(
            clss,display
        )
        
        hide_options[ "onclick" ]=self.HTML_Icons_OnClick_Show(
            clss,display
        )

        show_style=dict(style)
        hide_style=dict(style)
        hide_style[ "display" ]="none"
        
        show_color=colors[0]
        hide_color=colors[1]


        if (hidden):
            hide_style[ "display" ]="none"
        else:
            hide_style[ "display" ]=self.HTML_Icons_Display(display)
            show_style[ "display" ]="none"
        
        return [
            self.HTML_Icon(
                icon,
                show_color,
                size,
                show_options,
                show_style
            ),
            self.HTML_Icon(
                icon,
                hide_color,
                size,
                hide_options,
                hide_style
            ),
        ]
        
    ##! 
    ##! 
    ##!
    
    def HTML_Icons_Classes_Hide(self,clss):
        return clss+" Hide"
        
    ##! 
    ##! 
    ##!
    
    def HTML_Icons_Classes_Show(self,clss):
        return clss+" Show"
        
    ##! 
    ##! 
    ##!
    
    def HTML_Icons_OnClick_Hide(self,clss,display):        
        return self.HTML_JS_Show(
            self.HTML_Icons_Classes_Hide(clss),
            self.HTML_Icons_Display(display)
        )+self.HTML_JS_Hide(
            self.HTML_Icons_Classes_Show(clss)
        )
        
    ##! 
    ##! 
    ##!
    
    def HTML_Icons_OnClick_Show(self,clss,display):
        return self.HTML_JS_Hide(
            self.HTML_Icons_Classes_Hide(clss)
        )+self.HTML_JS_Show(
            self.HTML_Icons_Classes_Show(clss),
            self.HTML_Icons_Display(display)
        )
        
        
    ##! 
    ##! 
    ##!
    
    def HTML_Icons_Display(self,display):
        if (display==None):
            display=self.HTML_Icon_Color_Default_Display

        return display
        
