from math import *


from Vector import Vector

class Matrix(list):

    def __init__(A,B=[]):
        A.__Alloc__(B)
         
        for i in range(len(B)):
            for j in range(len(B[i])):
                A[i][j]=1.0*B[i][j]

    def __Alloc__(A,B):
        for i in range(len(B)):
            A.append([])
            for j in range(len(B[i])):
                A[i].append(0.0)
        
    def __add__(A,other):        
        B=Matrix(A)
        for i in range(len(other)):
            for j in range(len(other[i])):
                B[i][j]+=other[i][j]
        return B
    
    def __mul__(A,other):
        if (other.__class__.__name__=="int"):
            other*=1.0
            
        if (other.__class__.__name__=="float"):
            B=Matrix()
            for i in range( len(A) ):
                B.append( [] )
                for j in range( len(A[i]) ):
                    B[i].append(  A[i][j]*other  )

            return B

        if (other.__class__.__name__=="Vector"):
            v=Vector( len(A) )
            for i in range( len(A) ):
                v[i]=0.0
                for j in range( len(other) ):
                    v[i]+=A[i][j]*other[j]

            return v

        print "Matrix:: Invalid second argument type in __mul__:",other.__class__.__name__
        #exit()
    
    def __str__(A):
        text="["
        for i in range( len(A) ):
            text+="\n  ["
            for j in range( len(A[i]) ):
                text+=str(A[i][j])
                if ( j+1<len(A[i]) ):
                    text+=","
                    
            if (i+1<len(A)):
                text+="],"
            else:
                text+="]\n]"
        return text
            

    
    def Matrix_Column(A,i):
        v=Vector()
        v.__Alloc__(len(A[i]))
        for j in range( len(v) ):
            v[j]=A[j][i]
        return v

    def Matrix_Line(A,i):
        v=Vector()
        v.__Alloc__(len(A))
        for j in range( len(v) ):
            v[j]=A[i][j]
        return v

    def Trace(A):
        tr=0.0
        for i in range( len(A) ):
            tr+=A[i][i]

        return tr


    def Transpose(A):
        AT=Matrix([])
        for j in range(len(A[0])):
            AT.append( [] )
            for i in range(len(A)):
                AT[j].append( A[i][j] )

        return AT
        


    def MultiplyRow(A,i,c):
        for j in range( len(A[i]) ):
            A[i][j]*=c
        
    #Do row operation A_j-cA_i       
    def RowOperation(A,i,j,c):
        for k in range( len(A[i]) ):
            A[j][k]-=c*A[i][k]
            
    def SwapRows(A,i,j):
        if (i==j):
            return
        for k in range( len(A[i]) ):
            tmp=A[i][k]
            A[i][k]=A[j][k]
            A[j][k]=tmp

        
    def FindPivote(A,n):
        large=abs(A[n][n])
        pos=n
        for i in range(n,len(A)):
            if (abs(A[i][n])>large):
                large=abs(A[i][n])
                pos=i
                
        return i

    def GaussForward(self):
        #Make a copy in order not to change
        A=Matrix(self)
        
        #loop over diagonal elements
        det=1.0
        for i in range( len(A) ):
            ii=A.FindPivote(i)
            if (i!=ii):
                A.SwapRows(i,ii)
                det*=-1.0
            
            c=A[i][i]
            det*=c
            if (c==0.0):
                print "Matrix Singular at position",str(i+1)
                return 0.0
            
            A.MultiplyRow(i,1.0/c)
            for j in range(i+1,len(A)):
                #A_j=A_j-cA_i, c=A_i_j
                A.RowOperation(i,j,A[j][i])            
        return det

    def Determinant(A):
        return A.GaussForward()
    
    def Discriminant(A):
        return (A[0][0]-A[1][1])**2.0+4.0*A[0][1]*A[1][0]

    def Eigen_Values(A):
        tr=A.Trace()
        delta=A.Discriminant()

        lambdas=[]
        if (delta>=0):
            delta=sqrt(delta)
            lambdas=[
                (tr-delta)*0.5,
                (tr+delta)*0.5,
            ]
        return Vector(lambdas)
    
    def Eigen_Vectors2(A,lambdas=[]):
        if (not lambdas): lambdas=A.Eigen_Values()

        v0=Vector([
            lambdas[0]-A[0][0],
            A[1][0]
        ])
        
        if (abs(lambdas[0]-A[0][0])==0.0):
            v0=Vector([1.0,0.0])
            
        v0=v0.Normalize()
        v1=v0.Transverse2()
        
        return Matrix([
            [ v0[0],v1[0] ],
            [ v0[1],v1[1] ],
        ])

    
    def Quadratic_Diagonalize(A,b=None,c=1.0):
        if (not ): b=[0.0,0.0]

        lambdas=self.Quadratic_Eigen_Values()
        D=self.Eigen_Vectors(lambdas)

        return [ lambdas,D ]
        
def Kronecker(i,j):
    res=0.0
    if (i==j): res=1.0

    return res
    
def I(n):
    I=Matrix()
    for i in range(n):
        I.append([])
        for j in range(n):
            I[i].append( Kronecker(i,j) )

    return I

def Diagonal(v):
    D=Matrix()
    for i in range(n):
        D.append([])
        for j in range(n):
            D[i].append( v[i]*Kronecker(i,j) )

    return D
