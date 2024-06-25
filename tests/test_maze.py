import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'main', 'python')))

from gui import Maze, Window

def main() -> None:
    win = Window(800, 600, title="Testing Cell")
    # Test Maze: init, create_cells, draw_cell, animate
    maze = Maze(50, 125, 22, 12, 30, 30, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()