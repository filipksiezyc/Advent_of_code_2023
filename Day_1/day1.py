import re

def part_one(lines: list[str]) -> int:
    num_sum = 0

    for line in lines:
        first = ''
        last = ''

        for char in line:
            if char.isnumeric():
                if first == '':
                    first = char
                last = char

        num_sum += int(first + last)

    return num_sum


def part_two(lines: list[str]) -> int:
    numbers_words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    regexp = r'(?=(\d|' + '|'.join(numbers_words.keys()) + '))'
    for i, line in enumerate(lines):
        nums = re.findall(regexp, line)

        for j, num in enumerate(nums):
            if not num.isnumeric():
                nums[j] = numbers_words[num]

        lines[i] = "".join(nums)

    return part_one(lines)


if __name__ == '__main__':
    filename = 'input_zad1.txt'

    with open(filename, 'r') as file:
        lines = file.readlines()
        output_part_one = part_one(lines)
        print(output_part_one)

        output_part_two = part_two(lines)
        print(output_part_two)
