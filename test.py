import pytest
import sys
# sys.path.insert(1, '/Users/ksvni/Documents/Project/Python/game-of-life/src/')

import grid as gr
import button
import controller as ctrl

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


class Test_Button:
    mock1 = button.Button(5, 4, 10, '')

    def test_isMouseHover(self):
        assert self.mock1.isMouseHover(5, 4) == True
        assert self.mock1.isMouseHover(15, 14) == True
        assert self.mock1.isMouseHover(9, 13) == True
        assert self.mock1.isMouseHover(4, 2) == False
        assert self.mock1.isMouseHover(19, 15) == False


class Test_Controller:
    def test_inputHandler(self):
        pass
