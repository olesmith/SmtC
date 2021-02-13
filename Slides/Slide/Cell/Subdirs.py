import re

class Slides_Slide_Cell_Subdirs():
    
    ##!
    ##! Get Title of a subdir.
    ##
    
    def Slide_Cell_Subdir_Title(self,paths,subdir):
        spaths=list(paths)
        spaths.append(subdir)

        url="/".join(spaths)

        return self.A(
            "?Path="+url,
            self.Slide_Name_Get(spaths),
            {
                "title": self.Slide_Title_Get(spaths),
            }
        )
    
    ##!
    ##! Insert list of subdirs, who has a title file, Title.html..
    ##
    
    def Slide_Cell_SubdirList(self,content,paths):
        path="/".join([self.DocRoot]+paths)
        subdirs=self.Path_Subdirs(path,"Title.html")
        spec=re.sub('\s*@SubdirsList\s*',"",content, flags=re.IGNORECASE)
        print spec
        
        html=[]
        n=1
        for subdir in subdirs:
            if (spec!=""):
                if (not re.search(spec,subdir)):
                    continue;
            titlefile="/".join([subdir,"Title.html"] )
            namefile="/".join([subdir,"Name.html"] )
            contentsfile="/".join([subdir,"Contents.html"] )

            if (not self.File_Exists(namefile)): namefile=titlefile
            
            name=re.sub('^\s+',"",self.File_Read(namefile))
            name=re.sub('\s+$',"",name)
            title=re.sub('^\s+',"",self.File_Read(titlefile))
            title=re.sub('\s+$',"",title)
            
            subdircomps=subdir.split("/")
            subdirname=self.File_BaseName(subdir)

            final=";"
            if (n==len(subdirs)): final="."

            cell=name
            cell=cell+final
            if (self.File_Exists(contentsfile)):
                cell=self.A(
                    "?Path="+"/".join(paths+[subdirname]),
                    title+final,
                    {
                        #"title": self.File_Read(titlefile),
                    },
                    title
                )

            html.append(cell)
            n+=1
            
        return self.HTML_List(
            html,
            "UL",
            {
                "style": 'list-style-type:square',
            }
        )
    
    ##!
    ##! Get list of all subdirs titles.
    ##
    
    def Slide_Cell_Subdir_Titles(self,paths):
        rpaths=[ self.DocRoot ]+paths
        subdirs=self.Path_Dirs( "/".join(rpaths) )

        if (not subdirs):
            return []
        
        slist=[]
        for subdir in subdirs:
            slist.append( self.Slide_Cell_Subdir_Title(paths,subdir) )

        rhtml=[ self.Div("Subtopics:",{"class": "Slide_Subtopic_Title",}) ]
        
        return rhtml+self.HTML_List(slist,"OL",{"class": "Slide_Subtopic",},{"class": "Slide_Subtopic",})

