from math import *
import re,sys,time,os

from Vector import *
from Base import *



class CS(Base):

    #Coordinate system
    O=[]
    I=[]
    J=[]
    K=[]
    
    eps=1.0E-3
    eps2inv=0
    
    ##!
    ##! Sets eps parms.
    ##!
    
    def CS_SetParms(self,vals={}):
        self.O=Vector([0.0,0.0])
        self.I=Vector([1.0,0.0])
        self.J=Vector([0.0,1.0])
        
        self.dt=(self.t2-self.t1)/(1.0*self.NPoints)
        self.eps2inv=1.0/(2.0*self.eps)

        self.eps2inv=1.0/(2.0*self.eps)
