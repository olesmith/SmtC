import re

class HTML_Parse():

    ##! 
    ##! Parses HTML code doing convenient substitutes.
    ##!
    
    def HTML_Parse(self,html):
        if ( re.search('<LATEX>',html) ):
            html=re.sub(r'<LATEX>',"<BR><CENTER>[;",html)
        if ( re.search('</LATEX>',html) ):
            html=re.sub(r'</LATEX>',";]</CENTER>",html)

        regex=re.compile(r'\\input{[^}]*}')
        found=regex.findall(html)
        for i in range( len(found) ):
            latex=re.sub(r'\\input{',"",found[i])
            latex=re.sub(r'}\n?',"",latex)
            
            if (not self.File_Exists(latex)):
                latex=latex+".tex"
            
            if (self.File_Exists(latex)):
                latex=self.File_Read(latex)
            else:
                latex=latex+": not found"

            #Fix!!
            latex=re.sub(r'\\Matrix',"\\underline",latex)
            latex=re.sub(r'\\Vector',"\\underline",latex)
            latex=re.sub(r'\\',"___",latex)
            html=re.sub('\\'+found[i]+'\n?',latex,html)
            html=re.sub('___',r'\\',html)

        return html
            
       
       
