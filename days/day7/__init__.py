
# Day 7: The Treachery of Whales
from math import ceil, floor


def main(data: list[str], sample: list[str]):

    positions = [int(i) for i in data[0].split(",")]
    positions_sorted = sorted(positions)
    length = len(positions)
    mid = positions_sorted[int(length / 2)]

    moved = [abs(i - mid) for i in positions_sorted]
    return sum(moved)


def calc_usage(x: int) -> int:
    return int((x * x + x) / 2)


# Day 7: The Treachery of Whales pt2
def main_pt2(data: list[str], sample: list[str]):
    positions = [int(i) for i in data[0].split(",")]
    length = len(positions)
    align_to = floor(sum(positions) / length)
    moved = [calc_usage(abs(i - align_to)) for i in positions]
    return sum(moved)
