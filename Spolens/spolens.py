import pyglet
from setups import read_setup
from window import SpolensWindow


def main():
    lines, planes = read_setup("./setups/s03.txt")
    # print(str(planes[0]))
    # print(str(lines[0]))
    SpolensWindow(600, 600, title="Spolens", lines=lines, planes=planes)
    pyglet.app.run()


if __name__ == "__main__":
    main()
