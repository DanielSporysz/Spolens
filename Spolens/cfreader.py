import re


def load_objects_configuration(file_name):
    f = open(file_name, "r")
    if f.mode == 'r':
        lines = []

        for idx, file_line in enumerate(f.readlines()):
            if file_line[0] != '#':
                points = re.findall(r'\d+ \d+ \d+', file_line)

                if len(points) != 2:
                    raise Exception(
                        "Line " + idx + " has unsopported data format!")

                start_point = re.findall(r'\d+', points[0])
                end_point = re.findall(r'\d+', points[1])

                lines.append([start_point, end_point])

        return lines
    else:
        raise Exception("Problem reading: " + file_name)
