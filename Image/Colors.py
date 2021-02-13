
class Image_Colors():

    def BackGround_Color(self):
        if (self.W):
            return "White"
        else:
            return "Black"
   
    def BackGround(self):
        if (self.W):
            return "White"
        else:
            return "Black"
   
    def Colors_Defaults000(self):
        i=255
        grey=220

        if (self.W):
            self.BackGround_Color="White"
            self.BackGround=(255,255,255)
        else:
            self.BackGround=(0,0,0)
            self.BackGround_Color="Black"
            
        self.BackGround_Color = self.Color_Allocate( self.BackGround )
        self.Black = self.Color_Allocate( (0,0,0) )
        self.White = self.Color_Allocate( (i,i,i) )
        
        self.Red   = self.Color_Allocate( (i,0,0) )
        self.Blue  = self.Color_Allocate( (0,0,i) )
        self.Green = self.Color_Allocate( (0,i,0))
        
        self.Yellow  = self.Color_Allocate( (i,i,0))
        self.Cyan    = self.Color_Allocate( (0,i,i))
        self.Magenta = self.Color_Allocate( (i,0,i))
        self.Orange  = self.Color_Allocate( (i,169,0))
        self.Grey    = self.Color_Allocate( (grey,grey,grey))

    def Color_Allocate000(self,color_rgb):
        return self.Image.colorAllocate(color_rgb)

