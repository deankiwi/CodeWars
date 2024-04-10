
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()

        length = len(deck)
        index_s = [i for i in range(length)]

        take = True
        new_order = [0] * length
        new_index = []
        while index_s != []:
            front = index_s.pop(0)
            if take:
                new_index.append(front)

                take = False
            else:
                index_s.append(front)
                take = True
        for index in range(length):
            new_order[new_index[index]] = deck[index]

        return new_order


print(
    Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]),
    [2, 13, 3, 11, 5, 17, 7],
)
print(Solution().deckRevealedIncreasing([1, 10]), [1, 10])


'''
better solution:
- used the deque class from collection as you can pop items more efficiently
- each pass they would take the index from the front and then move the next one to the back

from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the deck in increasing order
        deck.sort()
        
        n = len(deck)
        result = [0] * n
        indices = deque(range(n))
        
        for card in deck:
            idx = indices.popleft()  # Get the next available index
            result[idx] = card       # Place the card in the result array
            if indices:               # If there are remaining indices in the deque
                indices.append(indices.popleft())  # Move the used index to the end of deque
        
        return result
'''

