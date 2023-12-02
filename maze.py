from cell import Cell
from graphics import Point, Window
from time import time as t

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
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__window = win

        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = []
    
    def _draw_cells(self, i: int, j: int) -> None:
        pass
        # draw

        # animate
        self._animate()
    
    def _animate(self) -> None:
        self.__window.redraw()
        t.sleep(0.05)