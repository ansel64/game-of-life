from pyray import *
from enum import Enum
from time import sleep

from raylib.defines import KEY_ENTER, MOUSE_LEFT_BUTTON
import grid as gr
import controller as ctrl

Screens = Enum('Screens', ['EDIT', 'RUN'])

def main():
    SCREEN_WIDTH = 961
    SCREEN_HEIGHT = 961
    DELTA_T = 0.75
    CELL_SIZE = 24

    grid = gr.Grid([], 0) # This is a stub for now
    controller = ctrl.Controller(CELL_SIZE, 42)
    currentScreen = Screens.EDIT

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Conway's Game of Life")

    set_target_fps(60)

    while (not window_should_close()):
        match currentScreen:
            case Screens.EDIT:
                controller.drawController()

                if is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
                    x = get_mouse_x()
                    y = get_mouse_y()

                    controller.clickHandler(x, y)

                if is_key_pressed(KEY_ENTER):
                    grid = gr.Grid(controller.inputHandler(), CELL_SIZE)
            case Screens.RUN:
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
