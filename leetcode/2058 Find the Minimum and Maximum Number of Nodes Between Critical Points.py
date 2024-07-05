
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        count = 0
        #index of critical
        first_critical = -1
        last_critical = -1
        min_dis = float('inf')

        stack = deque()

        curr = head

        while curr and count < 2:
            count += 1
            stack.append(curr.val)
            curr = curr.next

        if count != 2:
            return [-1,-1]
        
        while curr:
            count += 1
            stack.append(curr.val)
            left = stack.popleft()
            mid = stack[0]
            right = stack[-1]

            if (left < mid > right) or (left > mid < right):
                if first_critical == -1:
                    first_critical = count
                else:
                    min_dis = min(min_dis, count-last_critical)
                
                last_critical = count
            curr = curr.next
        if first_critical == last_critical:
            return [-1,-1]
        return [min_dis, last_critical - first_critical ]

