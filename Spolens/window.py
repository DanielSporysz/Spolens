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

        self.step = 10
        self.slow_step = 2
        self.r_step = 1
        self.d_step = 10

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
            'ZX - rOZ', x=0, y=height-7*self.font_size)

        super().__init__(width, height, title)

    def on_draw(self):
        self.clear()

        screen_lines = cast_lines_on_screen(
            self.lines, self.width, self.height, self.distance_to_screen)
        for line in screen_lines:
            self.draw_line(line.start, line.end, line.color)

        # display controls help
        self.controls_labelAD.draw()
        self.controls_labelWS.draw()
        self.controls_labelQE.draw()
        self.controls_labelTG.draw()
        self.controls_labelFH.draw()
        self.controls_labelRY.draw()
        self.controls_labelZoom.draw()

        # display parameters
        pyglet.text.Label(
            'd = ' + str(self.distance_to_screen), x=0, y=0).draw()

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

        self.on_draw()

    def draw_line(self, start: Point, end: Point, color: list):
        glBegin(GL_LINES)
        glColor4f(color[0], color[1], color[2], color[3])
        glVertex3f(start.x, start.y, start.z)
        glVertex3f(end.x, end.y, end.z)
        glEnd()
