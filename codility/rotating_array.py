

def solution(A, K):
    # Implement your solution here
    new_array = []
    length = len(A)
    for i in range(length):
        print((i + K)%length)
        new_array.append(A[(i - K)%length])
    return new_array

print(solution( [3, 8, 9, 7, 6],3)) #[9, 7, 6, 3, 8]
print(solution( [3, 8, 9, 7, 6],-1)) #[9, 7, 6, 3, 8]
print(solution( [3, 8, 9, 7, 6],1)) #[9, 7, 6, 3, 8]

