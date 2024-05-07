from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return str(self.val)

    def display(self):
        print(f"{self.val}, ", end="")
        if self.next:
            self.next.display()
        else:
            print(':end')


def create_linked_list(head: List[int], pos = -1):
    output = []
    for num in head:
        output.append(ListNode(num))
    for i in range(len(head) - 1):
        output[i].next = output[i + 1]
    if pos != -1:
        output[-1].next = output[pos]
    return output[0]

