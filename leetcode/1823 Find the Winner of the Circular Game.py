

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [1] * n
        loc = 0
        count = 1
        for _ in range(n - 1):
            for _ in range(k - 1):
                loc = (loc + 1) % n
                while players[loc] == 0:
                    loc = (loc + 1) % n

            # print(f'remove: {loc + 1}')

            players[loc] = 0
            while players[loc] == 0:
                loc = (loc + 1) % n
        # print(players)
        return players.index(1) + 1


"""
    there is a much better solution but very hard to understand

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for player_num in range(2, n + 1):
            res: int = (res + k) % player_num
        return res + 1


"""

