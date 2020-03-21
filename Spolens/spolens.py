import pyglet
from setups import read_setup
from window import SpolensWindow


def main():
    lines = read_setup("./setups/s01.txt")
    window = SpolensWindow(600, 600, distance_to_screen=100,
                           lines=lines, title="Spolens")
    pyglet.app.run()


if __name__ == "__main__":
    main()
