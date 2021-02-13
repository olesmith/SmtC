import os,re,glob


class Path():
    ##!
    ##! Makes sure path exists, if not tries to create it.
    ##!
    
    def Path_Create(self,path):
        paths=path.split('/')

        spath=""
        for i in range( len(paths) ):
            spath+=paths[i]+"/"
            try:
                os.stat(spath)
            except:
                print "Creating directory:",spath
                os.mkdir(spath)
                

    def Path_Exists(self,path):
        return os.path.isdir(path)

    def Path_Cwd(self):
        return os.getcwd()


    ##!
    ##! All dir entries in path.
    ##!
    
    def Path_Entries(self,path):
        entries=glob.glob(path+"/*")
        entries=sorted(entries)
        return entries

    
    ##!
    ##! 
    ##!
    
    def Path_Subdirs(self,path,withfile=None):
        paths=[]
        for entry in self.Path_Entries(path):
            if (os.path.isdir(entry)):
                if (withfile):
                    file=os.path.join(entry,withfile)
                    if (os.path.isfile(file)):
                        paths.append(entry)
                else:
                    paths.append(entry)
                    
        paths.sort()
        return paths

    ##!
    ##! Subdir (short) dir names in path
    ##!
    
    def Path_Dirs(self,path,withfile=None):
        rpaths=self.Path_Subdirs(path,withfile)
        
        subdirs=[]
        for rpath in rpaths:
            comps=rpath.split("/");
            subdirs.append( comps.pop() )
            
        return subdirs

    ##!
    ##! 
    ##!
    
    def Path_Files(self,path,regex):
        files={}
        for filename in self.Path_Entries(path):
            if (os.path.isfile(filename)):
                
                #if (re.match??(regex,os.path.basename(filename))):
                if (re.search(regex,os.path.basename(filename))):
                    files[ filename ]=True
                    
        files=files.keys()
        files.sort()

        return files

    ##!
    ##! 
    ##!
    
    def Path_Subdirs_Num(self,path):
        paths=[]
        for rpath in self.Path_Subdirs(path):
            comps=rpath.split('/')
            rpath=comps.pop()
            if (re.match('^-?[\d\.]+$',rpath)):
                paths.append(rpath)

        return paths

    
    ##!
    ##! Detect path tree of subdirs. Recursive.
    ##!
    
    def Path_Tree(self,path,regex=""):
        tree={}
        for subdir in self.Path_Dirs(path):
            rpath=path+"/"+subdir
            if (regex and (not re.match(regex,subdir)) ):
                    continue
            tree[ subdir ]=self.Path_Tree(rpath,regex)

        return tree
    
    
    ##!
    ##! From tree dictionary scanned byu Path_Tree, detect subdirs in paths (splitted list)
    ##!
    
    def Path_Tree_Subdirs_Get(self,tree,paths,fname=None):
        subtree=dict(tree)
        subpaths=[]
        
        for path in paths:
            if (path and subtree.has_key(path) ):
                subtree=subtree[ path ]

                subpaths=subtree.keys()
                subpaths.sort()

        return subpaths

    ############## First and last subdirs #########################
    
    ##!
    ##! From tree dictionary, detect first subdir
    ##!
    
    def Path_Tree_Subdirs_First(self,tree,paths):
        subpaths=self.Path_Tree_Subdirs_Get(tree,paths)

        rsubpaths=[]
        if ( len(subpaths)>0 ):
            #We have subdirs, take first
            rsubpaths=subpaths.pop( 0 )
            rsubpaths=paths+[ rsubpaths ]

        return rsubpaths

    ##!
    ##! From tree dictionary, detect last subdir
    ##!
    
    def Path_Tree_Subdirs_Last(self,tree,paths):
        subpaths=self.Path_Tree_Subdirs_Get(tree,paths)

        rsubpaths=[]
        if ( len(subpaths)>0 ):
            #We have subdirs, take first
            rsubpaths=subpaths.pop( len(subpaths)-1 )
            rsubpaths=paths+[ rsubpaths ]

        return rsubpaths


    ################## Next subdir ############################
    
    ##!
    ##! From tree dictionary, detect next subdir, do NOT consider current level subdirs.
    ##!
    
    def Path_Tree_Subdir_Next(self,tree,paths,currdir):
        subdirs=self.Path_Tree_Subdirs_Get(tree,paths)
        subpaths=[]
        for n in range( len(subdirs) ):
            if (currdir==subdirs[ n ]):
                if (n<len(subdirs)-1):
                    subpaths=paths+[ subdirs[ n+1 ] ]
                else:
                    subpaths=list(paths)
                    subpath=subpaths.pop( len(subpaths)-1 )

                    rpaths=subpaths+[ subpath ]
                    subpaths=self.Path_Tree_Subdir_Next(tree,subpaths,subpath)

        return subpaths
    
    ##!
    ##! From tree dictionary, detect next subdir, consider current level subdirs.
    ##!
    
    def Path_Tree_Subdirs_Next(self,tree,paths):
        subpaths=self.Path_Tree_Subdirs_First(tree,paths)

        if ( not subpaths and len(paths)>0):
            rpaths=list(paths)
            thisdir=rpaths.pop( len(rpaths)-1 )
            subpaths=self.Path_Tree_Subdir_Next(tree,rpaths,thisdir)
        return subpaths

    ################## Previous subdir ############################
    
    ##!
    ##! From tree dictionary, detect previous subdir, do NOT consider current level subdirs.
    ##!
    
    def Path_Tree_Subdir_Previous(self,tree,paths,currdir):

        subdirs=self.Path_Tree_Subdirs_Get(tree,paths)
        subpaths=[]
        for n in range( len(subdirs) ):
            if (currdir==subdirs[ n ]):
                if (n>0):
                    subpaths=paths+[ subdirs[ n-1 ] ]
                else:
                    subpaths=list(paths)
                    if ( len(subpaths)>0 ):
                        subpath=subpaths.pop( len(subpaths)-1 )

                        rpaths=subpaths+[ subpath ]
                        subpaths=self.Path_Tree_Subdir_Previous(tree,subpaths,subpath)

        return subpaths
    
    ##!
    ##! From tree dictionary, detect previous subdir, consider current level subdirs.
    ##!
    
    def Path_Tree_Subdirs_Previous(self,tree,paths):
        subpaths=self.Path_Tree_Subdirs_Last(tree,paths)
        if ( not subpaths and len(paths)>0):
            rpaths=list(paths)
            thisdir=rpaths.pop( len(rpaths)-1 )
            subpaths=self.Path_Tree_Subdir_Previous(tree,rpaths,thisdir)
        return subpaths

    ##!
    ##! From tree dictionary, detect previous subdir, consider current level subdirs.
    ##!
    
    def Path_Tree_Files(self,base_path,files_regexp=None,contents_regexp=None):
        tree=self.Path_Tree(base_path)

        files=[]
        
        path=base_path
        for subdir in tree.keys():
            rpath=path+"/"+subdir

            rfiles=self.Path_Files(rpath,files_regexp)
            for rfile in rfiles:
                contents=self.File_Read(rfile)
                if (re.search(contents_regexp,contents, flags=re.IGNORECASE)):
                    files.append(rfile)
                    break

            if (not os.path.islink(rpath)):
                files=files+self.Path_Tree_Files(rpath,files_regexp,contents_regexp)

        return files

            
    ##!
    ##! From tree dictionary, detect previous subdir, consider current level subdirs.
    ##!
    
    def Path_Tree_Paths(self,base_path,files_regexp=None,contents_regexp=None):
        paths={}
        for fname in self.Path_Tree_Files(base_path,files_regexp,contents_regexp):
            paths[ self.File_PathName(fname) ]=True

        paths=paths.keys()

        return paths
