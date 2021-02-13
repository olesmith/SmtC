

class HTML_Input():
    ##! 
    ##! 
    ##!
    
    def HTML_Input(self,id,name,value=None,input_type=None,options=None,style=None):

        roptions=self.HTML_Input_Options(id,name,value,input_type,options,style)
        
        if (input_type=="area"):
            return self.HTML_Input_Area(
                id,name,value,roptions,style
            )

        return self.XML_Tag1(
            "INPUT",
            roptions
        )

    ##! 
    ##! 
    ##!
    
    def HTML_Input_Options(self,id,name,value,input_type,options,style):
        if (value==None):      value=""
        if (input_type==None): input_type="text"

        if (options==None):    options={}
        if (style!=None):      options[ "style" ]=style
            
        options[ "name" ]=name
        if (input_type!="area"):
            options[ "value" ]=value
        options[ "type" ]=input_type
        

        return options
    
    ##! 
    ##! 
    ##!
    
    def HTML_Input_Area(self,id,name,value,options,style=None):
        if (style!=None): options[ "style" ]=style

        return [
            self.XML_TagIt(
                "TEXTAREA",
                options
            )+
            "\n".join(value)+
            self.XML_TagIt("/TEXTAREA")
        ]

