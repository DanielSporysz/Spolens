import re
from structures import Point
from structures import Line


def read_setup(fname):
    f = open(fname, "r")
    if f.mode == 'r':
        lines = []

        points = {}
        for idx, file_line in enumerate(f.readlines()):
            # Lines starting with P define a Point
            # e.g. P pointID 300 300 300
            if file_line[0] == 'P':
                # validate line
                if len(re.findall(r'P [A-Za-z]+ (([-+]?(\d+\.?\d*)) ?){3}', file_line)) != 1:
                    raise Exception(
                        "Line " + idx + " has unsupported data format!")

                # parse data
                point_id = re.findall(r'[A-Za-z]+', file_line)[1]
                coords = re.findall(r'[-+]?\d+\.?\d*', file_line)
                coords = [float(i) for i in coords]

                # create a point
                point = Point(coords[0], coords[1], coords[2])
                points[point_id] = point

            # Lines starting with C define a connection
            # e.g. 'C pointID_A pointID_V 1 0 0 1'
            elif file_line[0] == 'C':
                # validate line
                if len(re.findall(r'C [A-Za-z]+ [A-Za-z]+ (([-+]?(\d+\.?\d*)) ?){4}', file_line)) != 1:
                    raise Exception(
                        "Line " + idx + " has unsupported data format!")

                # parse data
                point_ids = re.findall(r'[A-Za-z]+', file_line)[1:3]
                color = re.findall(r'[-+]?\d+\.?\d*', file_line)
                color = [float(i) for i in color]

                # connect points
                line = Line(points[point_ids[0]], points[point_ids[1]], color)
                lines.append(line)

        return lines
    else:
        raise Exception("Couldn't read file: " + fname + "!")
