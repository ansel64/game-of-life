# button.py
from pyray import *

# A square button with position x and y, 
# size (side length), and its current color
class Button(object):
    def __init__(self, x: int, y:int , size: int, color) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    
    # Draws the button to the screen at its appropriate position
    def drawButton(self) -> None:
        # Draw the square one pixel smaller to give the 'grid' effect.
        draw_rectangle(self.x+1, self.y+1, self.size-1, self.size-1, self.color)
