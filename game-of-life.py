from pyray import *
from enum import Enum
from time import sleep

from raylib.defines import  MOUSE_LEFT_BUTTON
import grid as gr
import controller as ctrl

Screens = Enum('Screens', ['EDIT', 'RUN'])

def main():
    DELTA_T = 0.10
    CELL_SIZE = 24
    GRID_SIZE = 80

    SCREEN_WIDTH = (CELL_SIZE * GRID_SIZE) + 1
    SCREEN_HEIGHT = (CELL_SIZE * GRID_SIZE) + 1


    grid = gr.Grid([], 0) # This is a stub for now
    controller = ctrl.Controller(CELL_SIZE, GRID_SIZE)
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

                if is_key_pressed(32): # When space is pressed
                    grid = gr.Grid(controller.inputHandler(), CELL_SIZE)
                    currentScreen = Screens.RUN
            case Screens.RUN:
                grid.drawGrid()
                sleep(DELTA_T)
                grid.updateGrid()

    close_window()


if __name__ == '__main__':
    main()
