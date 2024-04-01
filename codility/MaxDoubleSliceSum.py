










def solution(A):
    # Implement your solution here
    max_total = 0
    for i in range(1,len(A)-1):
        max_right_arm = 0
        max_left_arm = 0
        for right_arm in range(i+1,len(A)-1):
            max_right_arm = max(max_right_arm,sum(A[i+1:right_arm]))
        for left_arm in range(0,i-1):
            max_left_arm = max(max_left_arm,sum(A[left_arm+1:i]))
        max_total = max(max_total,max_right_arm+max_left_arm)
    return max_total

x = sum([2,6,-1,4,5,-1])

print(solution([3,2,6,-1,4,5,-1,2]))  # 17

