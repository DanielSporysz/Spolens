import pyglet
from pyglet.gl import *
from cfreader import load_objects_configuration

lines = load_objects_configuration("lines.txt")

win = pyglet.window.Window(1024, 576)

def draw_line(start, end):
    glBegin(GL_LINES)
    glVertex3f(float(start[0]),float(start[1]),float(start[2]))
    glVertex3f(float(end[0]),float(end[1]),float(end[2]))
    glEnd()

@win.event
def on_draw():
    for line in lines:
        draw_line(line[0], line[1])

pyglet.app.run()