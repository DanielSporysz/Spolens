class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.y) + ")"


class Line:
    def __init__(self, start: Point, end: Point, color: list):
        self.start = start
        self.end = end
        self.color = color

    def get_points(self):
        return [self.start, self.end]

    def __str__(self):
        return "{" + str(self.start) + "->" + str(self.end) + "}"
