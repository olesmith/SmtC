

class HTML_Button():
    ##! 
    ##! 
    ##!
    
    def HTML_Button(self,id,name,title,value,button_type,options=None):
        return self.XML_Tags(
            "Button",
            title,
            self.HTML_Button_Options(id,name,value,button_type,options)
        )

    ##! 
    ##! 
    ##!
    
    def HTML_Button_Options(self,id,name,value,button_type,options):
        if (options==None):    options={}

        options[ "name" ]=name
        options[ "value" ]=value
        options[ "type" ]=button_type
        
        return options
