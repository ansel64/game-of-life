from pyray import *
from button import *

class Controller(object):
    def __init__(self, buttonSize, controllerSize):
        self.buttonSize = buttonSize
        self.controllerSize = controllerSize
        self.controller = []

        for i in range(controllerSize):
            self.controller.append([])
            for j in range(controllerSize):
                self.controller[i].append(Button(j * buttonSize, i * buttonSize, buttonSize, BLACK))


    def drawController(self):
        '''Draw the entire controller to screen.'''
        controller = self.controller

        clear_background(WHITE)
        begin_drawing()

        for row in controller:
            for button in row:
                button.drawButton()

        end_drawing()


    def inputHandler(self):
        '''Converts the controller to grid format.'''
        controller = self.controller
        grid = []

        for i in range(len(controller)):
            grid.append([])
            for button in controller[i]:
                if button.color == WHITE:
                    grid[i].append(1)
                else:
                    grid[i].append(0)
