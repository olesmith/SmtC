

class HTML_Table_Old():
    ##!
    ##! Generate table THEAD section: 
    ##!
    
    def HTML_Table_Old_Head(self,titles,indent,troptions,thoptions={}):
        row=self.HTML_Table_Old_Row(
            titles,
            ["THEAD","TR"],
            "TH",
            indent,
            troptions,
            thoptions
        )
        
        return row
    
    ##!
    ##! Generate one table row.
    ##!
    
    def HTML_Table_Old_Row(self,row,trtag,tdtag,indent,troptions,tdoptions):
        sep=self.HTML_Indent(indent)
        rsep="\n"+sep
        
        return self.XML_Tags(
            trtag,
            self.HTML_Table_Old_Row_Cells(
                row,
                tdtag,
                indent+1,
                tdoptions
            )+rsep,
            troptions,
            self.HTML_Indent(indent)
        )

    
    ##!
    ##! Generate TD (tdtag) cells for one row.
    ##!
    
    def HTML_Table_Old_Row_Cells(self,row,tdtag,indent,options):
        sep=self.HTML_Indent(indent)
        rsep="\n"+sep
        
        row=self.XML_Tags_List(tdtag,row,options)
        
        return rsep+rsep.join(row)
        
   
    ##!
    ##! Generate HTML table. 
    ##!
    
    def HTML_Table_Old(self,rows,titles=[],tails=[],options={},troptions={},tdoptions={},thoptions={},tailoptions={}):

        repeattitles=len(rows)+1
        if (options.has_key("repeat")):
            repeattitles=options[ "repeat" ]
            del options[ "repeat" ]

        indent=1
        sep=self.HTML_Indent(indent)
        rsep="\n"+self.HTML_Indent(indent+1)
        rrsep="\n"+self.HTML_Indent(indent+2)
        
        titlerow=self.HTML_Table_Old_Row(titles,"TR","TH",indent+3,troptions,thoptions)
        
        rrows=[]
        for i in range( len(rows) ):
            row=self.HTML_Table_Old_Row_Cells(rows[i],"TD",indent+3,tdoptions)
            
            if (i>0 and (i % repeattitles)==0):
                rrows.append(titlerow)
                
            rrows.append(row+rrsep)
 
        rrows=self.XML_Tags_List("TR",rrows,troptions)

        options[ "align" ]="center"

        
        return sep+self.XML_Tags(
            "TABLE",
            "\n"+self.HTML_Table_Old_Head(titles,indent+1,thoptions)+
            rsep+self.XML_Tag_Start("TBODY")+
            rrsep+rrsep.join(rrows)+
            rsep+self.XML_Tag_End("TBODY")+
            "\n"+sep,
            options
        )
    
    
