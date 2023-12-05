import math
import re
from typing import Dict, Any, Tuple, List


def search_for_symbols(lst: list[str]) -> list[tuple[str, tuple[int, int]]]:
    symbols = []

    for i, text in enumerate(lst):
        for j, char in enumerate(text):
            if not char.isalnum() and char != '.' and char != '\n':
                symbols.append((char, (i, j)))
    return symbols


def search_for_numbers(lst: list[str]) -> list[tuple[int, tuple[int, int, int]]]:
    numbers = []

    for i, text in enumerate(lst):
        match = re.finditer(r'\b\d{1,3}\b', text)
        for mat in match:
            numbers.append((int(mat.group(0)), (i, mat.start(), len(mat.group(0)))))
    return numbers


def calculate_dist_euclid(x: tuple[int, int], y: tuple[int, int]) -> float:
    return math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))


def calculate_dist_word(x: tuple[int, int, int], y: tuple[int, int]) -> bool:
    for i in range(x[2]):
        if calculate_dist_euclid((x[1] + i, x[0]), (y[1], y[0])) < 1.5:
            return True
    return False


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        symbols_idx = search_for_symbols(lines)
        numbers_idx = search_for_numbers(lines)

        print(numbers_idx)
        print(symbols_idx)

        result = 0
        for symbol in symbols_idx:
            for number in numbers_idx:
                if calculate_dist_word(number[1], symbol[1]):
                    result += number[0]
        print(f'Part one result: {result}')

        symbols_idx = [symbol for symbol in symbols_idx if symbol[0] == '*']

        gears = {}
        for symbol in symbols_idx:
            for number in numbers_idx:
                if calculate_dist_word(number[1], symbol[1]):
                    if symbol[1] not in gears.keys():
                        gears[symbol[1]] = []
                    gears[symbol[1]].append(number[0])

        gears = [v for _, v in gears.items() if len(v) > 1]

        ratio = 0
        for gear in gears:
            ratio += gear[0] * gear[1]

        print(f'Part two result: {ratio}')



