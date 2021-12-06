# Dive!
from helpers.data import read_data


def main():
    operations, _ = read_data(2)

    horizontal = 0
    depth = 0

    for operation in operations:
        direction, amount = operation.split(" ")

        if direction == "forward":
            horizontal += int(amount)
        elif direction == "up":
            depth -= int(amount)
        elif direction == "down":
            depth += int(amount)

    return horizontal * depth


# Dive! pt2
def main_pt2():

    operations, _ = read_data(2)

    horizontal = 0
    depth = 0
    aim = 0

    for operation in operations:
        direction, amount = operation.split(" ")
        amount = int(amount)

        if direction == "forward":
            horizontal += amount
            depth += amount * aim
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount

    return horizontal * depth
