from pyray import *
from button import *

class Controller(object):
    def __init__(self, buttonSize: int, controllerSize: int) -> None:
        '''Create a 2d array of buttons that corresponds to the logic grid.'''
        self.buttonSize = buttonSize
        self.controllerSize = controllerSize
        self.controller = []

        for i in range(controllerSize):
            self.controller.append([])
            for j in range(controllerSize):
                self.controller[i].append(Button(i * buttonSize, j * buttonSize, buttonSize, BLACK))


    def drawController(self) -> None:
        '''Draw the controller to screen.'''
        controller = self.controller

        clear_background(WHITE)
        begin_drawing()

        for row in controller:
            for button in row:
                button.drawButton()

        end_drawing()


    def clickHandler(self, mouseX: int, mouseY: int) -> None:
        '''Change the button's color when it's clicked'''
        i = mouseX // self.buttonSize # For whatever reason the mouse positions are switched
        j = mouseY // self.buttonSize
        button = self.controller[i][j]
        
        if button.color == BLACK: button.color = WHITE
        else: button.color = BLACK


    def inputHandler(self) -> list:
        '''Converts the controller to grid format. This also means creating 2 extra rows and columns for the edges'''
        controller = self.controller
        grid = []

        for i in range(len(controller)):
            grid.append([])
            for j in range(len(controller[i])):
                button = controller[j][i]
                
                if j == 0: 
                    grid[i].append(0)

                if button.color == WHITE: grid[i].append(1)
                else: grid[i].append(0)

                if j == len(controller[i]) - 1: 
                    grid[i].append(0)

        grid.insert(0, [0] * (self.controllerSize + 2))
        grid.append([0] * (self.controllerSize + 2))

        return grid
