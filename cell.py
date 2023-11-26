from graphics import *

class Cell():
    def __init__(self, top_left: Point, bottom_right: Point, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self._win = win

    def draw(self) -> None:
        if self._win is None:
            return
        
        # draw left wall
        self._win.draw_line(
            Line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2)
            ),
            "black" if self.has_right_wall else "white"
        )

        # draw right wall
        self._win.draw_line(
            Line(
                Point(self._x2, self._y1),
                Point(self._x2, self._y2)
            ),
            "black" if self.has_right_wall else "white"
        )

        # draw top wall
        self._win.draw_line(
            Line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1)
            ),
            "black" if self.has_right_wall else "white"
        )

        # draw bottom wall
        self._win.draw_line(
            Line(
                Point(self._x1, self._y2),
                Point(self._x2, self._y2)
            ),
            "black" if self.has_right_wall else "white"
        )