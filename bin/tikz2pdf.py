#!/usr/bin/python

import sys,argparse

sys.path.append("/usr/local/Python")

from File import *
from System import *
from Latex import *
from CGI import *



##
## Generates PDF or SVG or PNG from .tex or tikz.tex.
##
## Create symbolic links to this script:
##
## tikz2XXX: Treat as TiKZ:
##   use standalone docstyle and
##   insert begin/end tikzpicture.
## Will create encapsulated PDF.
##
## tikz2pdf: Just create the PDF.
## tikz2svg: Create PDF and run pdf2svg.
## tikz2png: Create PDF and run ghostscript to create a png.
##
## latex2pdf: Run latex generating fullpage PDF.


##
## Command line arguments: see with -h
##
## If runned as CGI script, be silent.
## Input file should be in GET File=.
##
## If runned from command line, process
## files listed as last arguments.
##


#MAIN EXECUTION

verbose=False
noclean=False
force=False
silent=False


test=False
if (test):
    noclean=True
    force=True
    print "Content-type: text/html\n"


if (CGI().CGI_Is()):
    import cgitb
    cgitb.enable()


Latex().Latex_Process_Files()
