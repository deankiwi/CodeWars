

# Definition for singly-linked list.
from typing import Optional

from utils.utils import create_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        length = 0
        curr = head
        while curr:
            length += 1
            if length == k:

                new_head = curr
            curr = curr.next

        curr = head
        last = None

        for _ in range(length // k):
            end = curr
            print(f"{end.val = }")
            before = curr
            curr = curr.next
            for _ in range(k - 1):
                # print(f"{curr.val  = }")

                next = curr.next

                curr.next = before

                before = curr
                curr = next

            # print(f"{curr.val = } end of ")
            print(f"{before.val = }")

            if last:
                last.next = before

            else:
                last = end

        end.next = curr

        return new_head


# linked_list = create_linked_list([1, 2, 3, 4, 5])
# linked_list.display()

# new_list = Solution().reverseKGroup(linked_list, 2)
# new_list.display()

linked_list = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
linked_list.display()

new_list = Solution().reverseKGroup(linked_list, 3)
new_list.display()

"""
25. Reverse Nodes in k-Group
Hard
Topics
Companies
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

