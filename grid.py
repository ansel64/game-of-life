import copy
from pyray import *

class Grid(object):
    def __init__(self, grid: list, cellSize: int) -> None:
        '''Create two copies of the given list, one for updating and another for storing.'''
        self.grid = grid
        self.storage = copy.deepcopy(grid)
        self.gridSize = len(grid)
        self.cellSize = cellSize


    def updateGrid(self) -> None:
        '''Updates the grid based on Conway's rule.'''
        grid = self.grid
        storage = self.storage
        gridSize = self.gridSize

        Grid.clearEdge(self)

        for i in range(1, gridSize-1):
            for j in range(1, gridSize-1):
                totalNeighbors = Grid.countNeighbors(self, i, j)
                cell = storage[i][j]

                if cell == 0 and totalNeighbors == 3:
                    grid[i][j] = 1
                elif cell == 1 and (totalNeighbors < 2 or totalNeighbors > 3):
                    grid[i][j] = 0
                elif cell == 1 and (totalNeighbors == 2 or totalNeighbors == 3):
                    grid[i][j] = 1

        self.storage = copy.deepcopy(grid)


    def countNeighbors(self, i: int, j: int) -> int:
        '''Count the surrounding alive cells at the given cell index.'''
        grid = self.storage
        return (grid[i][j-1] + grid[i][j+1]) + (grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]) + (grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1])


    def clearEdge(self) -> None:
        '''Kill all the cells that reaches the edge of the grid.'''
        grid = self.grid
        storage = self.storage

        grid[0] = [0] * len(grid)
        grid[(len(grid) - 1)] = [0] * len(grid)

        storage[0] = [0] * len(grid)
        storage[(len(grid) - 1)] = [0] * len(grid)

        for i in range(len(grid)):
            grid[i][0] = 0
            grid[i][(len(grid) - 1)] = 0

            storage[i][0] = 0
            storage[i][(len(grid) - 1)] = 0


    def drawGrid(self):
        '''Draw the grid to the screen.'''
        grid = self.grid
        gridSize = self.gridSize
        cellSize = self.cellSize

        clear_background(WHITE)
        begin_drawing()

        posY = 1
        for i in range(1, gridSize-1):
            posX = 1
            for j in range(1, gridSize-1):
                if grid[i][j] == 0:
                    draw_rectangle(posX, posY, cellSize-1, cellSize-1, BLACK)
                else:
                    draw_rectangle(posX, posY, cellSize-1, cellSize-1, WHITE)
                posX += cellSize
            posY += cellSize

        end_drawing()
