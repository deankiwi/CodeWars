


def solution(A):
    # Implement your solution here
    for i in range(1, len(A)):
        if i not in A:
            return i
    return len(A) + 1
    



print(solution([1, 2, 3, 4, 5])) # 6
print(solution([1, 3, 6, 4, 1, 2])) # 5
print(solution([-1, 3, 6, 4, 1, 2])) # 1

