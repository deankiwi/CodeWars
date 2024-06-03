
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        fast = slow = head
        # move fast k nodes ahead of slow
        finished = False
        for i in range(k):
            if not fast.next:  # k is > than length of ListNode
                break
            fast = fast.next
        else:
            finished = True

        if not finished:

            # k is > than length of ListNode
            k = k % (i + 1)
            if k == 0:
                return head

            for _ in range(i - k):
                slow = slow.next

        while fast.next:
            fast = fast.next
            slow = slow.next  # type: ignore

        fast.next = head
        head = slow.next
        slow.next = None

        return head


nodes = ListNode(0, ListNode(1, ListNode(2)))

curr = Solution().rotateRight(nodes, 4)


print("start")
while curr:
    print(curr.val)
    curr = curr.next
print("end")

nodes = ListNode(1, ListNode(2))

curr = Solution().rotateRight(nodes, 2)


print("start")
while curr:
    print(curr.val)
    curr = curr.next
print("end")


"""
61. Rotate List
Medium
Topics
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


'''
review on solution,

same method other two pointers but clearer implantation,
by working out the length before sending out the second node

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        lastElement = head
        length = 1
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        k = k % length
            
        lastElement.next = head
        
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        answer = tempNode.next
        tempNode.next = None
        
        return answer

'''

