
from collections import defaultdict


def solution(A):
    # Implement your solution here
    seen = defaultdict(int)
    for num in A:
        seen[num] += 1
    for i in range(1,len(A)+2):
        if not seen[i]:
            return i




print(solution([1, 3, 6, 4, 1, 2]), " = 5")
print(solution([1, 2, 3]), " = 4")

