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
            win: Window = None,
            left_wall: bool = True,
            right_wall: bool = True,
            top_wall: bool = True,
            bottom_wall: bool = True
            ):
        # x1,y1 -> top-left corner
        # x2,y2 -> bottom-right
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x1     
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = False


    def draw(self) -> None:

        # Left wall
        pointUL = Point(self._x1, self._y1)
        pointLL = Point(self._x1, self._y2)
        line = Line(pointUL, pointLL)
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, 'white')

        # Right wall
        pointUR = Point(self._x2, self._y1)
        pointLR = Point(self._x2, self._y2)
        line = Line(pointUR, pointLR)
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, 'white')

        # Top wall
        pointUL = Point(self._x1, self._y1)
        pointUR = Point(self._x2, self._y1)
        line = Line(pointUL, pointUR)
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, 'white')

        # Bottom wall
        pointLL = Point(self._x1, self._y2)
        pointLR = Point(self._x2, self._y2)
        line = Line(pointLL, pointLR)
        if self.has_bottom_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, 'white')

    def draw_move(
            self,
            to_cell: 'Cell',
            undo: bool = False
            ) -> None:
        center1 = self.get_cell_center()
        center2 = to_cell.get_cell_center()
        line = Line(center1, center2)
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._win.draw_line(line, fill_color)

    def get_cell_center(self) -> Point:
        x = (self._x1 + self._x2) // 2
        y = (self._y1 + self._y2) // 2
        return Point(x, y)
        
    