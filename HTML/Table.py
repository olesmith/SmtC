

class HTML_Table():
    ##!
    ##! Generate table THEAD section: 
    ##!
    
    def HTML_Table_Head(self,titles,indent,troptions,thoptions={}):
        return self.HTML_Table_Row(
            titles,
            ["THEAD","TR"],
            "TH",
            troptions,
            thoptions
        )
    
    ##!
    ##! Generate one table row.
    ##!
    
    def HTML_Table_Row(self,row,trtag,tdtag,troptions,tdoptions):
        html=[]
        html=html+[ self.XML_Tag_Start(trtag,troptions) ]
        html=html+[ self.HTML_Table_Row_Cells(row,tdtag,tdoptions) ]
        html=html+[ self.XML_Tag_End(trtag) ]

        return html
    
    
    ##!
    ##! Generate TD (tdtag) cells for one row.
    ##!
    
    def HTML_Table_Row_Cells(self,row,tdtag,tdoptions):
        html=[]
        for cell in row:
            html.append( self.XML_Tags(tdtag,cell,tdoptions) )

        return html
        
   
    ##!
    ##! Generate HTML table. 
    ##!
    
    def HTML_Table(self,rows,titles=[],tails=[],options={},troptions={},tdoptions={},thoptions={},tailoptions={}):
        
        repeattitles=len(rows)+1
        if (options.has_key("repeat")):
            repeattitles=options[ "repeat" ]
            del options[ "repeat" ]

        html=[]
        html=html+[ self.XML_Tag_Start("TABLE",options) ]

        titlerow=[]
        if ( len(titles)>0 ):
            titlerow=[ self.HTML_Table_Row(titles,"TR","TH",troptions,thoptions) ]
        
        for i in range( len(rows) ):
            if ( len(titles)>0 and (i % repeattitles)==0 ):
                html.append(titlerow)
                
            html.append([ self.HTML_Table_Row(rows[i],"TR","TD",troptions,tdoptions) ])
            
        html=html+[ self.XML_Tag_End("TABLE") ]

        return html
    
    
