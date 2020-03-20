import pyglet
from pyglet.gl import *
from cfgreader import load_objects_configuration
from setups import read_setup
import numpy as np
import math
from structures import Point
from structures import Line

WIDTH = 800
HEIGHT = 800

SCREEN_DISTANCE = 100

lines = read_setup("./setups/s01.txt")

win = pyglet.window.Window(WIDTH, HEIGHT)


def draw_line(start: Point, end: Point, color: list):
    glBegin(GL_LINES)
    glColor4f(color[0], color[1], color[2], color[3])
    glVertex3f(start.x, start.y, start.z)
    glVertex3f(end.x, end.y, end.z)
    glEnd()


def cast_on_screen(lines):
    screen_lines = []

    for line in lines:
        screen_points = []
        for point in line.get_points():
            x = point.x * SCREEN_DISTANCE / point.z + WIDTH/2
            y = point.y * SCREEN_DISTANCE / point.z + HEIGHT/2
            screen_points.append(Point(x, y, 1))
        screen_lines.append(Line(screen_points[0], screen_points[1], line.color))

    return screen_lines


@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)

    screen_lines=cast_on_screen(lines)
    for line in screen_lines:
        draw_line(line.start, line.end, line.color)


def main():
    pyglet.app.run()


if __name__ == "__main__":
    main()
