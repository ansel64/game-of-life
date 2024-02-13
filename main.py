from pyray import *
from enum import Enum
from time import sleep
import grid as gr

def main():
    SCREEN_WIDTH = 961
    SCREEN_HEIGHT = 961
    DELTA_T = 0.75

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Conway's Game of Life")

    grid = gr.Grid(parseGrid('grid.txt'))

    set_target_fps(60)

    while (not window_should_close()):
                grid.drawGrid()
                sleep(DELTA_T)
                grid.updateGrid()

    close_window()


def parseGrid(fileName):
    file = open(fileName)
    lines = file.readlines()
    grid = []

    for i in range(len(lines)):
        grid.append([])
        line = lines[i].split(' ')
        for cell in line:
            grid[i].append(int(cell))
    return grid

if __name__ == '__main__':
    main()
