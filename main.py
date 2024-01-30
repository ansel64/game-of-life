import time
import grid

def main():
    # Take and validate input file (create grid object)
    #
    # For every tick second:
    # . Draw the grid
    # . Update the grid

    delta_t = 1 # How many seconds per tick
    fhand = open(grid.txt)
    grid = grid.Grid(parseInput(fhand))
    
    while True:
        grid.drawGrid()
        grid.updateGrid()
        time.sleep(delta_t)

def parseInput(file) -> list:
    return []

if __name__ == '__main__':
    main()