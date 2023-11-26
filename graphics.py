from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point1.x, self.point1.y,self.point2.x, self.point2.y, fill = fill_color, width = 2
        )
        canvas.pack()


class Window():
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title = 'Maze Solver'
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self._canvas = Canvas(
            self.__root,
            bg="white",
            width=width,
            height=height,
        )
        self._canvas.pack(fill=BOTH, expand=1)
        self._is_running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self._is_running = True
        while self._is_running:
            self.redraw()

    def close(self) -> None:
        self._is_running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self._canvas, fill_color)