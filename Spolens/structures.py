class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Line:
    def __init__(self, start, end, color):
        self.start = start
        self.end = end
        self.color = color

    def get_points(self):
        return [self.start, self.end]