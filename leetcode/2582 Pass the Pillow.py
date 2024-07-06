
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % ((n * 2) - 2)

        if time < n:
            return time +1
        
        return n*2-1 - time
        
