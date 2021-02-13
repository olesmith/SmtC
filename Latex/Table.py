import re


class Latex_Table():
    ##!
    ##!
    ##!
   
    def Latex_Table_Width(self,table):
        width=1
        for row in table:
            if ( row.__class__.__name__=='list'):
                if (width<len(row) ):
                    width=len(row)

        return width
    
    ##!
    ##!
    ##!
   
    def Latex_Table_Args2Arg(self,args,argname):
        value=self.__Latex__[ "Table" ][ "Defaults" ][ argname ]
        if (args.has_key(argname)):
            value=str(args[ argname ])

        return value


    ##!
    ##!
    ##!
   
    def Latex_Table_Spec(self,width,args):
        specs=self.Latex_Table_Args2Arg(args,"Specs")
        if (specs!=None):
            return specs
        
        spec=self.Latex_Table_Args2Arg(args,"Spec")
        specsep=self.Latex_Table_Args2Arg(args,"SpecSep")

        spec=specsep+spec
        spec=spec*width+specsep

        return spec
    
    ##!
    ##!
    ##!
   
    def Latex_Table_Begin(self,width,args):    
        return "\\begin{tabular}{"+self.Latex_Table_Spec(width,args)+"}"
        
    ##!
    ##!
    ##!
   
    def Latex_Table_End(self):
        return "\\end{tabular}"
        
    ##!
    ##!
    ##!
   
    def Latex_Table_Row(self,width,row,args={}):
        pre=self.Latex_Table_Args2Arg(args,"Pre")
        
        if ( row.__class__.__name__=='str' ):
            return pre+row

        spec=self.Latex_Table_Args2Arg(args,"Spec")
        specsep=self.Latex_Table_Args2Arg(args,"SpecSep")
        colsep=self.Latex_Table_Args2Arg(args,"ColSep")
        rowsep=self.Latex_Table_Args2Arg(args,"RowSep")

        specspecsep=specsep+spec+specsep

        if ( len(row)<width ):
            rpre=pre+row[0]
            mwidth=width-len(row)+1
            return pre+"\\multicolumn{"+str(mwidth)+"}{"+specspecsep+"}{"+rpre+"}\\\\"
        
        colsep=colsep+"\n"+pre
        return pre+colsep.join(row)+rowsep
        
     
    ##!
    ##!
    ##!
   
    def Latex_Table(self,table,args={}):
        width=self.Latex_Table_Width(table)

        latex=[]
        latex.append( self.Latex_Table_Begin(width,args) )

        for row in table:
            latex.append( self.Latex_Table_Row(width,row,args) )
        
        latex.append( self.Latex_Table_End() )

        return latex
