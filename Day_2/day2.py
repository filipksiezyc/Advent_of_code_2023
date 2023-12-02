from dataclasses import dataclass


@dataclass
class BagOfBalls:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def add_colors(self, red: int, green: int, blue: int):
        self.red += red
        self.green += green
        self.blue += blue

    def __str__(self) -> str:
        return f'Red: {self.red}, Green: {self.green}, Blue: {self.blue}'


def parse_id(game: str) -> int:
    id_parsed = 0
    id_start = game.find('Game')
    if id_start != -1:
        len_game = len('Game')
        id_parsed = int(game[id_start + len_game: game.find(':')])
    return id_parsed


def set_color_num(obj: BagOfBalls, color: str, value: str) -> BagOfBalls:
    match color:
        case 'blue':
            obj.blue = int(value)
        case 'red':
            obj.red = int(value)
        case 'green':
            obj.green = int(value)
    return obj


def parse_color(obj: BagOfBalls, game: str, color: str) -> BagOfBalls:
    color_end = game.find(color)
    if color_end != -1:
        if color_end < 5:
            color_start = 0
            value = game[color_start + 1: color_end]
            obj = set_color_num(obj, color, value)

        else:
            color_start = color_end - 1
            while game[color_start] != ',':
                color_start -= 1

            value = game[color_start + 2: color_end]
            obj = set_color_num(obj, color, value)
    return obj


def part_one(in_list: list[list[str]]) -> int:
    id_count = 0
    for item in in_list:
        id = 0
        drop_data = False

        for attempt in item:
            bag = BagOfBalls()

            id = parse_id(attempt) if parse_id(attempt) != 0 else id
            attempt = attempt[attempt.find(':') + 1:]
            bag = parse_color(bag, attempt, 'blue')
            bag = parse_color(bag, attempt, 'red')
            bag = parse_color(bag, attempt, 'green')

            if bag.blue > 14 or bag.red > 12 or bag.green > 13:
                drop_data = True
                break

        if not drop_data:
            id_count += id

    return id_count


def part_two(in_list: list[list[str]]) -> int:
    sum_of_power = 0

    for item in in_list:
        max_bag = BagOfBalls()

        for attempt in item:
            bag = BagOfBalls()
            attempt = attempt[attempt.find(':') + 1:]

            bag = parse_color(bag, attempt, 'blue')
            bag = parse_color(bag, attempt, 'red')
            bag = parse_color(bag, attempt, 'green')

            if bag.blue > max_bag.blue:
                max_bag.blue = bag.blue
            if bag.red > max_bag.red:
                max_bag.red = bag.red
            if bag.green > max_bag.green:
                max_bag.green = bag.green

        sum_of_power += max_bag.green * max_bag.blue * max_bag.red

    return sum_of_power


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.split(';') for line in lines]

        passing_games = part_one(lines)
        print(passing_games)

        sum_of_powers = part_two(lines)
        print(sum_of_powers)
