

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self) -> str:
        return str(self.val)

def create_linked_list(head, pos):
    output = []
    for num in head:
        output.append(ListNode(num))
    for i in range(len(head)-1):
        output[i].next = output[i+1]
    if pos != -1:
        output[-1].next = output[pos]
    return output[0]

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next # type: ignore
            if fast == slow:
                return True

        return False


head = create_linked_list(head = [3,2,0,-4], pos = 1)

print(Solution().hasCycle(head), ' = True')
print(Solution().hasCycle(create_linked_list([1,2],0)), ' = True')
print(Solution().hasCycle(create_linked_list([1,2],-1)), ' = False')

print(head[0].next.val)
print(head[0].next.next.val)
    


