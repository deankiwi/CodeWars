class Solution:
    def numTilings(self, n: int) -> int:
        # end tiles, number
        count = {"": 0, "I": 1, "II": 0, "LL": 0, "ll": 0}
        for i in range(n - 1):
            next_count = {"": 0, "I": 0, "II": 0, "LL": 0, "ll": 0}
            next_count[""] = count["I"] + count["II"] * 2
            next_count["I"] = count[""] + count["LL"]
            next_count["II"] = count["I"] + count["II"]
            next_count["LL"] = count["II"]
            next_count["ll"] = count["LL"]*2 + count["ll"]
            count = next_count
        return count[""] + count["I"] + count["II"]


print(f"{Solution().numTilings(1) = } = 1")
print(f"{Solution().numTilings(2) = } = 2")
print(f"{Solution().numTilings(3) = } = 5")
print(f"{Solution().numTilings(4) = } = 9")
print(f"{Solution().numTilings(5) = } = 9")
