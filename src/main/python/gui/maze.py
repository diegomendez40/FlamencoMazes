import time
from .cell import Cell
from .window import Window

class Maze:

    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Window,
        ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = []
        for row in range(self.num_rows):
            cell_row = []
            for col in range(self.num_cols):
                cell = Cell(
                    self._x1,
                    self._x1 + self.cell_size_x,
                    self._y1,
                    self._y1 + self.cell_size_y,
                    self._win
                    )
                cell_row.append(cell)
            self._cells.extend(cell_row)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col)

    def _draw_cell(self, i: int, j: int) -> None:
        x1 = self._x1 + i * self.cell_size_x
        y1 = self._y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = Cell(x1, x2, y1, y2, self._win)
        cell.draw()
        self._animate()

    def _animate(self) -> None:
        self._win.redraw()
        time.sleep(0.05)
