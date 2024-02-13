from pyray import *
from enum import Enum
from time import sleep
import grid as gr
import controller as ctrl

Screens = Enum('Screens', ['EDIT', 'RUN'])

def main():
    SCREEN_WIDTH = 961
    SCREEN_HEIGHT = 961
    DELTA_T = 0.75
    CELL_SIZE = 24

    controller = ctrl.Controller(CELL_SIZE, 42)
    currentScreen = Screens.EDIT

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Conway's Game of Life")

    set_target_fps(60)

    while (not window_should_close()):
        match currentScreen:
            case Screens.EDIT:
                controller.drawController()
            case Screens.RUN:
                pass

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
