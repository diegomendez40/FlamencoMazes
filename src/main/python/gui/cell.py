from .line import Line
from .point import Point
from .window import Window

class Cell:

    def __init__(
            self,
            x1: int,
            x2: int,
            y1: int,
            y2: int,
            win: Window,
            left_wall: bool = True,
            right_wall: bool = True,
            top_wall: bool = True,
            bottom_wall: bool = True
            ):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self) -> None:
        if self.has_left_wall:
            pointUL = Point(self._x1, self._y1)
            pointLL = Point(self._x1, self._y2)
            line = Line(pointUL, pointLL)
            self._win.draw_line(line)

        if self.has_left_wall:
            pointUL = Point(self._x1, self._y1)
            pointLL = Point(self._x1, self._y2)
            line = Line(pointUL, pointLL)
            self._win.draw_line(line)

        if self.has_left_wall:
            pointUL = Point(self._x1, self._y1)
            pointLL = Point(self._x1, self._y2)
            line = Line(pointUL, pointLL)
            self._win.draw_line(line)

        if self.has_left_wall:
            pointUL = Point(self._x1, self._y1)
            pointLL = Point(self._x1, self._y2)
            line = Line(pointUL, pointLL)
            self._win.draw_line(line)

        
    