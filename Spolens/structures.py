class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


class Line:
    def __init__(self, start: Point, end: Point, color: list):
        self.start = start
        self.end = end
        self.color = color

    def get_points(self):
        return [self.start, self.end]

    def __str__(self):
        return "{" + str(self.start) + "->" + str(self.end) + " of color " + str(self.color) + "}"

class Plane:
    def __init__(self, points: list, color: list):
        if len(points) < 3:
            raise Exception("Given points do not make a plane!")

        self.points = points
        self.color = color

    def getFarZ(self):
        if len(self.points < 3):
            raise Exception("Illegal state. Plane has too few points!")

        furthest = self.points[0].z
        for point in self.points:
            if furthest < point.z:
                furthest = point.z
        return furthest

    def __lt__(self, other):
         return self.getFarZ() < other.getFarZ()

    def __str__(self):
        return "{" + str([str(i) for i in self.points]) + " of color " + str(self.color) + "}"