from structures import Point
from structures import Line
import numpy as np
import math

TOLERANCE = 1e-5


def cast_lines_on_screen(lines, width, height, distance_to_screen, clipping_distance):
    # clipping plane
    plane_point1 = Point(20, 2, clipping_distance)
    plane_point2 = Point(1, 1, clipping_distance)
    plane_point3 = Point(2, 30, clipping_distance)
    plane_points = [plane_point1, plane_point2, plane_point3]

    screen_lines = []
    for line in lines:
        line_to_draw = line
        # skip lines that are behind the clipping distance
        if (line.start.z <= clipping_distance and line.end.z <= clipping_distance):
            continue
        # clip lines that go through the screen if needed
        line_to_draw = clip_line(line, plane_points)

        points = []
        for point in line_to_draw.get_points():
            s_point = cast_point_on_screen(
                point, width, height, distance_to_screen)
            points.append(s_point)

        screen_lines.append(
            Line(points[0], points[1], line.color))

    return screen_lines


def cast_point_on_screen(point, width, height, distance_to_screen):
    try:
        x = point.x * distance_to_screen / point.z + width / 2
        y = point.y * distance_to_screen / point.z + height / 2
        return Point(x, y, 1)
    except Exception as e:
        print(e, flush=True)
        return Point(width/2, height/2, 1)


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


def rotate_lines(lines, angle, axis):
    angle = angle*math.pi/180
    rotation_matrix = get_rotation_matrix(angle, axis)

    new_lines = []
    for line in lines:
        points = []
        for point in line.get_points():
            new_point = np.dot(rotation_matrix, [point.x, point.y, point.z, 1])
            new_point = Point(new_point[0], new_point[1], new_point[2])
            points.append(new_point)

        new_lines.append(
            Line(points[0], points[1], line.color))

    return new_lines


def get_rotation_matrix(angle, axis):
    if(axis == "x"):
        return np.array([
            [1, 0, 0, 0],
            [0, math.cos(angle), -math.sin(angle), 0],
            [0, math.sin(angle), math.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    elif(axis == "y"):
        return np.array([
            [math.cos(angle), 0, math.sin(angle), 0],
            [0, 1, 0, 0],
            [-math.sin(angle), 0, math.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    elif(axis == "z"):
        return np.array([
            [math.cos(angle), -math.sin(angle), 0, 0],
            [math.sin(angle), math.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    else:
        raise Exception("Unknown axis: " + axis)


def clip_line(line: Line, plane_points: list):
    # check if the line has clipping point
    clipping_z = plane_points[0].z
    if (line.start.z < clipping_z and line.end.z < clipping_z
            or line.start.z > clipping_z and line.end.z > clipping_z):
        return line

    p0 = np.array([plane_points[0].x, plane_points[0].y, plane_points[0].z])
    p1 = np.array([plane_points[1].x, plane_points[1].y, plane_points[1].z])
    p2 = np.array([plane_points[2].x, plane_points[2].y, plane_points[2].z])

    p01 = p1 - p0
    p02 = p2 - p0

    la = np.array([line.start.x, line.start.y, line.start.z])
    lb = np.array([line.end.x, line.end.y, line.end.z])
    lab = lb - la

    # evaluate the point that is still visible
    if line.start.z < p0[2] or np.isclose(line.start.z, p0[2]):
        visible_point = line.end
    else:
        visible_point = line.start

    # calculate clipping point
    t = (p01.dot(p02) * (la - p0)) / (-lab * p01.dot(p02))
    clipping_point = la + lab.dot(t[2])
    clipping_point = Point(
        clipping_point[0], clipping_point[1], clipping_point[2])

    return Line(clipping_point, visible_point, line.color)


def get_plane_parameters(p1: Point, p2: Point, p3: Point):  # currently unused
    # args check
    D = np.array([
        [p1.x, p1.y, p1.z],
        [p2.x, p2.y, p2.z],
        [p3.x, p3.y, p3.z]
    ])
    D = np.linalg.det(D)
    if(D == 0):
        raise Exception("Cannot determine a plane with given points!")

    d = 5
    ceo = - d / D

    a = ceo * np.linalg.det(np.array([
        [1, p1.y, p1.z],
        [1, p2.y, p2.z],
        [1, p3.y, p3.z]
    ]))

    b = ceo * np.linalg.det(np.array([
        [p1.x, 1, p1.z],
        [p2.x, 1, p2.z],
        [p3.x, 1, p3.z]
    ]))

    c = ceo * np.linalg.det(np.array([
        [p1.x, p1.y, 1],
        [p2.x, p2.y, 1],
        [p3.x, p3.y, 1]
    ]))

    return [a, b, c, d]
