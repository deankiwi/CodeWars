

import pprint
from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        total = 0
        crossed = 0

        for n in nums:
            # print(f'{n = } {total - n = }')
            if total > 0 and total + n == 0:
                # print('negative')
                crossed += 1
            elif total < 0 and total + n == 0:
                # print('postive')
                crossed += 1

            total += n

        return crossed

    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        count = 1

        for i in range(k, len(word), k):
            if word[0 : len(word) - i] == word[i:]:
                return count
            count += 1

        # print('hit')
        return count

    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        W = len(image[0])
        H = len(image)

        result = [[[] for _ in range(W)] for _ in range(H)]

        def is_region(i, j):
            for jj in range(-1, 2, 1):
                if abs(image[i - 1][j + jj] - image[i][j + jj]) > threshold:
                    return False
                if abs(image[i][j + jj] - image[i + 1][j + jj]) > threshold:
                    return False
            for ii in range(-1, 2, 1):
                if abs(image[i + ii][j] - image[i + ii][j - 1]) > threshold:
                    return False
                if abs(image[i + ii][j] - image[i + ii][j + 1]) > threshold:
                    return False

            return True

        for i in range(1, H - 1):
            for j in range(1, W - 1):
                if is_region(i, j):
                    ...

        for i in range(H):
            for j in range(W):
                if len(result[i][j]) == 0:
                    result[i][j] = image[i][j]  # type: ignore

        return result


result = [[[] for _ in range(4)] for _ in range(4)]

pprint.pprint(result)
result[0][0] = 10
pprint.pprint(result)
for i in range(-1, 2, 1):
    print(i)


# print(f'{Solution().returnToBoundaryCount([2,3,-5]) = } == 1')
# print(f'{Solution().returnToBoundaryCount([3,2,-3,-4]) = } == 0')
# print(f'{Solution().returnToBoundaryCount([-10,10]) = } == 1')
# print(f'{Solution().returnToBoundaryCount([-7,10]) = } == 0')
# print(f'{Solution().minimumTimeToInitialState(word = "abacaba", k = 3) = } == 2')
# print(f'{Solution().minimumTimeToInitialState(word = "abacaba", k = 4) = } == 1')
# print(f'{Solution().minimumTimeToInitialState(word = "abcbabcd", k = 2) = } == 4')

