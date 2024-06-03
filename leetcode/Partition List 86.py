
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ...
        dummy_high = higher = ListNode()

        dummy_low = lower = ListNode()

        curr = head

        while curr:
            next = curr.next
            if curr.val < x:
                lower.next = curr
                lower = lower.next
            else:
                higher.next = curr
                higher = higher.next

            curr = next

        higher.next = None

        lower.next = dummy_high.next

        return dummy_low.next


"""
86. Partition List
Medium
Topics
Companies
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

