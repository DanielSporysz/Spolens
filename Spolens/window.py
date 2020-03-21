import pyglet
from pyglet.gl import *
from pyglet.window import key
from structures import Point
from structures import Line
from calc import *


class SpolensWindow(pyglet.window.Window):
    def __init__(self, width, height, title, distance_to_screen, lines):
        self.distance_to_screen = distance_to_screen
        self.lines = lines
        super().__init__(width, height, title)

    def on_draw(self):
        self.clear()

        screen_lines = cast_lines_on_screen(
            self.lines, self.width, self.height, self.distance_to_screen)
        for line in screen_lines:
            self.draw_line(line.start, line.end, line.color)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.lines = translate_lines(self.lines, -100, 0, 0)
            self.on_draw()
        elif symbol == key.D:
            self.lines = translate_lines(self.lines, 100, 0, 0)
        elif symbol == key.W:
            self.lines = translate_lines(self.lines, 0, 100, 0)
        elif symbol == key.S:
            self.lines = translate_lines(self.lines, 0, -100, 0)

    def draw_line(self, start: Point, end: Point, color: list):
        glBegin(GL_LINES)
        glColor4f(color[0], color[1], color[2], color[3])
        glVertex3f(start.x, start.y, start.z)
        glVertex3f(end.x, end.y, end.z)
        glEnd()
