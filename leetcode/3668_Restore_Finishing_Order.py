from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        seen = set()
        for friend in friends:
            seen.add(friend)
        
        for f in order:
            if f in seen:
                result.append(f)


        return result