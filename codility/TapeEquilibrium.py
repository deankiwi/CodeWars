
def solution(A):
    # Implement your solution here
    sumRight = sum(A[1:])
    # print(sumRight)
    sumLeft = A[0]
    # print(sumLeft)

    min_diff = abs(sumLeft - sumRight)
    # print(min_diff)

    for number in A[1:-1]:
        sumRight -= number
        sumLeft += number
        if abs(sumLeft - sumRight) < min_diff:
            # print('here')
            min_diff = abs(sumLeft - sumRight)
        
    
    return min_diff

print(solution([3,1,2,4,3]))
print(solution([100,1]))
print(solution([100,1,1]))
print(solution([1,100]))
print(solution([100]))
print(solution([1,1,1,1,-1111111,100]))
print(solution([1,-1,-1]))
print(solution([101,100]))
print(solution([-100,100]))
print(solution([100,-100]))

