from typing import TypedDict, List


class Order(TypedDict):
    direction: str
    turns: int


def get_zeros_clicks_pt1(start: int, orders: List[Order]) -> int:
    count = 0
    curr = start
    for order in orders:
        # print(f"{order=}, {curr=}")
        turns = order["turns"]
        if order["direction"] == "L":
            turns *= -1
        curr += turns
        curr %= 100
        if curr == 0:
            count += 1

    return count


def get_zeros_clicks_pt2(start: int, orders: List[Order]) -> int:
    count = 0
    curr = start
    for order in orders:
        turns = order["turns"]
        if order["direction"] == "L":
            turns *= -1
        if turns > 0:
            crossings = (curr + turns) // 100 - curr // 100
        elif turns < 0:
            crossings = (curr - 1) // 100 - (curr + turns - 1) // 100
        else:
            crossings = 0

        count += crossings
        curr = (curr + turns) % 100

    return count


def txt_to_orders(filepath: str) -> List[Order]:
    orders = []
    with open(filepath, "r") as file:
        for line in file:
            orders.append({"direction": line[0], "turns": int(line[1:])})

    return orders


def main():
    orders = txt_to_orders("advent-of-code-2025/day-1/example.txt")
    # print(orders)

    print("example: ", get_zeros_clicks_pt1(50, orders))
    print("example: ", get_zeros_clicks_pt2(50, orders))

    orders = txt_to_orders("advent-of-code-2025/day-1/actual.txt")
    # print(orders)

    print("actual: ", get_zeros_clicks_pt1(50, orders))
    print("actual: ", get_zeros_clicks_pt2(50, orders))

if __name__ == "__main__":
    main()