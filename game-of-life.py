# This app uses the Ryalib libraries for GUI: https://www.raylib.com
from pyray import *
from enum import Enum
from time import sleep

from raylib.defines import  MOUSE_LEFT_BUTTON
import grid as gr
import controller as ctrl

Screens = Enum('Screens', ['EDIT', 'RUN']) # The state of the screen tells what to listen for inputs and output to the user.

def main():
    DELTA_T = 0.3 # Seconds to wait between each iteration of cells
    CELL_SIZE = 24
    GRID_SIZE = 50

    SCREEN_WIDTH = (CELL_SIZE * GRID_SIZE) + 1
    SCREEN_HEIGHT = (CELL_SIZE * GRID_SIZE) + 1


    grid = gr.Grid([], 0) # This is a replacement for now
    controller = ctrl.Controller(CELL_SIZE, GRID_SIZE)
    currentScreen = Screens.EDIT

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Conway's Game of Life")

    set_target_fps(144)

    '''This is the main loop that dictates the program's behavior based on its current screen.'''
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
                wait_time(DELTA_T)
                gr.Grid.updateGrid(grid)

    close_window()


if __name__ == '__main__':
    main()
