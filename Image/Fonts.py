import os,cStringIO

class Image_Fonts():
    def Fonts_Defaults(self):
        fontlist = [
            '/usr/share/fonts/truetype/freefont/FreeSerif.ttf',
            '/usr/share/fonts/truetype/freefont/FreeSans.ttf',
            '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
        ]

        fontpath = '.'
        for f in fontlist:
            if os.path.exists(f):
                fontpath = fontpath + ':' + os.path.dirname(f)
                self.Font = os.path.abspath(f)
                break

        os.environ["GDFONTPATH"] = "fontpath"

        try:
            self.Font
        except NameError:
            print "no fonts found"
            sys.exit(1)
        
