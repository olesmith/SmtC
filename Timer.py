import time

class Timer():

    Title=""
    MTime=0
    Echo=True
    
    def __init__(self,title,echo=False):
        self.Title=title
        self.Echo=echo
        self.MTime=time.time()

        if (self.Echo):
            print title
        return

    def __del__(self):
        if (self.Echo):
            print "Done,",self.Title,time.time()-self.MTime," seconds."

        return

#Program execution timer
timer=Timer("Program Execution")
