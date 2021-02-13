import re,random


class Slides_Slide_Cell_Phrase():
    
    ##!
    ##! Insert phrase from file.
    ##!
    
    def Slide_Cell_Phrase(self,paths):
        phrasefile=self.Slide_Cell_Phrase_File()
        
        html=[]
        if (self.File_Exists(phrasefile)):
            text=self.File_Read_Lines(phrasefile)

            rtext=[]
            for i in range( len(text) ):
                if (re.search(r'\S',text[   i   ])):
                    rtext.append(text[i])

            for i in range( len(rtext) ):
                if (i<len(rtext)-1):
                    if (not re.search(r'<br',rtext[i],re.IGNORECASE)):
                        rtext[i]=rtext[i]+self.BR()
                else:
                    if (not re.search(r'<i\s*',rtext[ i ],re.IGNORECASE)):
                        rtext[ i ]=self.XML_Tags(
                            "DIV",
                            rtext[ i ],
                            {
                                "class": "Author",
                            }
                        )

                
            html=html+[ self.XML_Tags("DIV",rtext,{ "class": 'Phrase', }) ]

        return html

    
    ##!
    ##! Reads phrase files: list of numbered files in Phrase dir.
    ##!
    
    def Slide_Cell_Phrase_File(self):
        phrasefiles=self.Slide_Cell_Phrase_Files()

        return random.choice(phrasefiles)
        
        
    ##!
    ##! Reads phrase files: list of numbered files in Phrase dir.
    ##!
    
    def Slide_Cell_Phrase_Files(self):
        #Subdirs in root path
        path=self.Slide_Cell_Phrase_Path()

        files=[]
        if (path!=None):        
            files=self.Path_Files(
                path,
                '^\d+\S*\.html$'
            )

        return files
        
    
    ##!
    ##! Detect directory to read phrases from:
    ##! First found dir in Slides root, with 'Phrase' in it's name.
    ##!
    
    def Slide_Cell_Phrase_Path(self):
        #Subdirs in root path
        subdirs=self.Path_Subdirs(self.DocRoot)

        for subdir in subdirs:
            if (re.search('Phrases',subdir)):
                return subdir
                
        return None
