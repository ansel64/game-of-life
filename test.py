# test.py
# Unit tests for the class methods
import pytest

import grid as gr
import controller as ctrl
from button import *

class Test_Grid:
    grid1 = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    grid2 = [[0, 1, 1, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0]]
                            
    mock1 = gr.Grid(grid1, 24)
    mock2 = gr.Grid(grid2, 24)

    def test_countNeighbors(self):
        assert self.mock1.countNeighbors(2, 2) == 0
        assert self.mock2.countNeighbors(2, 2) == 3


    def test_clearEdge(self):
        self.mock1.clearEdge()
        assert self.mock1.grid == self.grid1
        assert self.mock1.storage == self.grid1

        self.mock2.clearEdge()
        assert self.mock2.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 1, 0, 0],
                                   [0, 1, 0, 0, 0],
                                   [0, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0]]
        assert self.mock2.storage == [[0, 0, 0, 0, 0],
                                      [0, 0, 1, 0, 0],
                                      [0, 1, 0, 0, 0],
                                      [0, 1, 0, 0, 0],
                                      [0, 0, 0, 0, 0]]


    def test_updateGrid(self):
        self.mock1.updateGrid()
        assert self.mock1.grid == self.grid1
        assert self.mock1.storage == self.grid1

        self.mock2.updateGrid()
        assert self.mock2.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 1, 1, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0]]
        assert self.mock2.storage == self.mock2.grid


class Test_Controller:
    mock = ctrl.Controller(24, 5)
    grid = [[1, 0, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0]]
    controller = []
    
    for i in range(len(grid)):
        controller.append([])
        for cell in grid[i]:
            if cell == 0:
                controller[i].append(Button(0, 0, 24, BLACK))
            else:
                controller[i].append(Button(0, 0, 24, WHITE))
    mock.controller = controller

    def test_inputHandler(self):
        assert self.mock.inputHandler() == [[0, 0, 0, 0, 0, 0, 0],
                                            [0, 1, 0, 0, 1, 1, 0],
                                            [0, 0, 1, 1, 1, 0, 0],
                                            [0, 1, 0, 0, 1, 0, 0],
                                            [0, 0, 0, 0, 1, 0, 0],
                                            [0, 0, 1, 0, 1, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0]]
