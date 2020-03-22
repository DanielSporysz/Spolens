from structures import Point
from structures import Line
import numpy as np
import math


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
    try:
        x = point.x * distance_to_screen / point.z + width / 2
        y = point.y * distance_to_screen / point.z + height / 2
        return Point(x, y, 1)
    except:
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
