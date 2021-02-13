#!/usr/bin/python

import sys,os,time

name="tikz2pdf"

desthosts=[
    "ocean",
]
files=[
   "File",
   "System",
   "Latex",
   "CGI",
   "bin/tikz2pdf.py",
]


scpbin="/usr/bin/scp"    
    
tarbin="/bin/tar"
tarflags="fz"

rtime=time.localtime()
date=time.strftime("%Y.%m.%d",time.localtime())

tarfile="/usr/local/tars/"+name+"/"+name+"."+date+".tgz"
    
os.system("/usr/local/Perl/bin/CleanTree.pl /usr/local/Python")


excludes=[
   #"--exclude=DB.rename.php",
   #Put .exclude.txt in dirs not to include in tar: Uploads e tmp
   "--exclude-tag-all=.exclude.txt"
]

#foreach 


tarcommands=[
    tarbin,
    "c"+tarflags,
    tarfile,
]+excludes+files

print "Running:\n"+" ".join(tarcommands)
os.system( " ".join(tarcommands) )
    
for desthost in desthosts:
    scpcommands=[
        scpbin,
        tarfile,
        desthost+":"+tarfile
    ] 
    print "Running:\n"+" ".join(scpcommands)
    os.system( " ".join(scpcommands) )

