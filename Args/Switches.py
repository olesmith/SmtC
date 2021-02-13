#from subprocess import call
import os,sys,re

   
class Args_Switches():
    ##! 
    ##! self.__Switches__ acessor.
    ##!
    
    def Switches_Get(self,switch=None,key=None):
        if (switch):
            if (self.__Switches__.has_key(switch)):
                if (key):
                    if (self.__Switches__[ switch ].has_key(key)):
                        return self.__Switches__[ switch ][ key ]
                else:
                    return self.__Switches__[ switch ]
        else:
            return self.__Switches__

        return None
    
    ##! 
    ##! Returns info hash associated with switch
    ##!
    
    def Switch_2_Hash(self,switch):
        return self.Switches_Get(switch)
    
    ##! 
    ##! Returns attribute name associated with switch
    ##!
    
    def Switch_2_Attr(self,switch):
        return self.Switches_Get(switch,"Attr")
    
    ##! 
    ##! Returns text (user info) associated with switch
    ##!
    
    def Switch_2_Text(self,switch):
        return self.Switches_Get(switch,"Text")
    
    ##! 
    ##! Returns type associated with switch: int, float, str and bool
    ##!
    
    def Switch_2_Type(self,switch):
        return self.Switches_Get(switch,"Type")
        
    ##! 
    ##! Parse switches for usable object switch/attribute values
    ##!
    
    def Switches_2_Obj(self,switches):
        for switch in switches:
            info=self.Switch_2_Hash(switch)
            if (info):
                type=self.Switch_2_Type(switch)
                attr=self.Switch_2_Attr(switch)
                
                value=switches[ switch ]
                
                self.Value_2_Attr(attr,type,value,"Switch")
 
