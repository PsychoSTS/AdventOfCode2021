from dataclasses import dataclass

from helpers.data import read_data


@dataclass
class Coordinate:
    x1: int
    y1: int
    x2: int
    y2: int


def calc_line(x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
    if x1 == x2:
        if y1 < y2:
            return [(x1, i) for i in range(y1, y2 + 1)]
        else:
            return [(x1, i) for i in range(y2, y1 + 1)]

    elif y1 == y2:
        if x1 < x2:
            return [(i, y1) for i in range(x1, x2 + 1)]
        else:
            return [(i, y1) for i in range(x2, x1 + 1)]

    return []


# Day 5: Hydrothermal Venture
def main():
    data, sample = read_data(5)
    lines = sample

    points = {}

    for line in lines:
        start, end = line.replace(' ', '').split('->')
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")

        line_points = calc_line(int(x1), int(y1), int(x2), int(y2))

        for p in line_points:
            key = str(p)

            if key not in points.keys():
                points.setdefault(key, 1)
            else:
                points[key] += 1

    return len([p for p in points.values() if p > 1])


def calc_line2(x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
    if x1 == x2:
        return [(x1, i) for i in range(min(y1, y2), max(y1, y2) + 1)]

    elif y1 == y2:
        return [(i, y1) for i in range(min(x1, x2), max(x1, x2) + 1)]

    elif abs(x1 - x2) == abs(y1 - y2):
        return [(x1 + i if x1 < x2 else x1 - i, y1 + i if y1 < y2 else y1 - i) for i in range(abs(x1 - x2) + 1)]

    return []


# Day 5: Hydrothermal Venture pt2
def main_pt2():
    data, sample = read_data(5)
    lines = data

    points = {}

    for line in lines:
        start, end = line.replace(' ', '').split('->')
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")

        line_points = calc_line2(int(x1), int(y1), int(x2), int(y2))

        for p in line_points:
            key = str(p)

            if key not in points.keys():
                points.setdefault(key, 1)
            else:
                points[key] += 1

    return len([p for p in points.values() if p > 1])
