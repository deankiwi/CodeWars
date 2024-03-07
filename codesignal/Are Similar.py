

def solution(a, b):
    lives = 2
    wrongA = 0
    wrongB = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            if lives == 0:
                return False
            lives -= 1
            if wrongA:
                if wrongA != b[i] or wrongB != a[i]:

                    return False
                else:

                    wrongA = 0
                    wrongB = 0
            else:

                wrongA = a[i]
                wrongB = b[i]

    if wrongA and wrongB:

        return False

    return True


print(solution([1, 2, 3], [2, 1, 3]))  # True
print(solution([1, 2, 3], [2, 1, 3]))  # true
print(solution([1, 2, 4], [1, 2, 3]))  # false
print(solution([1, 2, 3], [2, 2, 3]))  # false
print(solution([1, 1, 2, 2], [2, 2, 1, 1]))  # false


print(
    solution(
        [832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
        [832, 570, 148, 998, 533, 561, 455, 147, 894, 279],
    )
)


# best solution - lot simpler solution, sorted(A)==sorted(B) checks if the lists are the same, and sum([a!=b for a,b in zip(A,B)])<=2 checks if there are at most 2 differences

# def solution(A, B):
#     return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2

