import time


class Time():
    def Time_Text(self,mtime=None):
        if (mtime==None): mtime=time.localtime()
        
        return time.strftime('%Y.%m.%d-%H.%M.%S',mtime)
