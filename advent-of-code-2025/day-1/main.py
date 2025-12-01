
from typing import TypedDict, List

class Order(TypedDict):
    direction: str
    turns: int

def get_zeros_clicks(start: int, orders: List[Order]) -> int:
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

def txt_to_orders(filepath: str) -> List[Order]:
    orders = []
    with open(filepath, "r") as file:
        for line in file:
            orders.append({"direction": line[0], "turns": int(line[1:])})

    return orders

def main():
    orders = txt_to_orders("advent-of-code-2025/day-1/example.txt")
    # print(orders)
    
    print("example: " , get_zeros_clicks(50, orders))

    orders = txt_to_orders("advent-of-code-2025/day-1/actual.txt")
    # print(orders)
    
    print("actual: " , get_zeros_clicks(50, orders))


main()