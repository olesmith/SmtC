import re
from Base import *


from SVG    import XML_SVG

class XML(Base,XML_SVG):
    __Indent__="  "
    
    ##! 
    ##! Transforms list of (text) lists, into flat list, with indention
    ##!
    
    def XML_Print(self,xmls,level=0):
        indent=self.__Indent__*level

        output=""
        for xml in xmls:
            if (xml.__class__.__name__=="list"):
                output=output+self.XML_Print(xml,level+1)
            else:
                output=output+indent+xml+"\n"
                
        return output
    
    ##! 
    ##! Create option=value part. Take heed of list and dicts.
    ##!
    
    def XML_Option(self,option,value):
        if (value.__class__.__name__=="dict"):
            text=[]
            for key in value:
                val=value[ key ]
                if (val.__class__.__name__):
                    val=str(val)
                    text.append(key+": "+val+";")

            value=" ".join(text)
            
        elif (value.__class__.__name__=="list"):
            text=[]
            for key in value:
                text.append(str(key))
                
            value=" ".join(text)
        elif (value==None):
            return option
            
        value=str(value)
        value=re.sub(r'"',"",value)
           
        return option+"=\""+value+"\""

    ##! 
    ##! Create tag option part.
    ##!
    
    def XML_Options(self,options):
        text=[""]
        keys=options.keys()
        keys=sorted(keys)
        
        for option in keys:
            text.append( self.XML_Option(option,options[ option ]) )

        svg=""
        if ( len(text)>1 ):
            svg=" ".join(text)

        return svg
    
    ##! 
    ##! Consider possibility ogf tag being a list, in this case
    ##! produce several tags.
    ##!
    
    def XML_Tag_Make(self,tag,last=False):
        if (not tag.__class__.__name__=="list"):
            tag=[tag]

        glue="><"
        if (last):
            glue="></"
            tag.reverse()
            
        return glue.join(tag)
    
    ##! 
    ##! Create <tag+options>
    ##!
    
    def XML_Tag(self,tag,options={}):
        return "<"+self.XML_Tag_Make(tag)+self.XML_Options(options)+">"

    ##! 
    ##! Create start tag.
    ##!
    
    def XML_Tag_Start(self,tag,options={},indent=0):
        return self.XML_Tag(tag,options)

    ##! 
    ##! Create stand alone tag, ending with />
    ##!
    
    def XML_Tag1(self,tag,options={}):
        return "<"+self.XML_Tag_Make(tag)+self.XML_Options(options)+"/>"

    ##! 
    ##! Create end tag.
    ##!
    
    def XML_Tag_End(self,tag):
        return "</"+self.XML_Tag_Make(tag,True)+">"

    ##! 
    ##! Tag content, but omit new line (for codes)
    ##!
    
    def XML_Tags_No_New_Line(self,tag,content,options):
        if (not content): content.append("")
        
        content[0]=self.XML_Tag(tag,options)+content[0]
        content[   len(content)-1   ]=content[   len(content)-1   ]+ self.XML_Tag_End(tag)
        
        return content

    ##! 
    ##! Tag contents, start and end tag.
    ##!
    
    def XML_Tags(self,tag,content,options={},html=[]):
        if (content.__class__.__name__=="list"):
            html=html+[ self.XML_Tag_Start(tag,options) ]
            html=html+content
            html=html+[ self.XML_Tag_End(tag) ]
        else:
            html=html+[
                self.XML_Tag_Start(tag,options),
                str(content),
                self.XML_Tag_End(tag),
            ]

        return html

    ##! 
    ##! Simple tagging.
    ##!
    
    def XML_TagIt(self,tag,options={}):
        return "<"+tag+self.XML_Options(options)+">"
   
    ##! 
    ##! Insert comment section.
    ##!
    
    def XML_Comment(self,comment):
        return self.XML_Comments([ "",comment,"" ] )
   
    ##! 
    ##! Insert comments section.
    ##!
    
    def XML_Comments(self,comments):
        text="<!--\n"
        for comment in comments:
            text+="   ***! "+comment+"\n"
        text+="-->"

        return text
            
    ##! 
    ##! Tag with newlines after start tag and contents.
    ##!
    
    def XML_Tags_NL(self,tag,content,options={}):
        xml=self.XML_Tag(tag,options)+"\n"
        xml=xml+content+"\n"
        xml=xml+"</"+tag+">\n"

        return xml
    
    ##! 
    ##! Tag list with tag.
    ##!
    
    def XML_Tags_List(self,tag,contents,options={},indent=""):
        rcontents=[]
        for i in range( len(contents) ):
            rcontents.append( self.XML_Tags(tag,contents[i],options,indent) )
            
        return rcontents

