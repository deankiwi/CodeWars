
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-106)
        dummy.next = head

        if not head:
            return head

        left = dummy

        mid = head

        right = head.next

        completed_cycle = True

        while right:
            if mid.val > right.val:
                completed_cycle = False
                temp = right.next
                mid.next = temp
                right.next = mid
                left.next = right
                mid, right = right, mid
            if right.next:
                left, mid, right = left.next, mid.next, right.next
            elif not right.next and completed_cycle:
                right = None
            else:
                completed_cycle = True
                left, mid, right = dummy, dummy.next, dummy.next.next

        return dummy.next


"""
148. Sort List
Medium
Topics
Companies
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""


'''
Had time out error and solution was too slow, 
Although not O(1) memory merge short would have been a better solution
'''

