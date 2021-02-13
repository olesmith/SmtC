from math import *
from Vector import *
from XML import *
from Canvas2 import Canvas2

class Mesh(list,XML):
    Point_Size=3
    Last_Point_Size=5
    Draw_Connections=True
    Draw_Mesh=False
    Point_Size=3
    
    Color="Black"

    __PX__=[]
    Name="Mesh"
    
    def __init__(self,name="Mesh",arg=None,dim=2):
        if (not arg): arg=[]
        
        if (name.__class__.__name__=="str"):
            self.Name=name
            
        if (arg.__class__.__name__=="int"):
            #arg is an int, calloc so many points
            for i in range(arg):
                self.append( Vector(dim) )
        elif (arg.__class__.__name__=="list"):
            #arg is a list of points, transfer to self.
            for i in range( len(arg) ):
                self.append( arg[i] )

        __PX__=[]
        #print "Mesh init",self.Name


    def __str__(self):
        text=""
        text=text+"Mesh: "+self.Name+". "
        text=text+str(len(self) )+" Nodes"

        return text
    def Max(self):
        vmax=Vector(self[0])
        for i in range( len(self) ):
            vmax=vmax.Max(self[i])

        return vmax
                
    def Min(self):
        vmin=Vector(self[0])
        for i in range( len(self) ):
            vmin=vmin.Min(self[i])

        return vmin
                
    def P2Pix(self,canvas,i):
        if ( len(self.__PX__)==0 ):
            self.Ps2Pix(canvas)

        return self.__PX__[i]
    
    def Ps2Pix(self,canvas):
        if (not self.__PX__):
            self.__PX__=canvas.Ps2Pix(self)

        return self.__PX__
    
    def Draw_Node(self,canvas,color,n):
        classs=self.Name+"_Last"

        if ( n<len(self) ):
            canvas.Draw_Point(self[n],self.Point_Size,classs,color)
            
    def Draw_Nodes(self,canvas,color,size=0,every=1):
        canvas.Image_SVG_Comment("Drawing Curve Nodes: "+self.Name)
        classs=self.Name+"_Mesh"
        textclasss=self.Name+"_Text"

        if (size==0):
            size=self.Point_Size

        canvas.Draw_Nodes(self,size,classs,textclasss,color,{},{},every)
            
    def Draw_Curve(self,canvas,color,n):
        canvas.Image_SVG_Comment("Drawing Curve Connections: "+self.Name)
        classs=self.Name+"_Conn"
        lclass=self.Name+"_Conn_Last"

        pxs=self.Ps2Pix(canvas)
        pxs1=pxs[0:n]
        pxs2=pxs[n:len(pxs)-1]
        canvas.Image_Draw_Mesh(pxs1,classs,color)
        canvas.Image_Draw_Mesh(pxs2,lclass,color)
         
            
    def Draw_Connection(self,canvas,conn,color):
        i=conn[0]
        j=conn[1]

        classs="Conn"

        canvas.Image_Draw_Line(
            self.P2Pix(canvas,i),
            self.P2Pix(canvas,j),
            classs,
            color
        )
            
    def Draw_Connections(self,canvas,conns,classs):        
        for i in range( len(conns) ):
            self.DrawConnection(canvas,conns[i],color)
        


    def Draw_Both(self,canvas,color,n):
        canvas.Image_SVG_Comment("Drawing Curve: "+self.Name)
        canvas.Image_Add_Open_Tag(
            "g",
            {
                "style": {
                },
                "id": self.Name,
            }
        )
        self.Draw_Curve(canvas,color,n)

        canvas.Image_Add_Close_Tag("g")

        
    def Mesh_SVG(self,canvas,svgname,classs,color="red",parms={},meshes=[],svg=[]):
        if (not color): color=self.Color
        
        body=[]
        for mesh in meshes:
            body=body+mesh.Mesh_SVGs(canvas,"Curve","",parms)
            
        body=body+self.Mesh_SVGs(canvas,classs,color,parms)+svg
        
        self.File_Write(
            svgname,
            self.SVG_Pre_Amble(canvas)+body+self.SVG_Post_Amble(canvas),
            True
        )

    def Mesh_SVGs(self,canvas,classs,color="yellow",parms={}):
        if (not color): color=self.Color

        svg=[]
        if (self.Draw_Mesh):
            svg=svg+canvas.SVG_Mesh(
                canvas.Ps2Pix(self),
                self.Point_Size,
                classs+"_Mesh",
                color,
                parms
            )

        if (self.Draw_Connections):
            svg=svg+canvas.SVG_Conns(
                canvas.Ps2Pix(self),
                classs+"_Conn",
                color,
                parms
            )

        return svg

    def Mesh_Write_Nodes(self,file):
        text=[]
        for n in range( len(self) ):
            line=[ str(n) ]
            for i in range( len(self[n]) ):
                line.append( str(self[n][i]) )

            text.append( "\t".join(line) )

        return self.File_Write(file,text,True)


    def Mesh_SVG_Draw_With_Coordinate_System(self,svgfile,classs,color,resolution,curves=[]):
        fmin=self.Min()
        fmax=self.Max()
        
        curves.append(
            Mesh(
                "X",
                [
                    [ fmin[0],0.0 ],
                    [ fmax[0],0.0 ],
                ]
            )
        )

        curves.append(
            Mesh(
                "Y",
                [
                    [ 0.0,fmin[1] ],
                    [ 0.0,fmax[1] ],
                ]
            )
        )

        self.Mesh_SVG(
            Canvas2(
                {},
                [ fmin,fmax ],
                resolution
            ),
            svgfile,
            classs,
            color
        )

