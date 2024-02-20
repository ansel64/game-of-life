from pyray import *

class Button(object):
    '''A square button with position x and y, size (side length), and its current color.'''
    def __init__(self, x: int, y:int , size: int, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    

    def drawButton(self):
        '''Draws the button to the screen at its appropriate position.'''
        draw_rectangle(self.x+1, self.y+1, self.size-1, self.size-1, self.color) # Draw the square one pixel smaller to give the 'grid' effect.
