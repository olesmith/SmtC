
class Slides_SubMenu():
    def Slide_SubMenu_Entry(self,subdir,paths,cssclass):
        spaths=list(paths)
        spaths.append(subdir)
        
        url="/".join(spaths)

        cgipaths=self.Slides_CGI_Paths()                

        html=self.Slide_Name_Get(spaths)
        if (self.Slide_Link_Should(spaths)):
            html=self.A(
                "?Path="+url,
                html,
                {
                    "class": cssclass,
                    "title": self.Slide_Title_Get(spaths),
                }
            )
            
        return[  html ]
