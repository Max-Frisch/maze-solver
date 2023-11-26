from graphics import Window, Point
from cell import Cell

def main():
    # window
    win = Window(800, 600)

    # draw some cells
    cell = Cell(Point(50,50), Point(100,100), win)
    cell.draw()
    cell = Cell(Point(125,125), Point(200,200), win)
    cell.draw()
    cell = Cell(Point(300,300), Point(500,500), win)
    cell.draw()

    # run/mainloop
    win.wait_for_close()

main()