from tkinter import Tk, BOTH, Canvas
from .point import Point
from .line import Line

class Window:

    def __init__(self, width: int, height: int, title: str="") -> None:
        """
        Initialize the window.

        Args:
            width (int): The width of the window in pixels.
            height (int): The height of the window in pixels.
            title (str, optional): The title of the window. Defaults to an empty string.
        """
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.__root)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False 
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()


    def close(self) -> None:
        self.running = False


    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)


    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()


def main() -> None:
    win = Window(800, 600)
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