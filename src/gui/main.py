from pyray import *
from enum import Enum

Screens = Enum('Screens', ['EDIT', 'RUN'])

def main():
    SCREEN_WIDTH = get_screen_width()
    SCREEN_HEIGHT = get_screen_height()

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Conway's Game of Life")
    set_target_fps(60)

    current_screen = Screens.EDIT

    while (not window_should_close()):
        match current_screen:
            case Screens.EDIT:
                pass
            case Screens.RUN:
                pass

    close_window()


if __name__ == '__main__':
    main()
