#!/usr/bin/python


import sys,re

sys.path.append('/usr/local/Python')


from CGI import CGI
from File import File

debug=False

base_paths=[
    "/var/www/html",
    "/usr/local",
    "/usr/local/Slides",
]

if (debug):
    import cgi
    import cgitb
    cgitb.enable()


cgiobj=CGI()
get=cgiobj.CGI_GET()
if (debug):
    cgiobj.CGI_HTTP_Header_Print()

def Header(fname):
    header=""
    if (re.search('\.pdf$',fname)):
        header="pdf"
    elif (re.search('\.jpg$',fname)):
        header="jpg"
    elif (re.search('\.png$',fname)):
        header="png"
    elif (re.search('\.svg$',fname)):
        header="svg"

    elif (re.search('\.tex$',fname)):
        header="tex"
    elif (re.search('\.(tgz|tar.gz)$',fname)):
        header="tgz"

    return header
    
if (get.has_key("File")):
    fname=get[ "File" ]
    header=Header(fname)
    for base_path in base_paths:
        fobj=File()
        if (fobj.File_Exists(base_path+fname)):

            cgiobj.CGI_HTTP_Header_Print(header,fname)
            print fobj.File_Read(base_path+fname)
            exit()
    
    cgiobj.CGI_HTTP_Header_Print()
    print fname,"non-existent"
