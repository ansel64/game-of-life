from pyray import *
from button import *

class Controller(object):
    def __init__(self, buttonSize, gridSize):
        self.buttonSize = buttonSize
        self.gridSize = gridSize
        self.controller = []

        for i in range(gridSize):
            self.controller.append([])
            for j in range(gridSize):
                self.controller[i].append(Button(j * buttonSize, i * buttonSize, buttonSize, BLACK))
