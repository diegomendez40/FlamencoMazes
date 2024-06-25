import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'main', 'python')))

from gui import Cell, Line, Point, Window

def main() -> None:
    win = Window(800, 600, title="Testing Cell")
    # Test Cell.draw
    point1 = Point(50, 125)
    point2 = Point(75, 150)
    point3 = Point(75, 125)
    point4 = Point(100, 150)
    cell1 = Cell(point1.x, point2.x, point1.y, point2.y, win, left_wall=False)
    cell1.draw()
    cell2 = Cell(point3.x, point4.x, point3.y, point4.y, win, right_wall=False, left_wall=False)
    cell2.draw()
    cell1.draw_move(cell2)
    win.wait_for_close()


if __name__ == "__main__":
    main()