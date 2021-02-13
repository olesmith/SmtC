import re


class Slide_Cell_Code_CGI():
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_CGI_Key(self):
        return self._Doc_Class_CGI_
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_CGI_Value(self):
        docstyle=self._Doc_Class_Default_
        cgivalue=self.CGI_POST_Text(
            self.Slide_Cell_Code_CGI_Key()
        )

        if (cgivalue!=""):
            docstyle=cgivalue

        return docstyle
    
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_CGI_Options_Key(self):
        return self._Doc_Class_Options_CGI_
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_CGI_Options_Value(self):
        docoptions=self._Doc_Class_Options_Default_
        cgivalue=self.CGI_POST_Text(
            self.Slide_Cell_Code_CGI_Options_Key()
        )

        if (cgivalue!=""):
            docoptions=cgivalue
            
        return docoptions

    
    
    
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_Pre_Amble_Key(self):
        return self._Doc_Ambles_Pre_CGI_
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_CGI_Pre_Amble_Values(self):
        preamble=self._Doc_Ambles_Pre_Default_
        cgi_key=self.Slide_Cell_Code_Pre_Amble_Key()
        
        cgi_value=self.CGI_POST_List(cgi_key)

        value="".join(cgi_value)
        if (re.search('\S',value)):
            preamble=cgi_value
            
        return preamble

    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_CGI_Post_Amble_Values(self):
        return self._Doc_Ambles_Post_Default_
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_CGI_Body_Key(self):
        return self._Doc_Body_CGI_
    
    ##!
    ##! 
    ##!
    
    def Slide_Cell_Code_CGI_Body_Values(self):
        body=self._Doc_Body_Default_
        cgi_key=self.Slide_Cell_Code_CGI_Body_Key()
        
        cgi_value=self.CGI_POST_List(cgi_key)

        value="".join(cgi_value)
        
        if (re.search('\S',value)):
            body=cgi_value
            
        return body

    
    
