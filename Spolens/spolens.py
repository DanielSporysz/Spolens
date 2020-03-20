import pyglet
from pyglet.gl import *
from cfgreader import load_objects_configuration
import numpy as np
import math

lines = load_objects_configuration("lines.txt")

width = 600
height = 600
win = pyglet.window.Window(width, height)


def draw_line(start, end):
    glBegin(GL_LINES)
    glVertex3f(start[0], start[1], 1)
    glVertex3f(end[0], end[1], 1)
    glEnd()


def cast_on_screen(lines):
    lines_on_screen = []

    angle = 90
    aspectRatio = width / height
    fov = 1.0 / math.tan(angle/2.0)
    far = 5000
    near = 1

    # [fov * aspectRatio][        0        ][        0              ][        0       ]
    # [        0        ][       fov       ][        0              ][        0       ]
    # [        0        ][        0        ][(far+near)/(far-near)  ][        1       ]
    # [        0        ][        0        ][(2*near*far)/(near-far)][        0       ]

    for line in lines:
        line_points_on_screen = []
        for point in line:
            # coefficient = 2/point[2]
            cast_matrix = np.array([
                [fov*aspectRatio, 0, 0, 0],
                [0, fov, 0, 0],
                [0, 0, (far+near)/(far-near), 1],
                [0, 0, (2*near*far)/(near-far), 0]
            ])

            point.append(1)
            clipped_point = cast_matrix.dot(point)

            # new_x = (x * Width ) / (2.0 * w) + halfWidth;
            # new_y = (y * Height) / (2.0 * w) + halfHeight;
            x = clipped_point[0] * width / (2 * clipped_point[2]) + width/2
            y = clipped_point[1] * width / (2 * clipped_point[2]) + height/2

            line_points_on_screen.append([x, y])

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
