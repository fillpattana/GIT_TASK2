from turtle import *

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        
    def showdisk():
        for i in range(4):
            fd(50)
            right(90)
            showturtle
            exitonclick
    
    def newpos(self, xpos, ypos):
        pass
    
    def cleardisk(self):
        pass
    
    showdisk()