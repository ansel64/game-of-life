import logging
import time
import grid as gr
import error

logging.basicConfig(level=logging.INFO)

def main():
    grid = gr.Grid(parseForGrid('grid.txt'))

    delta_t = 1 # How many seconds per tick

    while True:
        grid.drawGrid()
        grid.updateGrid()
        time.sleep(delta_t)


def parseForGrid(filename: str) -> list: # TODO: make a proper grid parser for gui.
    '''Parses grid file and turn it into a 2d list. For now, assume that file format is correct.
    !!! THIS FUNCTION IS A STUB !!!'''

    logging.info("Prasing and generating grid...")

    file = open(filename)
    lines = file.readlines()
    grid = []

    for line in lines:
        grid.append(line.split())
    return grid


if __name__ == '__main__':
    main()
