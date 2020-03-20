import re


def string_list_to_float(slist):
    return [float(i) for i in slist]


def load_objects_configuration(file_name):
    f = open(file_name, "r")
    if f.mode == 'r':
        lines = []

        for idx, file_line in enumerate(f.readlines()):
            if file_line[0] != '#':
                points = re.findall(r'-?\d+ -?\d+ -?\d+', file_line)
                if len(points) != 3:
                    raise Exception(
                        "Line " + idx + " has unsopported data format!")
                start_point = string_list_to_float(
                    re.findall(r'-?\d+', points[0]))
                end_point = string_list_to_float(
                    re.findall(r'-?\d+', points[1]))

                color = re.findall(r'c .*', file_line)
                color = re.findall(r'([0-9]*\.[0-9]+|[0-9]+)', color[0])
                color = string_list_to_float(color)

                # print([start_point, end_point, color])

                lines.append([start_point, end_point, color])

        return lines
    else:
        raise Exception("Problem reading: " + file_name)
