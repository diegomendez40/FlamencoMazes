import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'main', 'python')))

from gui import Line, Point, Window

def main() -> None:
    win = Window(800, 600, title="Testing Window")
    # Test draw_line
    point1 = Point(50, 50)
    point2 = Point(60, 95)
    point3 = Point(450, 400)
    point4 = Point(550, 50)
    line1 = Line(point1, point2)
    win.draw_line(line1, 'black')
    line2 = Line(point2, point3)
    win.draw_line(line2, 'red')
    line3 = Line(point3, point4)
    win.draw_line(line3, 'blue')
    win.wait_for_close()


if __name__ == "__main__":
    main()