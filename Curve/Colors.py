
class Curve_Colors():
    
    ##!
    ##! Set colors
    ##!

    def Curve_Colors_Take(self,colordefs):
        bcolor=self.BackGround_Color()
        for color in colordefs.keys():
            self.Color_Schemes[ bcolor ][ color ]=colordefs[ color ]
        
    ##!
    ##! Sets Analytical Evolute colors.
    ##!

    def Evolute_Analytical_Colors(self):
        bcolor=self.BackGround_Color()
        self.Curve_Colors_Take(self.Color_Schemes_Analytical[ bcolor ])
        
 
