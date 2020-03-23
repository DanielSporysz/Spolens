import pyglet
from setups import read_setup
from window import SpolensWindow


def main():
    lines = read_setup("./setups/s03.txt")
    window = SpolensWindow(600, 600, distance_to_screen=200,
                           lines=lines, title="Spolens")
    pyglet.app.run()


if __name__ == "__main__":
    main()
