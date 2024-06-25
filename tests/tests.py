import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'main', 'python')))

from gui import Maze, Window
import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
            "El número de filas no coincide con el esperado"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
            "El número de columnas no coincide con el esperado"
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 14
        num_rows = 18
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
            "El número de filas no coincide con el esperado"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
            "El número de columnas no coincide con el esperado"
        )
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_left_wall and m1._cells[0][0].has_top_wall,
            False,
            "La entrada del laberinto no se ha creado correctamente" 
        )
        self.assertEqual(
            m1._cells[num_rows - 1][num_cols - 1].has_right_wall and m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
            "La salida del laberinto no se ha creado correctamente" 
        )
        

if __name__ == "__main__":
    unittest.main()