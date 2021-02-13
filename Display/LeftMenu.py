from Base import *

import os

class Display_LeftMenu():
    ##! 
    ##! Generates Display left menu. Overrides method in HTML class.
    ##!
    
    def Parameter_Name(self,name):
        return self.Setup[name]
    ##! 
    ##! Generates Display left menu. Overrides method in HTML class.
    ##!
    
    def HTML_Left_Menu(self):

        url=self.CGI_Script_Name()

        html=[]
        items=[self.A(url,"Start")]

        bpath="/".join(   [ self.FS_Root,self.BasePath ]  )
        for path in self.Path_Subdirs(bpath,"Setup.inf"):
            comps=path.split('/')
            rpath=comps.pop()
            items.append(self.Display_LeftMenu_Path(rpath))

        self.Setup={}
        dpath="/".join( [ self.Display_Setup_Path(), ] )
        
        self.Display_Setup_Read(dpath)
         
        html=html+[ self.HTML_List_Old(items) ]
        
        return html
    
    ##! 
    ##! Returns current value of a
    ##!
    
    def Display_Parm_Get(self,n,path,subdirs):
        parms=self.Display_Animation_Parms()
        a=None

        if ( len(parms)>n ):
            a=parms[n]
        elif ( len(subdirs)==1):
            a=subdirs[0]
            
        return a
    

            
    ##! 
    ##! Generates Display left menu entry for path
    ##!
    
    def Display_LeftMenu_Path(self,path):
        apath="/".join( [ self.FS_Root,self.BasePath,path ] )
        aapath="/".join( [ self.BasePath,path ] )

        self.Setup={}
        self.Display_Setup_Read(aapath)
  
        
        url=self.CGI_Script_Name()+"?"+"/".join( [ self.BasePath,path ])

        html=self.A(url, self.Display_Setup_Key("Name") )

        animation=self.Display_Animation()
        
        query=self.CGI_Query_Path()
        dpath=self.Display_Setup_Path()

        if (apath == dpath):
            items=[]

            subdirs=self.Path_Subdirs_Num(apath)
            for a in subdirs:
                items.append( self.Display_LeftMenu_Path_a(path,a,subdirs) )

            html=html+self.HTML_List_Old(items)
            
       
        return html
    
    ##! 
    ##! Generates Display left menu entry for a value a
    ##!
    
    def Display_LeftMenu_Path_a(self,path,a,subdirs):
        rpath="/".join( [ path,str(a) ] )
        apath="/".join( [ self.FS_Root,self.BasePath,rpath ] )
        url=self.CGI_Script_Name()+"?"+"/".join( [ self.BasePath,rpath ])

        aa=self.Display_Parm_Get(1,path,subdirs)

        html=""
        if (aa==a):
            html=self.Parameter_Name("a")+"="+str(a)
            items=[]
            subdirs=self.Path_Subdirs_Num(apath)
            for b in subdirs:
                items.append( self.Display_LeftMenu_Path_a_b(path,a,b,subdirs) )

            html=html+self.HTML_List_Old(items)
        else:
            html=self.A(url,self.Parameter_Name("a")+"="+str(a))
        
        return html
    
    ##! 
    ##! Generates Display left menu entry for a,b values
    ##!
    
    def Display_LeftMenu_Path_a_b(self,path,a,b,subdirs):
        rpath="/".join( [ path,str(a),str(b) ] )
        apath="/".join( [ self.FS_Root,self.BasePath,rpath ] )
        url=self.CGI_Script_Name()+"?"+"/".join( [ self.BasePath,rpath ])

        bb=self.Display_Parm_Get(2,path,subdirs)

        html=""
        if (bb==b):
            html=self.Parameter_Name("b")+"="+str(b)

            items=[]
            subdirs=self.Path_Subdirs_Num(apath)
            for c in subdirs:
                items.append( self.Display_LeftMenu_Path_a_b_c(path,a,b,c,subdirs) )

            html=html+self.HTML_List_Old(items)
        else:
            html=self.A(url,self.Parameter_Name("b")+"="+str(b))

        return html
    
    ##! 
    ##! Generates Display left menu entry for a,b,c values
    ##!
    
    def Display_LeftMenu_Path_a_b_c(self,path,a,b,c,subdirs):
        rpath="/".join( [ path,str(a),str(b),str(c) ] )
        apath="/".join( [ self.FS_Root,self.BasePath,rpath ] )
        url=self.CGI_Script_Name()+"?"+"/".join( [ self.BasePath,rpath ])

        cc=self.Display_Parm_Get(3,path,subdirs)

        if (cc==c):
            html=self.Parameter_Name("c")+"="+str(c)
            
            items=[]
            subdirs=self.Path_Subdirs_Num(apath)
            for n in subdirs:
                items.append( self.Display_LeftMenu_Path_a_b_c_n(path,a,b,c,n,subdirs) )

            html=html+self.HTML_List_Old(items)
        else:
            html=self.A(url,self.Parameter_Name("c")+"="+str(c))


        return html

    
    ##! 
    ##! Generates Display left menu entry for a,b,c,n values
    ##!
    
    def Display_LeftMenu_Path_a_b_c_n(self,path,a,b,c,n,subdirs):
        rpath="/".join( [ path,str(a),str(b),str(c),str(n) ] )
        apath="/".join( [ self.FS_Root,self.BasePath,rpath ] )
        url=self.CGI_Script_Name()+"?"+"/".join( [ self.BasePath,rpath ])

        html=self.A(url,"n="+str(n))

        return html
