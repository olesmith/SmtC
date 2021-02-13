import re,glob

class Slides_Slide_Cell_List():
    ##!
    ##! Insert list of subdirs, who has a title file, Title.html..
    ##
    
    def Slide_Cell_List_Insert(self,content,paths):
        path="/".join([self.DocRoot]+paths)

        comps=content.split(' ')

        if (len(comps)>1):
            spec=comps[1]
            
        
        if (not re.search('/^(/|\.\.)/',spec)):
            spec=path+"/"+spec
            
        list_type="OL"
        if (   re.search('\s*@Items\s*',content, re.IGNORECASE)   ):
            list_type="UL"
            
        fnames=glob.glob(spec)
        fnames.sort()
        
        options=self.Slide_Cell_List_LI_Options(comps,paths)
        style="g"
        if (len(comps)>2):
            style=comps[2]


            
        lst=[]
        n=0
        for fname in fnames:
            n+=1
            
            items=[]
            if (style=="bib"):
                items.append('['+str(n)+']:')
                
            if (re.search('\.html$',fname)):
                items=items+[
                    self.Slide_Cell_Contents_Parse(
                        paths,
                        self.File_Read_Lines(fname)
                    )
                ]
            elif (re.search('\.py$',fname)):
                items=items+[
                    self.B(self.File_BaseName(fname)+":"),
                    self.Slide_Cell_Code_Insert(
                        "@Code "+fname,
                        paths,
                        options
                    )
                ]

                
            lst=lst+[items]


        return self.HTML_List(lst,list_type,{},options)

    ##!
    ##! 
    ##
    
    def Slide_Cell_List_LI_List_Type_Style(self,comps,paths):
        style="g"
        if (len(comps)>2):
            style=comps[2]

        #style=style[0]
        styles={
            "bib": "none",
            "d": "decimal",
            "1": "decimal",
            "0": "decimal-leading-zero",
            "a": "lower-alpha",
            "A": "upper-alpha",
            "i": "lower-roman",
            "i": "lower-roman",
            "g": "lower-greek",
            "G": "upper-greek",
        }

        if (styles.has_key(style)):
            style=styles[ style ]

        return style
    
    ##!
    ##! 
    ##
    
    def Slide_Cell_List_LI_Options(self,comps,paths):
        return {
            "STYLE": {
                #"display": "list-item;",
                "vertical-align": "bottom",
                "list-style-type": self.Slide_Cell_List_LI_List_Type_Style(
                    comps,paths
                ),
                "margin-bottom": '10px',
            }
        }
    ##!
    ##! 
    ##
    
    def Slide_Cell_List_LI(self,content,paths):
        item=fname
        if (re.search('\.html$',fname)):
            item=self.Slide_Cell_Contents_Parse(
                paths,
                self.File_Read_Lines(fname)
            )
        elif (re.search('\.py$',fname)):
                lst.append([
                    self.B(self.File_BaseName(fname)+":"),
                    self.Slide_Cell_Code_Insert(
                        "@Code "+fname,
                        paths,
                        options
                    )
                ])
