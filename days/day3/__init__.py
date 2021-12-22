import functools

from helpers.data import read_data

# Day3: Binary Diagnostic
def main():
    lines, _ = read_data(3)

    gamma_number = ""

    for column in range(len(lines[0])):

        ones = 0
        zeros = 0

        for number in lines:
            if number[column] == "1":
                ones += 1
            elif number[column] == "0":
                zeros += 1

        if ones > zeros:
            gamma_number += "1"
        else:
            gamma_number += "0"

    # print(gamma_number)

    gamma = int(gamma_number, 2)
    epsilon = gamma ^ (2 ** (len(gamma_number) + 1) - 1)
    epsilon = int(bin(epsilon)[3:], 2)

    # print(f"{epsilon:b}")
    #
    # print(gamma)
    # print(epsilon)
    return gamma * epsilon


# Day3: Binary Diagnostic pt2
def main_pt2():
    lines, _ = read_data(3)

    oxygen = lines.copy()
    co2 = lines.copy()

    for column in range(len(lines[0])):
        if len(oxygen) == 1 and len(co2) == 1:
            break

        if len(oxygen) > 1:
            oneCount = functools.reduce(lambda prev, curr: prev + int(curr[column]), oxygen, 0)
            zeroCount = len(oxygen) - oneCount

            if oneCount >= zeroCount:
                oxygen = list(filter(lambda x: x[column] == "1", oxygen))
            else:
                oxygen = list(filter(lambda x: x[column] == "0", oxygen))

        if len(co2) > 1:
            oneCount = functools.reduce(lambda prev, curr: prev + int(curr[column]), co2, 0)
            zeroCount = len(co2) - oneCount

            if oneCount >= zeroCount:
                co2 = list(filter(lambda x: x[column] == "0", co2))
            else:
                co2 = list(filter(lambda x: x[column] == "1", co2))

    return int(oxygen[0], 2) * int(co2[0], 2)
