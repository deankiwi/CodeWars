
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: ListNode) -> Optional[ListNode]:

        last_0 = head
        curr = head
        total = 0

        while curr.next:
            curr = curr.next
            if curr.val == 0:
                last_0.val = total
                last_0.next = curr
                if curr.next:
                    last_0 = curr
                    total = 0
            else:
                total += curr.val
        
        last_0.next = None
                

        return head
    
