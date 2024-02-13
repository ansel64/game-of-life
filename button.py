from pyray import *

class Button(object):
    def __init__(self, x: int, y:int , size: int, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    

    def drawButton(self):
        '''Draw the button to the screen.'''
        draw_rectangle(self.x+1, self.y+1, self.size-1, self.size-1, self.color)
