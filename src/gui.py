from pyray import *
from enum import Enum
import grid as gr

Screens = Enum('Screens', ['EDIT', 'RUN'])
g = [[0, 1, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0]]


def main():
    SCREEN_WIDTH = get_screen_width()
    SCREEN_HEIGHT = get_screen_height()

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Conway's Game of Life")

    grid = gr.Grid(g)
    current_screen = Screens.RUN

    set_target_fps(60)

    while (not window_should_close()):
        match current_screen:
            case Screens.EDIT:
                pass
            case Screens.RUN:
                drawGrid(grid)

    close_window()


def drawGrid(gridObj):
    CELL_SIZE = 50
    grid = gridObj.getGrid()

    clear_background(BLACK)
    begin_drawing()

    posY = 0
    for row in grid:
        posX = 0
        for cell in row:
            if cell == 0:
                draw_rectangle(posX, posY, CELL_SIZE, CELL_SIZE, BLACK)
            else:
                draw_rectangle(posX, posY, CELL_SIZE, CELL_SIZE, WHITE)
            posX += CELL_SIZE
        posY += CELL_SIZE

    end_drawing()


if __name__ == '__main__':
    main()
