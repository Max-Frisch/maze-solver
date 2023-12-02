from graphics import Window, Point
from cell import Cell
from maze import Maze

def main():
    # window
    win = Window(800, 600)

    # create a maze
    maze = Maze(10, 10, 16, 22, 35, 35, win)

 
    # run/mainloop
    win.wait_for_close()

main()