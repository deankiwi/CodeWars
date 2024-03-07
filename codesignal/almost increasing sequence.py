


def solution(sequence):
    count = 0
    if len(sequence) <= 2:
        return True
    for i in range(len(sequence) - 1):
        print(sequence[i], sequence[i + 1])
        if sequence[i] >= sequence[i + 1]:

            print(solution2(sequence[:i+1] + sequence[i + 2 :]), "solution2")
            print(solution2(sequence[:i] + sequence[i + 1 :]), "solution2")
            return solution2(sequence[:i+1] + sequence[i + 2 :]) or solution2(sequence[:i] + sequence[i + 1 :])
    return count <= 1


def solution2(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True


# best solution

# def solution(sequence):
#     fails1 = 0
#     fails2 = 0

#     for i in range(len(sequence)-1):
#             if sequence[i] >= sequence[i+1]:
#                 fails1 = fails1 + 1

#     for i in range(len(sequence)-2):
#             if sequence[i] >= sequence[i+2]:
#                 fails2 = fails2 + 1

#     if (fails1 < 2) and (fails2 < 2):

#         return True
#     else:
#         return False

print(solution([1, 3, 2]))  # True
print(solution([1, 3, 2, 1]))  # False
print(solution([1, 2, 1, 2]))  # False
print(solution([1, 2, 3, 4, 5, 3, 5, 6]))  # False
print(solution([1, 2, 3, 4, 100, 5, 6, 7]))  # True
