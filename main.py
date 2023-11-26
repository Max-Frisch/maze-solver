from graphics import Window, Point, Line

def main():
    # window
    win = Window(800, 600)

    # draw some lines
    point1 = Point(5, 5)
    point2 = Point(20, 20)
    line = Line(point1, point2)
    win.draw_line(line, 'blue')

    # run/mainloop
    win.wait_for_close()

main()