from helpers.data import read_data


def flatten(t):
    return [item for sublist in t for item in sublist]


class Board:

    def __init__(self, rows: list[str]):
        self.rows: list[list[int]] = [list(map(lambda x: int(x), row.split())) for row in rows]
        self.numbers = flatten(self.rows)
        self.row_length = len(self.rows[0])
        self.column_length = len(self.rows)
        self.won = False

    def input(self, number: int):
        # If I have the number
        if number in self.numbers:
            # tag it
            index = self.numbers.index(number)
            self.numbers[index] = -1

            # x = index % self.row_length
            x = int(index / self.row_length)
            # y = index % self.column_length
            y = int(index % self.column_length)

            start = x * self.row_length
            row = self.numbers[start:start + self.row_length]
            column = [self.numbers[i  * self.row_length + y] for i in range(self.column_length)]

            if sum(row) == -self.row_length or sum(column) == -self.column_length:
                self.won = True
                return True

        return False


# Day 4: Giant Squid
def main():
    data, sample = read_data(4)
    lines = data

    inputs = [int(i) for i in lines[0].split(',')]
    separators = [i for i, x in enumerate(lines) if not bool(x)]
    boards = []

    for i, start in enumerate(separators):
        end = separators[i + 1] if i + 1 < len(separators) else len(lines)

        board = lines[start + 1:end]
        boards.append(Board(board))

        # board = [list(map(lambda x: int(x), row.split())) for row in board]
        # boards.append(board)

    for i in inputs:
        for board in boards:
            if board.input(int(i)):
                sum_value = sum([x for x in board.numbers if x >= 0])
                return sum_value * i


# Day 4: Giant Squid pt2
def main_pt2():
    data, sample = read_data(4)
    lines = data

    inputs = [int(i) for i in lines[0].split(',')]
    separators = [i for i, x in enumerate(lines) if not bool(x)]
    boards = []

    for i, start in enumerate(separators):
        end = separators[i + 1] if i + 1 < len(separators) else len(lines)

        board = lines[start + 1:end]
        boards.append(Board(board))

        # board = [list(map(lambda x: int(x), row.split())) for row in board]
        # boards.append(board)

    for i in inputs:
        for index, board in enumerate(boards):
            if board.input(int(i)):

                if len(boards) == 1:
                    sum_value = sum([x for x in board.numbers if x >= 0])
                    return sum_value * i

        boards = [b for b in boards if b.won == False]
