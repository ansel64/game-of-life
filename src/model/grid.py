import copy

class Grid(object):
    def __init__(self, size: int) -> None:
        '''Create two empty grids, one for storing previous grid and another for updated version.'''
        self.grid = []

        for i in range(size):
            self.grid.append(list())
            for _ in range (size):
                self.grid[i].append(0)

        self.storage = copy.deepcopy(self.grid)


    def updateGrid(self) -> None:
        grid = self.grid
        storage = self.storage

        for i in range(len(storage)):
            for j in range(len(storage)):
                isBorder = (i == 0 or i == (len(grid)-1)) or (j == 0 or j == (len(grid)))

                if isBorder:
                    grid[i][j] = 0
                else:
                    totalNeighbors = Grid.countNeighbors(self, i, j)
                    cell = storage[i][j]

                    if cell == 0 and totalNeighbors == 3:
                        grid[i][j] = 1
                    elif cell == 1 and (totalNeighbors < 2 or totalNeighbors > 3):
                        grid[i][j] = 0
                    elif cell == 1 and (totalNeighbors == 2 or totalNeighbors == 2):
                        grid[i][j] = 1


    def countNeighbors(self, i: int, j: int) -> int:
        grid = self.grid
        return (grid[i][j-1] + grid[i][j+1]) + (grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]) + (grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1])


    def getGrid(self) -> list:
        return self.grid
    

    def getStorage(self) -> list:
        return self.storage

