import pyglet
from pyglet.gl import *
from pyglet.window import key
from structures import Point
from structures import Line
from calc import *


class SpolensWindow(pyglet.window.Window):
    def __init__(self, width, height, title, lines):
        self.lines = lines

        self.distance_to_screen = 200
        self.clipping_distance = 1

        self.step = 2
        self.slow_step = 2
        self.r_step = 1
        self.d_step = 10
        self.clipping_step = 1

        self.font_size = 20
        self.controls_labelWS = pyglet.text.Label(
            'WS - OY', x=0, y=height-self.font_size)
        self.controls_labelAD = pyglet.text.Label(
            'AD - OX', x=0, y=height-2*self.font_size)
        self.controls_labelQE = pyglet.text.Label(
            'QE - OZ', x=0, y=height-3*self.font_size)
        self.controls_labelTG = pyglet.text.Label(
            'FH - rOY', x=0, y=height-4*self.font_size)
        self.controls_labelFH = pyglet.text.Label(
            'TG - rOX', x=0, y=height-5*self.font_size)
        self.controls_labelRY = pyglet.text.Label(
            'RY - rOZ', x=0, y=height-6*self.font_size)
        self.controls_labelZoom = pyglet.text.Label(
            'ZX - Zoom', x=0, y=height-7*self.font_size)
        self.controls_labelClipping = pyglet.text.Label(
            'CV - Clipping', x=0, y=height-8*self.font_size)

        super().__init__(width, height, title)

    def on_draw(self):
        self.clear()

        # draw lines
        screen_lines = cast_lines_on_screen(
            self.lines, self.width, self.height, self.distance_to_screen, self.clipping_distance)
        for line in screen_lines:
            self.draw_line(line.start, line.end, line.color)

        # draw planes
        plane = [Point(100, 100, 1), Point(200, 100, 1), Point(200, 200, 1), Point(150, 190, 1)]
        self.draw_plane(plane, [1, 1, 1, 1])

        # display controls help
        self.controls_labelAD.draw()
        self.controls_labelWS.draw()
        self.controls_labelQE.draw()
        self.controls_labelTG.draw()
        self.controls_labelFH.draw()
        self.controls_labelRY.draw()
        self.controls_labelZoom.draw()
        self.controls_labelClipping.draw()

        # display parameters
        pyglet.text.Label(
            'clipping distance = ' + str(self.clipping_distance), x=0, y=0).draw()
        pyglet.text.Label(
            'zoom = ' + str(self.distance_to_screen), x=0, y=self.font_size).draw()

    def on_text(self, text):
        # OX
        if text == 'a':
            self.lines = translate_lines(self.lines, -self.step, 0, 0)
        elif text == 'd':
            self.lines = translate_lines(self.lines, self.step, 0, 0)
        # OY
        elif text == 'w':
            self.lines = translate_lines(self.lines, 0, self.step, 0)
        elif text == 's':
            self.lines = translate_lines(self.lines, 0, -self.step, 0)
        # OZ
        elif text == 'q':
            self.lines = translate_lines(self.lines, 0, 0, self.slow_step)
        elif text == 'e':
            self.lines = translate_lines(self.lines, 0, 0, -self.slow_step)
        # rOX
        elif text == 't':
            self.lines = rotate_lines(self.lines, -self.r_step, "x")
        elif text == 'g':
            self.lines = rotate_lines(self.lines, self.r_step, "x")
        # rOY
        elif text == 'f':
            self.lines = rotate_lines(self.lines, -self.r_step, "y")
        elif text == 'h':
            self.lines = rotate_lines(self.lines, self.r_step, "y")
        # rOY
        elif text == 'r':
            self.lines = rotate_lines(self.lines, self.r_step, "z")
        elif text == 'y':
            self.lines = rotate_lines(self.lines, -self.r_step, "z")
        # zoom
        elif text == 'z':
            self.distance_to_screen -= self.d_step
            if self.distance_to_screen < 10:
                self.distance_to_screen = 10
        elif text == 'x':
            self.distance_to_screen += self.d_step
        # clipping distance
        elif text == 'c':
            self.clipping_distance -= self.clipping_step
            if self.clipping_distance < 1:
                self.clipping_distance = 1
        elif text == 'v':
            self.clipping_distance += self.clipping_step

        self.on_draw()

    def draw_line(self, start: Point, end: Point, color: list):
        glBegin(GL_LINES)
        glColor4f(color[0], color[1], color[2], color[3])
        glVertex3f(start.x, start.y, start.z)
        glVertex3f(end.x, end.y, end.z)
        glEnd()

    def draw_plane(self, plane_points, color: list):
        glBegin(GL_POLYGON)
        glColor4f(color[0], color[1], color[2], color[3])
        for point in plane_points:
            glVertex3f(point.x, point.y, point.z)
        glEnd()
