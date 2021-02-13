#!/usr/bin/python

import os,re,glob

entries=glob.glob("*")
entries=sorted(entries)

files={}
for filename in entries:
    if (os.path.isfile(filename)):
        files[ filename ]=True
files=files.keys()
files.sort()

for filename in files:
    rfilename=filename

    regex='^\d+'
    rfilename=re.sub(regex,'',rfilename)
        
    regex='^\s+'
    rfilename=re.sub(regex,'_',rfilename)
        
    regex='^[_\-\.\&]+'
    rfilename=re.sub(regex,'',rfilename)
    
    regex='[\&]'
    filename=re.sub(regex,'\\)',filename)
    
    regex='[\(]'
    filename=re.sub(regex,'\\(',filename)
    rfilename=re.sub(regex,'_',rfilename)
    
    regex='[\)]'
    filename=re.sub(regex,'\\)',filename)
    rfilename=re.sub(regex,'_',rfilename)

    regex='[\']'
    filename=re.sub(regex,'\\\'',filename)
    rfilename=re.sub(regex,'\\\'',rfilename)
    
    
    regex='_[_]+'
    rfilename=re.sub(regex,'_',rfilename)
    
    regex='\s+'
    filename=re.sub(regex,'\\ ',filename)
    rfilename=re.sub(regex,'_',rfilename)


    if (filename!=rfilename):
        commands=[
            #"echo",
            "/bin/mv",
            "-f",
            filename,
            rfilename
        ]
        
        print " ".join(commands)
        try:
            output=os.system( " ".join(commands) )
        except:
            print "Unable to move: "+filename+" --> "+rfilename
            #exit()
        
