# make array consecutive 2


def solution(statues):
    missing = [x for x in range(min(statues), max(statues)) if x not in statues]
    return len(missing)


# best solution
# def solution(statues):
#     return max(statues) - min(statues) - len(statues) + 1

print(solution([6, 2, 3, 8]))  # 3
