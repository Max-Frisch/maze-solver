from cell import Cell
from graphics import Point, Window
import time

class Maze():
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int, 
            win,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = win

        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = []
        for x in range(self._num_cols):
            column = []
            for y in range(self._num_rows):
                cell_top_left = Point(
                    x=self._x1 + x * self._cell_size_x,
                    y=self._y1 + y * self._cell_size_y,
                )
                cell_bottom_right = Point(
                    x=cell_top_left.x + self._cell_size_x,
                    y=cell_top_left.y + self._cell_size_y,
                )
                cell = Cell(cell_top_left, cell_bottom_right, self._window)
                column.append(cell)
            self._cells.append(column)
    
        for x in range(self._num_cols):
            for y in range(self._num_rows):
                self._draw_cell(x,y)

    def _draw_cell(self, x: int, y: int) -> None:
        # draws all the cells in an "animation" using a simple time delay between lines
        self._cells[x][y].draw()
        self._animate()
    
    def _animate(self) -> None:
        self._window.redraw()
        time.sleep(0.015)