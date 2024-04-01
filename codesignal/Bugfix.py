


def solution(a):

    indexOfMinimum = -1
    minimalSum = float('inf')


    for i in range(len(a)):
        curSum = 0
        for j in range(len(a)):
            curSum += abs(a[j] - a[i])
        if curSum < minimalSum:
            minimalSum = curSum
            indexOfMinimum = i

    return a[indexOfMinimum]



print(solution([2,4,7])) # 4
# print(solution([1, 3, 3, 1, 1])) # 1

