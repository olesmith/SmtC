
class Slides_Menu():

    def Slides_Menu_Active(self,paths,subdir):
        cgipaths=self.Slides_CGI_Paths()
        rpaths=list(paths)
        rpaths.append(subdir)
        
        res=False
        if ( len(cgipaths)>len(paths) ):
            res=True
            for i in range( len(rpaths) ):
                if ( rpaths[i]!=cgipaths[i]):
                    res=False

        return res

    
    def Slides_Menu_Path(self,paths):
        return "/".join([self.DocRoot]+paths)

    def Slides_Menu_Pre(self,paths):
        paths=self.Slides_CGI_Paths()
        paths.pop()

        html=[]
        
        rpaths=[]
        for path in paths:
            html=html+[
                self.Slide_Menu_Entry_Title_A(rpaths),
            ]
            rpaths.append(path)
        
        return self.HTML_List(html)+[self.BR()]
    
        
    def Slides_Menu(self,paths):

        url="/".join(paths)
        
        cssclass="leftmenu"
        htmllist=[]

        path="/".join([self.DocRoot]+paths)
                                       
        subdirs=self.Path_Dirs(
            self.Slides_Menu_Path(paths),
            "Name.html"
        )
        
        for subdir in subdirs:
            htmlitem=[]
            if (self.Slides_Menu_Active(paths,subdir)):
                rpaths=list(paths)
                rpaths.append(subdir)
                htmlitem=self.Slides_Menu(rpaths)
            else:
                htmlitem=self.Slide_SubMenu_Entry(subdir,paths,cssclass)

            htmllist.append(htmlitem)


        html=[]
        html=html+[ self.Slide_Menu_Entry(paths,cssclass) ]
        html=html+[
            self.HTML_List(
                htmllist,
                "UL",
                {
                    "style": 'list-style-type:square',
                }
            )
        ]

        return html
 
    def Slide_Menu_Entry(self,paths,cssclass):

        cpath=self.CGI_POST("Path")
        path="/".join(paths)

        name=self.Slide_Name_Get(paths)        
        if (path==cpath):
            return self.B(
                name+"*",
                {
                    "title": self.Slide_Title_Get(paths),
                }
            )
        
        return [
            #Moved to Slide_Menu_Pre
            self.Slide_Menu_Entry_Title_A(paths,name,cssclass)
        ]


    def Slide_Menu_Entry_Title_A(self,paths,name=None,cssclass=None):
        if (name==None): name=self.Slide_Name_Get(paths)
        if (cssclass==None): cssclass="leftmenu"
        
        return self.A(
            "?Path="+"/".join(paths),
            name,
            {
                "class": cssclass,
                "title": self.Slide_Title_Get(paths),
            }
        )
