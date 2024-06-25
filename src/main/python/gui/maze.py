import random
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
            win: Window = None,
            seed: int = None
        ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)               # Intended for test reproducibility purposes only
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)


    def _animate(self) -> None:
        self._win.redraw()
        time.sleep(0.05)


    def _break_entrance_and_exit(self) -> None:
            self._cells[0][0].has_left_wall = False
            self._cells[self.num_rows - 1][self.num_cols - 1].has_right_wall = False
            self._draw_cell(0, 0)
            self._draw_cell(self.num_rows - 1, self.num_cols - 1)


    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True
        i_max = self.num_rows - 1
        j_max = self.num_cols - 1
        while True:
            to_visit = []
            for aux in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                if ( 0 <= i + aux[0] <= i_max) and (0 <= j + aux[1] <= j_max):
                    if self._cells[i + aux[0]][j + aux[1]].visited == False:
                        to_visit.append(aux)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            next_move = random.choice(to_visit)
            match next_move:
                case (-1, 0):   # LEFT
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                case (1, 0):   # RIGHT
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                case (0, 1):   # DOWN
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                case (0, -1):   # UP
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
            next_cell = (i + next_move[0], j + next_move[1])
            self._break_walls_r(*next_cell)


    def _create_cells(self) -> None:
        self._cells = []
        for row in range(self.num_rows):
            cell_row = []
            for col in range(self.num_cols):
                x1 = self._x1 + col * self.cell_size_x
                y1 = self._y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(
                    x1,
                    x2,
                    y1,
                    y2,
                    self._win
                    )
                cell_row.append(cell)
            self._cells.append(cell_row)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col)


    def _draw_cell(self, i: int, j: int) -> None:
        if self._win is not None:
            self._cells[i][j].draw()
            self._animate()


    def _reset_cells_visited(self) -> None:
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._cells[row][col].visited = False


    def solve(self) -> bool:
        return self._solve_r(0, 0)


    def _solve_r(self, i: int, j: int) -> bool:
        self._animate()
        self._cells[i][j].visited = True
        i_max = self.num_rows - 1
        j_max = self.num_cols - 1
        if i == i_max and j == j_max:
            # This is the exit cell
            return True
        for direction in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            feasible_move = False
            if ( 0 <= i + direction[0] <= i_max) and (0 <= j + direction[1] <= j_max):
                if ( self._cells[i + direction[0]][j + direction[1]].visited == False ):
                    # TODO: Finish this algorithm as per https://www.boot.dev/lessons/cd9b1811-98ca-496f-a391-86e102cdcf80
                    match direction:
                        case (-1, 0):   # LEFT
                            if self._cells[i][j].has_left_wall == False and self._cells[i-1][j].has_right_wall == False:
                                feasible_move = True
                        case (1, 0):   # RIGHT
                            if self._cells[i][j].has_right_wall == False and self._cells[i+1][j].has_left_wall == False:
                                feasible_move = True
                        case (0, 1):   # DOWN
                            if self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].has_top_wall == False:
                                feasible_move = True
                        case (0, -1):   # UP
                            if self._cells[i][j].has_top_wall == False and self._cells[i][j-1].has_bottom_wall == False:
                                feasible_move = True
                    if feasible_move:
                        next_cell = (i + direction[0], j + direction[1])
                        self._cells[i][j]._draw_move(self._cells[next_cell[0]][next_cell[1]])
                        if self._solve_r(*next_cell):
                            return True
                        else:
                            self._cells[i][j]._draw_move(self._cells[next_cell[0]][next_cell[1]], undo=True)
        return False
