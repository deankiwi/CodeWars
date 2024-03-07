
def solution(n):
    n = str(n)
    half = len(n) // 2
    return sum([int(i) for i in n[:half]]) == sum([int(i) for i in n[half:]])

print(solution(1230)) # True
print(solution(239017)) # False


# best solution - similar to mine

# def solution(n):
#     s = str(n)
#     pivot = len(s)//2
#     left, right = s[:pivot], s[pivot:]
#     return sum(map(int, left)) == sum(map(int, right))

