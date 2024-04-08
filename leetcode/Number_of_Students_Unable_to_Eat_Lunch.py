
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for student in students:
            count[student] += 1
        # print(count)
        for index, sandwich in enumerate(sandwiches):
            if count[sandwich] == 0:
                # print(index)
                return len(sandwiches) - index
            count[sandwich] -= 1
            if sum(count) == 0:
                # print(count)
                # print('here')
                return 0
        return 0


print(Solution().countStudents([1, 1, 0, 0], [0, 1, 0, 1]), 0)
print(Solution().countStudents([1, 1], [0, 1]), 2)
print(Solution().countStudents([1, 1], [0, 0]), 2)
print(Solution().countStudents([], []), 0)
print(Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), 3)

