from graphics import *
from typing import Optional

class Cell():
    def __init__(self, top_left: Point, bottom_right: Point, win: Optional[Window] = None):
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
            "black" if self.has_left_wall else "white"
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
            "black" if self.has_top_wall else "white"
        )

        # draw bottom wall
        self._win.draw_line(
            Line(
                Point(self._x1, self._y2),
                Point(self._x2, self._y2)
            ),
            "black" if self.has_bottom_wall else "white"
        )

    # draw the maze-solving line from center of cell to center of the next cell
    def draw_move(self, to_cell, undo: bool = False) -> None:
        if self._win is None:
            return
        self._win.draw_line(
            Line(
                Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2), # 50, 50   100, 50 -> 75,75
                Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2) # 100, 100  150, 100 -> 125,75
            ),
            "gray" if undo else "red"
        )
