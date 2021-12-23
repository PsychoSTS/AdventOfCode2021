# Day 6: Lanternfish
def main(data: list[str], sample: list[str]):
    timers = [int(n) for n in sample[0].split(',')]
    births = []

    # print(timers)
    for _ in range(80):
        print(_)

        # First decrement timers
        for i, timer in enumerate(timers):

            if timer == 0:
                births.append(i)
            else:
                timers[i] = timer - 1

        # Then do births
        for birth in births:
            timers.append(8)
            timers[birth] = 6

        # print(timers)
        births = []

    return len(timers)


simulation_time = 256


def calc_births(timer: int, days_left: int, days_past: int = 0) -> int:
    if days_left <= 0:
        return 0

    births = int((7 - timer + days_left) / 7)

    child_births = 0
    if births > 0:
        for i in range(births):
            day = days_past + timer + (7 * i) + 1
            if day > simulation_time:
                births -= 1

            child_births += calc_births(8, simulation_time - day, day)

    return births + child_births


levels = []


def calc_tree(timer: int, days_left: int, days_past: int = 0, level=1):

    if days_left <= 0:
        return 0

    births = int((7 - timer + (days_left - 1)) / 7)
    birth_days = []

    child_births = 0
    if births > 0:
        for i in range(births):
            day = days_past + timer + (7 * i) + 1
            if day > simulation_time:
                births -= 1

            birth_days.append(day)

        if len(levels) < level:
            levels.append(birth_days)
        else:
            levels[level].extend(birth_days)

        for d in birth_days:
            calc_tree(8, simulation_time - d, d, level + 1)

    return births + child_births




    # births = int((7 - timer + simulation_time) / 7)
    #
    # birth_days = []
    #
    # days_past = 0
    # for i in range(births):
    #     day = days_past + timer + (7 * i) + 1
    #     birth_days.append(day)
    #
    # print(timer)
    # print(" ".join([str(d) for d in birth_days]))


# Day 6: Lanternfish pt2
def main_pt2(data: list[str], sample: list[str]):

    fishes = [int(n) for n in sample[0].split(',')]
    days = [0] * 9

    for fish in fishes:
        days[fish] += 1

    for i in range(simulation_time):
        today = i % len(days)

        index = (today + 7) % len(days)
        days[index] += days[today]

    return sum(days)

    # print(days)




    # fish = len(timers)
    #
    # for i, timer in enumerate(timers):
    #     print(timer)
    #     calc_tree(timer, simulation_time)
    #
    #     count = 0
    #     for l in levels:
    #         print(*l, " ")
    #         count += len(l)
    #
    #     print(count + 1)
    #
    #     # children = calc_births(timer, simulation_time)
    #     # fish += children
    #
    # return fish
