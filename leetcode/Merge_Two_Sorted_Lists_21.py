

from typing import Optional

from utils.utils import ListNode, create_linked_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        head = ListNode(0)
        stack = head


        while list1 or list2:

            if list1 and list2:
                if list1.val > list2.val:
                    stack.val = list2.val
                    list2 = list2.next

                else:
                    stack.val = list1.val

                    list1 = list1.next

            elif list1:
                stack.val = list1.val

                list1 = list1.next

            elif list2:
                stack.val = list2.val
                list2 = list2.next

            if list1 or list2:
                stack.next = ListNode(0)
                stack = stack.next

        return head


list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

print(Solution().mergeTwoLists(list1, list2).display())
print([1, 1, 2, 3, 4, 4])
print(Solution().mergeTwoLists(None, None))
"""
21. Merge Two Sorted Lists


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""


'''
cleaner solution

same design patter as mine

1) used dummy at start then returned .next at end
2) copied class rather than assign a value
3) at the end added the rest of list to the end.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
'''

