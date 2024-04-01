

def solution(A):
    # Implement your solution here
    total = sum(A)
    # print(A, total)
    original_length = len(A)
    min_diff = total/original_length
    location = 0
    # print(original_length)
    
    # print(total/original_length)

    for i in range(original_length):
        for j in range(original_length,original_length+1):
            #j - Q-1
            total = sum(A[i:j])
            length = len(A[i:j])
            avg = total/length
            if avg < min_diff:
                # print('new low')
                min_diff = avg
                location = i
            # print(i,j-1,A[i:j], avg)
            # if j == original_length:
            #     print('end')
                # print(i,j-1,A[i:j], avg)
    return location


print(solution([4,2,2,5,1,5,8])) # 1
print(solution([8, 5, 1, 5, 2, 2, 4])) 
# print(solution([1,10000000,1,1]))
# print(solution([1,1,-100,-100]))
# print(solution([-100,-100,1,1]))

# could not do

