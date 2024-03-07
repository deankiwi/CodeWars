

def solution(a):
    sorted_list = sorted([i for i in a if i != -1])

    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted_list.pop(0)
    return a


print(
    solution([-1, 150, 190, 170, -1, -1, 160, 180])
)  # [-1, 150, 160, 170, -1, -1, 180, 190]


# best solution - more of a pure function approach by inserting -1s in the sorted list

# def solution(a):

#     l = sorted([i for i in a if i > 0])
#     for n,i in enumerate(a):
#         if i == -1:
#             l.insert(n,i)
#     return l

