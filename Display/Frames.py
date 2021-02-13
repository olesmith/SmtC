from Base import *

class Display_Frames():

    
    def Display_Frames_As(self):
        query=self.CGI_Query_Path()
        comps=query.split('/')

        svg=comps[ len(comps)-1 ]
        if (re.search('\.svg$', svg)):
            comps.pop()

        query="/".join(comps)
        
        indent=3
        n=1
        urls=[]
        csfile=""
        for svgfile in self.Path_Files(query,'svg'):
            
            comps=svgfile.split('/')
            sfile=comps.pop()
            spath="/".join(comps)
            
            url="?".join( [ self.CGI_Root+"/"+"Frame",query+'/'+sfile+"#IMG"] )
            options={
                "target": "frames",
                "href": url,
                "class": "FrameLinks",
            }
            urls.append( self.HTML_Indent(indent+1)+self.XML_Tags("A", ("%03d"%n), options )+"\n" )
            n+=1
            csfile=sfile

        urls=List_Slice(urls,20)

        sep="\n"+self.HTML_Indent(indent)+"|"

        html=""
        for rurls in urls:
            if ( len(rurls)>0 ):
                html=html+self.HTML_Indent(indent)+"[ "
                html=html+sep.join(rurls)+" ]"
            
                html=html+"\n"+self.BR()+"\n"

        return html
    
   
    def Display_Frames_HTML(self):
        query=self.CGI_Query_Path()
        comps=query.split('/')

        svg=comps[ len(comps)-1 ]

        query="/".join(comps)

        html=""
        html=html+self.Display_Frames_As()

        return html
    
        cfile=self.CGI_Query_File()
        if (not cfile):
            cfile=csfile
        
        url="?".join( [ self.CGI_Root+"/"+"SVG",query+'/'+cfile] )

        imgargs={
            #"class": "Center",
            "src": url,
        }
        
        html=html+self.Center(self.XML_Tag_Start("IMG",imgargs))+"\n"

        return html

    def Display_Frame(self):
        print self.Display_HTTP_Headers()

        query=self.CGI_Query_Path()
        comps=query.split('/')

        svg=comps.pop()

        query="/".join(comps)
        
        indent=3
        
        urls=[]
        n=1
        for svgfile in self.Path_Files(query,'svg'):
            options={
                "href": self.CGI_Root+"/"+"Frame?"+svgfile
            }
            urls.append( self.HTML_Indent(indent+1)+self.XML_Tags("A", ("%03d"%n), options ) )
            n+=1

        urls=List_Slice(urls,20)

        sep="\n"+self.HTML_Indent(indent)+"|"

        html=self.Display_Header()
        html=html+self.Display_Central_Info()
        html=html+self.HTML_Indent(indent)
        html=html+self.XML_Tag_Start("BODY")+"\n"
        #html=html+self.XML_Tag_Start("DIV",{ "class": "w3-content w3-section" })+"\n"

        
        anchorargs={
            "id": "IMG",
        }

        html=html+self.XML_Tags("A","",anchorargs)
        html=html+self.Display_Frames_As()

        url="?".join( [ self.CGI_Root+"/"+"SVG",query+"/"+svg] )
        imgargs={
            #"class": "Center",
            "src": url,
        }

        html=html+self.XML_Tag_Start("IMG",imgargs)
        
        html=self.Center(html)

        #html=html+self.XML_Tag_End("DIV")+"\n"
        html=html+self.HTML_Indent(indent)
        html=html+self.XML_Tag_End("BODY")+"\n"
        
        html=html+self.Display_Tailer()
        print html

        
