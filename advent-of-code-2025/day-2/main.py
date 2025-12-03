from pathlib import Path
from typing import List, Tuple

import pytest


def get_next_invalid(curr: int) -> int:
    if curr < 11:
        return 11
    s_n = str(curr)
    length = len(s_n)
    if length % 2 == 1:
        num_zeros = length // 2
        pattern_string = "1" + ("0" * num_zeros) + "1" + ("0" * num_zeros)

        return int(pattern_string)
    s_n_next = str(int(s_n[: length // 2])) * 2
    if int(s_n_next) > curr :
        return int(s_n_next)
    s_n_next = str(int(s_n[: length // 2]) + 1) * 2

    if len(s_n_next) % 2 == 1:
        num_zeros = length // 2
        pattern_string = "1" + ("0" * num_zeros) + "1" + ("0" * num_zeros)

        return int(pattern_string)

    return int(s_n_next)


def part1(spreads: List[Tuple[int, int]]) -> int:
    total = 0
    for left, right in spreads:
        curr = get_next_invalid(left - 1)

        while curr <= right:
            total += curr
            curr = get_next_invalid(curr)

    return total


def part2(spreads: List[Tuple[int, int]]) -> int:
    return 0


def parser(raw_date: str) -> List[Tuple[int, int]]:
    output = []
    for spread in raw_date.split((",")):
        left, right = spread.split("-")
        output.append((int(left), int(right)))
    return output


raw_data_example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def test_parser():
    test = parser(raw_data_example)
    print(test)
    assert test == [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]


def test_get_next_invalid():
    assert get_next_invalid(9) == 11
    assert get_next_invalid(94) == 99
    assert get_next_invalid(99) == 1010
    assert get_next_invalid(998) == 1010
    assert get_next_invalid(95) == 99
    assert get_next_invalid(998) == 1010
    assert get_next_invalid(1188511880) == 1188511885
    assert get_next_invalid(222220) == 222222
    assert get_next_invalid(446443) == 446446
    assert get_next_invalid(38593856) == 38593859

def test_part1_example():

    example = parser((raw_data_example))
    assert part1(example) == 1227775554


if __name__ == "__main__":
    test_parser()
    test_get_next_invalid()
    test_part1_example()
    print("All tests passed.")
    # not run with data from "data.txt"
    actual = parser(Path("advent-of-code-2025/day-2/data.txt").read_text().strip())
    print("Part 1:", part1(actual))
