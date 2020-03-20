import pyglet
from pyglet.gl import *
from cfgreader import load_objects_configuration
import numpy as np

lines = load_objects_configuration("lines.txt")

win = pyglet.window.Window(600, 600)


def draw_line(start, end):
    glBegin(GL_LINES)
    glVertex3f(start[0], start[1], 1)
    glVertex3f(end[0], end[1], 1)
    glEnd()


def cast_on_screen(lines):
    lines_on_screen = []

    for line in lines:
        line_points_on_screen = []
        for point in line:
            # coefficient = 2/point[2]
            cast_matrix = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1/point[2], 0]
            ])
            point.append(1)
            new_point = cast_matrix.dot(point)
            line_points_on_screen.append(new_point)

        lines_on_screen.append(
            [line_points_on_screen[0], line_points_on_screen[1]])

    return lines_on_screen


@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)

    lines_on_screen = cast_on_screen(lines)
    for line in lines_on_screen:
        draw_line(line[0], line[1])


pyglet.app.run()
