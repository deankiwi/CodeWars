


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        if not head or left == right:
            return head


        curr = head
        for j in range(left - 2):
            curr = curr.next  # type: ignore
        start = curr
        curr = curr.next  # type: ignore
        end = curr
        before = curr
        after = None


        if curr and curr.next:
            curr = curr.next

            for j in range(right - left):

                after = curr.next  # type: ignore
                curr.next = before
                before = curr
                curr = after  # type: ignore

        start.next = before
        if after:

            end.next = after

        if left == 1 and right != 1:
            return before

        return head  
    

print('test 1')
test = Solution()
node_output = test.reverseBetween(ListNode(3,ListNode(5)),1,1)
while node_output:
    print(node_output.val)
    node_output = node_output.next

print()
print('test 2')
test = Solution()
node_output = test.reverseBetween(ListNode(3,ListNode(5)),1,2)
while node_output:
    print(node_output.val)
    node_output = node_output.next
    



"""
92. Reverse Linked List II
Medium
Topics
Companies
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
"""


'''
Had issues with head being sent to back. should have justed a dummy started attached before
head to make it easier 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        # Edge case: empty list or no need to reverse
        if not head or left == right:
            return head

        # Initialize dummy node for easier head handling
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move `prev` to the node just before the reversal segment
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing the segment
        curr = prev.next
        tail = curr  # tail will eventually be the end of the reversed segment
        prev_of_segment = prev  # the node just before the start of the segment
        prev = None

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Connect the reversed segment back to the list
        prev_of_segment.next = prev
        tail.next = curr

        # Return the new head of the list
        return dummy.next

'''

