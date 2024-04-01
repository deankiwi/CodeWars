

def solution(A):
    n = len(A) + 1
    total_sum = n * (n + 1) // 2 
    array_sum = sum(A)
    return total_sum - array_sum


print(solution([2,3,1,5])) #4

