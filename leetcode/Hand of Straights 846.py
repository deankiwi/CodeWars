
from collections import Counter, deque
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        groupMade = deque()
        prev = None

        for num in sorted(count.keys()):

            diff = count[num] - len(groupMade)
            if prev == None or num - prev != 1:
                if len(groupMade) > 0:
                    return False
                groupMade.extend([1] * count[num])
            elif diff < 0:
                return False

            else:
                for i in range(len(groupMade)):
                    groupMade[i] += 1
                groupMade.extend([1] * diff)

            while groupMade and groupMade[0] == groupSize:
                groupMade.popleft()

            prev = num

        return len(groupMade) == 0


print(Solution().isNStraightHand([1, 2, 3, 4, 5, 6][::-1], 2))
print(Solution().isNStraightHand([1, 1, 1, 2, 2, 2][::-1], 2))
print(Solution().isNStraightHand([1, 1, 1, 2, 2, 3][::-1], 2))

"""
846. Hand of Straights
Medium
Topics
Companies
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
"""


'''
Better solution, for each value in the heap map walk up the heap map to make a 
group one at a time. This saves on memory and same time complexity

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Step 1: Check if grouping is possible
        if len(hand) % groupSize != 0:
            return False
        
        # Step 2: Count the occurrences of each card
        count = Counter(hand)
        
        # Step 3: Sort the unique card values
        sorted_keys = sorted(count.keys())
        
        # Step 4: Form consecutive groups
        for key in sorted_keys:
            if count[key] > 0:  # If this card is still available
                start_count = count[key]
                # Check and form a group starting from `key`
                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        
        # Step 5: Return True if all groups are formed successfully
        return True
'''

