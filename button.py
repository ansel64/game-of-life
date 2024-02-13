from pyray import *

class Button(object):
    def __init__(self, x: int, y:int , size: int, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    

    def isButtonClicked(self, mouseX, mouseY):
        x = self.x
        y = self.y
        size = self.size

        return (mouseX >= x and mouseX <= x + size) and (mouseY >= y and mouseY <= y + size)


    def drawButton(self):
        begin_drawing()

        draw_rectangle(self.x+1, self.y+1, self.size-1, self.size-1, self.color)

        end_drawing()
