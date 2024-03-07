#  all longest strings


def solution(inputArray):
    longestStrings = []
    longest = 0
    for i in inputArray:
        if len(i) > longest:
            longest = len(i)
            longestStrings = [i]
        elif len(i) == longest:
            longestStrings.append(i)
    return longestStrings


print(solution(["aba", "aa", "ad", "vcd", "aba"]))  # ["aba", "vcd", "aba"]


# best solution - find max first, then filter for max
# def solution(inputArray):
#     m = max(len(s) for s in inputArray)
#     r = [s for s in inputArray if len(s) == m]
#     return r