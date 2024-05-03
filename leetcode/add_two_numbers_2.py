
from typing import List, Optional


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


def create_linked_list(head: List[int], pos):
    output = []
    for num in head:
        output.append(ListNode(num))
    for i in range(len(head) - 1):
        output[i].next = output[i + 1]
    if pos != -1:
        output[-1].next = output[pos]
    return output[0]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):

        val_1 = l1
        val_2 = l2

        head = ListNode(0)
        nextNode = head
        leftover = 0
        num = 0
        while val_1 or val_2 or leftover:
            num = leftover
            leftover = 0
            if val_1:
                num += val_1.val
                val_1 = val_1.next
            if val_2:
                num += val_2.val
                val_2 = val_2.next
            if num > 9:
                leftover = 1
                num = int(str(num)[-1])
            # print(f'{num = }')

            nextNode.val = num

            if val_1 or val_2 or leftover:
                nextNode.next = ListNode(0)
                nextNode = nextNode.next

        return head


l1 = create_linked_list([2, 4, 3], -1)
l2 = create_linked_list([5, 6, 4], -1)
l3 = Solution().addTwoNumbers(l1, l2)
print(f"{l3 = }")
if hasattr(l3, "display") and callable(l3.display):  # type: ignore
    print("you have returned linked list")
    print(l3.display())  # type: ignore

print('\n---test 2---\n')
l1 = create_linked_list([9], -1)
l2 = create_linked_list([9], -1)
l3 = Solution().addTwoNumbers(l1, l2)
print(f"{l3 = }")
if hasattr(l3, "display") and callable(l3.display):  # type: ignore
    print("you have returned linked list")
    print(l3.display())  # type: ignore

