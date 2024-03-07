

def solution(picture):
    width = len(picture[0]) + 2
    picture = ["*" * width] + ["*" + i + "*" for i in picture] + ["*" * width]
    return picture


print(solution(["abc", "ded"]))
print(solution(["abc", "ded"]) == ["*****", "*abc*", "*ded*", "*****"])

# best solution - same as mine

