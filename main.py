from graphics import Window, Point
from cell import Cell

def main():
    # window
    win = Window(800, 600)

    # draw some cells
    cell1 = Cell(Point(50,50), Point(100,100), win)
    # cell1.has_right_wall = False
    cell1.draw()
    cell2 = Cell(Point(50,100), Point(100,150), win)
    # cell2.has_left_wall = False
    cell2.draw()
    cell3 = Cell(Point(100,100), Point(150,150), win)
    # cell2.has_left_wall = False
    cell3.draw()

    # draw move from cell1 to cell2
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)


    # run/mainloop
    win.wait_for_close()

main()