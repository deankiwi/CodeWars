
from collections import defaultdict
def solution(A):
    # Implement your solution here
    seen = defaultdict(int)
    for num in A:
        if seen[num-1] or seen[num+1]:
            return True
        seen[num] +=1

    return False

print(solution([7]))
print(solution([7,8]), '= true')
print(solution([7,9]))

