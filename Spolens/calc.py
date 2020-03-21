from structures import Point
from structures import Line


def cast_lines_on_screen(lines, width, height, distance_to_screen):
    screen_lines = []
    for line in lines:
        points = []
        for point in line.get_points():
            s_point = cast_point_on_screen(
                point, width, height, distance_to_screen)
            points.append(s_point)

        screen_lines.append(
            Line(points[0], points[1], line.color))

    return screen_lines


def cast_point_on_screen(point, width, height, distance_to_screen):
    x = point.x * distance_to_screen / point.z + width / 2
    y = point.y * distance_to_screen / point.z + height / 2
    return Point(x, y, 1)


def translate_lines(lines, x, y, z):
    new_lines = []
    for line in lines:
        points = []
        for point in line.get_points():
            new_point = Point(point.x + x, point.y+y, point.z+z)
            points.append(new_point)

        new_lines.append(
            Line(points[0], points[1], line.color))

    return new_lines
