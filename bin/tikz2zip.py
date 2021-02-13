#!/usr/bin/python


import sys,argparse

sys.path.append("/usr/local/Python")

from File import *
from System import *
from Latex import *
from CGI import *

def Process(tikz_file,verbose,noclean):
    path=File().File_Path(tikz_file)
    if (path): path=path+"/"
    
    pdf_out_file=path+re.sub(
        '\.tikz\.tex',
        ".pdf",
        File().File_BaseName(tikz_file)
    )

    if (not File().File_Exists(tikz_file)):
        System_Error_And_Die([
            "No such file: "+tikz_file,
            sys.argv[0]+",usage syntax:",
            "\t"+sys.argv[0]+"file.tikz.tex"
        ])


    pid="tikz2zip-"+str(os.getpid())
    
    tex_tmp_path="/".join([
        Latex().tmp_path,
        pid
    ])

    tex_tmp_file="/".join([
        tex_tmp_path,
        re.sub(
            '\.tikz\.tex',
            ".tex",
            File().File_BaseName(tikz_file)
        )
    ])
    
    rel_tex_tmp_file=re.sub(
        '\.tikz\.tex',
        ".tex",
        File().File_BaseName(tikz_file)
    )

    zip_file="/".join([
        tex_tmp_path,
        re.sub(
            '\.tikz\.tex',
            ".zip",
            File().File_BaseName(tikz_file)
        )
    ])

    latex=Latex().Latex_Document(tikz_file)
    for n in range(len(latex)):
        latex[n]=re.sub('/usr/local/tikz','tikz',latex[n])



    File().File_Write(tex_tmp_file,latex,verbose)

    files=Latex().Latex_Inputs(tikz_file,latex)
    
    main_name=files.pop(0)

    commands=[]
    if (not File().File_Exists(tex_tmp_path)):
        os.mkdir(tex_tmp_path)
    

    files_done={}
    
    for fname in files:
        if (files_done.has_key(fname)):
            continue
        
        rfname=fname
        if (re.search('/usr/local/tikz/',fname)):
            rfname=re.sub('/usr/local/tikz/','tikz/',fname)

        
        path=os.path.dirname(tex_tmp_path+"/"+rfname)
        
        if (not File().File_Exists(path)):
            os.mkdir(path)
            
        lines=File_Read(fname)
        for n in range(len(lines)):
            lines[n]=re.sub('/usr/local/tikz','tikz',lines[n])

        File().File_Write(tex_tmp_path+"/"+rfname,lines)
        
        files_done[ fname ]=rfname

    commands.append(
        [
            "/bin/rm -f",
            zip_file,
        ]
    )
    
    commands.append(
        [
            "/usr/bin/zip",
            zip_file,
            rel_tex_tmp_file,
        ]+files_done.values()
    )



    res=System().System_Execs(commands,tex_tmp_path,verbose)
    if (CGI().CGI_Is()):
        if (res==0):
            print "Content-type: application/zip"
            print "Content-Disposition: attachment; filename="+os.path.basename(zip_file)
            print ""
            
            f=open(zip_file,"rb")
            print f.read()
            f.close()

            exit()
            
    else:
        zip_in="/".join([
            #tex_tmp_path,
            zip_file,
        ])
        
        zip_out=re.sub(r'\.tikz\.tex',"",tikz_file)+'.zip'
        print zip_in,zip_out,'created'
        System().System_Exec([
            "/bin/cp",zip_in,zip_out
        ])

    if (not noclean):
        System().System_Exec([
            "/bin/rm -rf",
            tex_tmp_path
        ])
        


#MAIN EXECUTION
#Get Command Arguments: CGI or not


parser=argparse.ArgumentParser(
    description='ZIP TiKZ with dependencies',
    add_help=False
)

parser.add_argument(
    dest='tikz_files',
    metavar='tikz_file',
    nargs='+'
)

parser.add_argument(
    '-v','-verbose',
    dest='verbose',
    action='store_true',
    help='Echo criation of zip file and other actions take.'
)

parser.add_argument(
    '-n','-noclean',
    dest='noclean',
    action='store_true',
    help='Do not delete criated files afterwards.'
)


verbose=False
noclean=False

if (CGI().CGI_Is()):
    import cgitb
    cgitb.enable()

    tikz_files=[
        "/".join([
            CGI().CGI_Doc_Root(),
            CGI().CGI_POST("Src"),
        ])
    ]
else:
    args=parser.parse_args()
    tikz_files=args.tikz_files

    verbose=args.verbose
    noclean=args.noclean

#Test arguments
if (len(tikz_files)<1):
    if (CGI().CGI_Is()):
        print "Content-type: text/html\n\n"

    System().System_Error_And_Die([
        sys.argv[0]+",usage:",
        "[-v(erbose)]",
        "\t"+sys.argv[0]+"file.tikz.tex"
    ])
    exit(1)

    
for tikz_file in tikz_files:
    if (File().File_Exists(tikz_file)):
        Process(tikz_file,verbose,noclean)
    else:
        print "Content-type: text/html\n\n"

        print "No such file: "+tikz_file
        CGI().CGI_ENV_Show()
