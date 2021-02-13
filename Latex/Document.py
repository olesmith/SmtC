import re,sys

class Latex_Document():

    __Regexp_Document_Class__ = 'documentclass'
    __Regexp_Document_Begin__ = 'begin{document}'
    __Regexp_Document_End__   = 'end{document}'
    
    __Latex_PreAmple__        = 'PreAmble.tex'
    __Latex_PreAmple_TikZ__   = 'PreAmble.tikz.tex'
    __Latex_Document_Class__  = None
    
    ##!
    ##! Generate latex document, inserting, if necessary:
    ##!
    ##! 1: documentclass: report, if tex, standalone if tikz.
    ##!
    ##! 2: Preamble+\begin{document}
    ##!
    ##! 3: \end{document}
    ##!
   
    def Latex_Document(self,tex_file,tikz=None):
        self.__Latex_PreAmple__=self.__Latex_PreAmple__
        tikz=self.Latex_TikZ_Should(tex_file,tikz)
        
        if (tikz):
            self.__Latex_PreAmple__=self.__Latex_PreAmple_TikZ__
        
                
        latex=self.File_Read_Lines(tex_file)
        if (tikz):
            latex=self.Latex_TikZ_Picture(latex)
            
        self.Latex_Args_Message("Latex_Document",len(latex),"lines")
        
        latex=self.Latex_Document_Begin_Add_PreAmble(tex_file,latex,tikz)
        
        #Must be AFTER adding of preamble.
        latex=self.Latex_Document_Class(tex_file,latex,tikz)
        latex=self.Latex_Document_Begin_Add_PostAmble(tex_file,latex,tikz)
        
        return [self.__Latex_Document_Class__]+latex

    
    
    ##!
    ##! Checks if document class is defined, if not, inserts.
    ##!
   
    def Latex_Document_Class(self,tex_file,latex,tikz):
        
        if (
                not self.Latex_Document_Has_Regexp(
                    tex_file,latex,
                    self.__Regexp_Document_Class__
                )
        ):
            doc_options=""
            doc_class='report'
            if (tikz):
                doc_class='standalone'
                doc_options="[tikz,dvipsnames]"
                #doc_options="[]"
            
            self.__Latex_Document_Class__="\\"+self.__Regexp_Document_Class__+doc_options+'{'+doc_class+'}'
        else:
            for i in range(len(latex)):
                if (re.search(self.__Regexp_Document_Class__,latex[i])):
                    self.__Latex_Document_Class__=latex[i]
                    latex[i]=""

        return latex

    
    ##!
    ##! Locate latex PreAmble file.
    ##!
   
    def Latex_Document_PreAmble_Locate(self,tex_file,latex,tikz):
        doc_path=re.sub(
            '/+',"/",
            self.File_PathName(tex_file)
        )

        if (not re.search('\S',doc_path)):
            doc_path=self.Path_Cwd()
            
        if (not re.search('^/',doc_path)):
            doc_path=self.Path_Cwd()+"/"+doc_path
        
        paths=doc_path.split('/')

        preamble_file=None
        while (len(paths)>0):
            fullname="/".join(paths)+"/"+self.__Latex_PreAmple__

            if (self.File_Exists( fullname )):
                preamble_file=fullname
                break

            paths.pop(len(paths)-1)

        if (preamble_file==None):
            print "Preamble not found, Paths:",paths,self.__Latex_PreAmple__
            exit()

        return preamble_file
    
    ##!
    ##! Returns contents of preamble located with Latex_Document_PreAmble_Locate.
    ##!
   
    def Latex_Document_PreAmble_Get(self,tex_file,latex,tikz):
        #Return as input!
        if (not tikz): return []
        
        return [
            '\n\n%%!',
            '%%! Preamble located by '+sys.argv[0],
            '\\input{'+self.Latex_Document_PreAmble_Locate(tex_file,latex,tikz)+'}',
            '%%!\n\n',
            '\\newcommand{\\Path}{'+self.File_PathName(tex_file)+'}',
            '\\newcommand{\\TiKZPath}{/usr/local/tikz}\n',
            '%%!\n\n',
        ]
    
    ##!
    ##! Adds preamble to latex, if adequate.    
    ##!
   
    def Latex_Document_Begin_Add_PreAmble(self,tex_file,latex,tikz):
        #Include preamble
        preamble=self.Latex_Document_PreAmble_Get(tex_file,latex,tikz)

        if (
                self.Latex_Document_Has_Regexp(
                    tex_file,latex,
                    self.__Regexp_Document_Begin__
                )
        ):

            last=None
            for n in range(len(latex)):
                if (re.search('begin\{document\}',latex[n])):
                    last=n+1
                    break

                if (not re.search('documentclass',latex[n])):
                    preamble.append(latex[n])
                
            if (last!=None):
                latex=latex[last:]

        preamble.append("\\"+self.__Regexp_Document_Begin__)

        if (self.__T__):
            preamble=preamble+[
                "%%! Animation time parameter, \T, inserted",
                "\\tikzmath{\T="+self.__T__+";}",
            ]
            
        return ["%%% Original latex doc: "+tex_file]+preamble+latex
            
    ##!
    ##! Adds postamble to latex, if adequate.    
    ##!
   
    def Latex_Document_Begin_Add_PostAmble(self,tex_file,latex,tikz):
        if (
                not self.Latex_Document_Has_Regexp(
                    tex_file,latex,
                    self.__Regexp_Document_End__
                )
        ):
            latex=latex+["\\"+self.__Regexp_Document_End__]
            
        return latex
            
    ##!
    ##! Checks if lines in latex contains regexp.
    ##!
   
    def Latex_Document_Has_Regexp(self,tex_file,latex,regexp):
        for line in latex:
            if (re.search(regexp,line)):
                return True
            
        return False
    
