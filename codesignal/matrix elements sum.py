# matrix elements sum


def solution(matrix):
    sum = 0
    ghost = []
    print(ghost)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                ghost.append(j)
            if j not in ghost:
                sum += matrix[i][j]
    return sum

# # best solution
# def solution(m):
#     r = len(m)
#     c = len(m[0])
#     total=0
#     for j in range(c):
#         for i in range(r):
#             if m[i][j]!=0:
#                 total+=m[i][j]
#             else:
#                 break
#     return total

print(solution([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]))  # 9
print(solution([[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]]))  # 9
