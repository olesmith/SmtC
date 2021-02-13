

class HTML_Form():
    ##! 
    ##! 
    ##!
    
    def HTML_Form(self,edit,id,url,contents,options=None):
        if (edit==0): return contents

        #Make a copy of options
        roptions={}
        if (options!=None): roptions=dict(options)

        return self.XML_Tags(
            "FORM",
            contents,
            self.HTML_Form_Options(edit,id,url,roptions)
        )

    ##! 
    ##! 
    ##!
    
    def HTML_Form_Options(self,edit,id,url,options):
        options.update(
            {
                "action": url,
                "id": id,
                "method": "post",
            }
        )
        
        return options
