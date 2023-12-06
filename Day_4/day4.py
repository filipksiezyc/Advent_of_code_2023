from typing import TextIO, Any


def fast_mul_by_two(n: int) -> int:
    return 0 if n == 0 else 1 << (n - 1)


def read_input_card(file_ref: TextIO) -> list[tuple[Any, Any]]:
    lines = file_ref.readlines()
    parsed = []

    for line in lines:
        cutoff_idx = line.find(':')
        trimmed = line[cutoff_idx + 1:]
        wins, numbers = trimmed.split('|')
        wins = wins.strip().split(' ')
        numbers = numbers.strip().split(' ')

        wins = [el for el in wins if el != '']
        numbers = [el for el in numbers if el != '']
        parsed.append((wins, numbers))

    return parsed


def change_input_to_dict(lst: list[tuple[list[str], list[str]]]) -> dict[int: list[tuple[list[str], list[str]]]]:
    cards = {}

    for i, el in enumerate(lst):
        cards[i + 1] = el

    return cards


def part_one(winning_numbers: list[tuple[list[str], list[str]]]) -> int:
    score = 0

    for win, num in winning_numbers:
        match = len([el for el in num if el in win])
        score += fast_mul_by_two(match)

    return score


def get_loses(card_set: dict[int: list[tuple[list[str], list[str]]]]):
    loses = {}

    for k, v in card_set.items():
        match = [el for el in v[1] if el in v[0]]
        if len(match) == 0:
            loses[k] = 0

    return loses


def has_nonzero_el(card_set: dict[int: list[tuple[list[str], list[str]]]]):
    for _, v in card_set.items():
        if v != 0:
            return True
    return False


def part_two(scratch_pairs: list[tuple[list[str], list[str]]],
             card_set: dict[int: list[tuple[list[str], list[str]]]]) -> int:
    base_pairs = {n: 1 for n in card_set.keys()}
    bonus_pairs = {n: 0 for n in card_set.keys()}

    for i, (win, num) in enumerate(scratch_pairs):
        match = len([el for el in num if el in win])
        if match != 0:
            for j in range(1, match+1):
                base_pairs[i+j+1] += 1
                bonus_pairs[i+j+1] += 1

    while has_nonzero_el(bonus_pairs):
        for k in bonus_pairs.keys():
            if bonus_pairs.get(k) > 0:
                bonus_pairs[k] -= 1

                match = len([el for el in card_set[k][1] if el in card_set[k][0]])
                if match != 0:
                    for j in range(1, match + 1):
                        base_pairs[k+j] += 1
                        bonus_pairs[k+j] += 1

    return sum(base_pairs.values())


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input_cards = read_input_card(file)
        result_part_one = part_one(input_cards)
        print(f'Score for part one is: {result_part_one}')

        cards_set = change_input_to_dict(input_cards)
        result_part_two = part_two(input_cards, cards_set)
        print(f'Score for part two is: {result_part_two}')
