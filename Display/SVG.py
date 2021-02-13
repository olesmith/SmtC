import re

import cairosvg

from Base import *

class Display_SVG():

    __Input_File__=""
    __Output_File__=""
    outputfile=""

    viewbox=""
    
    ##!
    ##! Reads arguments from command line.
    ##!
    
    def Display_SVG_Args(self):
        #Command line version
        if (not self.CGI_Is()):
            #Input file
            if ( len(sys.argv)>1 ):
                self.__Input_File__=sys.argv[1]
                
            #Output file
            if ( len(sys.argv)>2 ):
                self.__Output_File__=sys.argv[2]
            else:
                self.__Output_File__=self.File_BaseName(self.__Input_File__)
        else:
            self.__Input_File__=self.CGI_Query_String()

    ##!
    ##! Detect output type: SVG, PDF or PNG
    ##!
    
    def Display_SVG_Output(self):
        execname=sys.argv[0]
        execname=execname.split('/')
        execname=execname.pop()
        if (execname=="SVG"):
            return "svg"
        elif (execname=="PDF"):
            return "pdf"
        elif (execname=="PNG"):
            return "png"
        else:
            print "Invalid output type: "+execname
            exit()

            
    ##!
    ##! Detect input file name.
    ##!
    
    def Display_SVG_File_Input(self):
        fname=self.__Input_File__
        
        if (not re.search('^/',fname)):
            fname= "/".join([ "/usr/local/",fname])
        else:
            fname=re.sub('^/usr/local/', "/var/www/html/1",fname)
        
        #if (not self.File_Exists(fname)):
        #    fname= "/".join([ "/var/www/html2",self.__Input_File__])

        return fname
            
    
    ##!
    ##! Detect output file name.
    ##!
    
    def Display_SVG_File_Output(self):
        output=self.Display_SVG_Output()
        
        fname=self.__Output_File__
        if (self.CGI_Is()):
           fname ="/".join([ "/tmp",fname])
            
        fname=re.sub('\.pdf$',"",fname)

        return fname+"."+output
    

    def Display_SVG_Get(self):
        self.Display_SVG_Args()
        
        infile=self.Display_SVG_File_Input()
        lines=re.sub(
            'http://127.0.0.1/poops.css',
            'http://'+self.CGI_Host_Name()+'/poops.css',
            self.File_Read(
                self.Display_SVG_File_Input()
            )
        ).splitlines()
        
        viewbox=""
        if (len(sys.argv)>2):
            vps=[]
            for i in range(3,len(sys.argv)):
                vps.append(sys.argv[i])
            viewbox=" ".join(vps)
            
        if (viewbox):
            vs=viewbox.split(' ')
            vx=int(vs[2])-int(vs[0])
            vy=int(vs[3])-int(vs[1])
            for i in range( len(lines) ):
                regex='viewBox="([\d\s]+)"'
                if (re.search(regex,lines[i])):
                    lines[i]=re.sub(
                        regex,
                        'viewBox="'+viewbox+'"',
                        lines[i]
                    )
                    lines[i]=re.sub(
                        'width="(\d+)"',
                        'width="'+str(vx)+'"',
                        lines[i]
                    )
                    lines[i]=re.sub(
                        'height="(\d+)"',
                        'height="'+str(vy)+'"',
                        lines[i]
                    )

                    print lines[i]

        return lines

    
    def Display_SVG(self):
        if (self.CGI_Is()):
            self.Display_HTTP_Headers_Print("image/svg+xml\n")

        svg="\n".join(self.Display_SVG_Get())

        
        if (self.CGI_Is()):
            print re.sub('\&gamma;=?',"",svg)
            exit()
        else:
            svgfile=self.Display_SVG_File_Output()
            self.File_Write(svgfile,svg)
            print "Output written to",svgfile


            
    def Display_PNG(self):
        if (self.CGI_Is()):
            self.Display_HTTP_Headers_Print("image/png\n")
            
        svg="\n".join(self.Display_SVG_Get())
        pngfile=self.Display_SVG_File_Output()


        fout = open(pngfile,'w')
        cairosvg.svg2png(bytestring=svg,write_to=fout)

        fout.close()

        if (self.CGI_Is()):
            print self.File_Read(pngfile)
        else:
            print "Output written to",pngfile

    def Display_PDF(self):
        
        if (self.CGI_Is()):
            self.Display_HTTP_Headers_Print("application/pdf\n")

        svg="\n".join(self.Display_SVG_Get())
        pdffile=self.Display_SVG_File_Output()

        path=self.File_PathName(pdffile)
        cwd=os.getcwd()

        fout = open(pdffile,'w')
       
        os.chdir( path )
        cairosvg.svg2pdf(bytestring=svg,write_to=fout)
        os.chdir(cwd  )
        
        fout.close()
        if (self.CGI_Is()):
            print self.File_Read(pdffile)
        else:
            print "Output written to",pdffile


    def Display_SVG_Generate(self):
        self.Display_SVG()
