from cell import Cell
from graphics import Point, Window
import time
from typing import Optional, List
import random

class Maze():
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int, 
            win: Optional[Window] = None,
            seed: Optional[int] = None,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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
                self._draw_cell(x,y, 0.015)

    def _draw_cell(self, x: int, y: int, delay: float) -> None:
        # draws all the cells in an "animation" using a simple time delay between lines
        self._cells[x][y].draw()
        self._animate(delay)
    
    def _animate(self, delay: float) -> None:
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(delay)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()
        
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw()

    def _get_possible_directions(self, x: int, y: int) -> List[Point]:
        possible_directions: List[Point] = []
        # Left neighbor
        if x > 0 and not self._cells[x - 1][y].visited:
            possible_directions.append(Point(x - 1, y))
        # Right neighbor
        if x < self._num_cols - 1 and not self._cells[x + 1][y].visited:
            possible_directions.append(Point(x + 1, y))
        # Top neighbor
        if y > 0 and not self._cells[x][y - 1].visited:
            possible_directions.append(Point(x, y - 1))
        # Bottom neighbor
        if y < self._num_rows - 1 and not self._cells[x][y + 1].visited:
            possible_directions.append(Point(x, y + 1))
        return possible_directions

    def _break_walls_r(self, x: int, y: int) -> None:
        actual_cell = self._cells[x][y]
        actual_cell.visited = True
        while True:
            possible_directions = self._get_possible_directions(x, y)

            if not possible_directions:
                self._draw_cell(x, y, 0.03)
                return

            next_loc = random.choice(possible_directions)
            next_cell = self._cells[next_loc.x][next_loc.y]
            if next_loc.x < x:
                actual_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif next_loc.x > x:
                actual_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif next_loc.y < y:
                actual_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            else:
                actual_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            self._break_walls_r(next_loc.x, next_loc.y)

