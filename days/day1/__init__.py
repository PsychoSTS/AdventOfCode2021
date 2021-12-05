
# Sonar sweep
def main():
    with open("days/day1/data.txt", mode="r", encoding="utf-8") as file:
        depths = list(map(lambda item: int(item), file.read().split("\n")))

        inc = 0
        for i in range(1, len(depths)):
            if depths[i] > depths[i - 1]:
                inc += 1

        return inc


# Sonar sweep pt2
def main_pt2():
    with open("days/day1/data.txt", mode="r", encoding="utf-8") as file:
        depths = list(map(lambda item: int(item), file.read().split("\n")))

        inc = 0
        for i in range(3, len(depths)):

            w1 = depths[i-3:i]
            w2 = depths[i-2:i+1]

            window1 = sum(w1)
            window2 = sum(w2)

            if window2 > window1:
                inc += 1

        return inc
