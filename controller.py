from pyray import *
from button import *

class Controller(object):
    def __init__(self, buttonSize, controllerSize):
        '''Create a 2d array of buttons that corresponds to the logic grid.'''
        self.buttonSize = buttonSize
        self.controllerSize = controllerSize
        self.controller = []

        for i in range(controllerSize):
            self.controller.append([])
            for j in range(controllerSize):
                self.controller[i].append(Button(i * buttonSize, j * buttonSize, buttonSize, BLACK))


    def drawController(self):
        '''Draw the controller to screen.'''
        controller = self.controller

        clear_background(WHITE)
        begin_drawing()

        for row in controller:
            for button in row:
                button.drawButton()

        end_drawing()


    def clickHandler(self, mouseX: int, mouseY: int) -> None:
        '''When mouse is clicked, locate the button that was clicked and change its state.'''
        i = mouseY // self.buttonSize # For whatever reason the mouse positions are switched
        j = mouseX // self.buttonSize
        button = self.controller[i][j]
        
        if button.color == BLACK:
            button.color = WHITE
        else:
            button.color = BLACK


    def inputHandler(self) -> list:
        '''Converts the controller to grid format. This also means creating 2 extra rows and columns for the edges'''
        controller = self.controller
        grid = []

        return grid
