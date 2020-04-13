import pyglet
from setups import read_setup
from window import SpolensWindow


def main():
    lines = read_setup("./setups/s03.txt")
    window = SpolensWindow(600, 600, lines=lines, title="Spolens")
    pyglet.app.run()


if __name__ == "__main__":
    main()
