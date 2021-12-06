def read_data(day: int) -> tuple[list[str], list[str]]:

    data: list[str]
    sample: list[str]

    with open(f"days/day{day}/data.txt", encoding="utf-8", mode="r") as file:
        data = file.read().split("\n")

    with open(f"days/day{day}/sample.txt", encoding="utf-8", mode="r") as file:
        sample = file.read().split("\n")

    return data, sample
