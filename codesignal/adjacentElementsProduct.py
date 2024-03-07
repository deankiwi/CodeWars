def solution(inputArray):
    max = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        if inputArray[i] * inputArray[i + 1] > max:
            max = inputArray[i] * inputArray[i + 1]
    return max


print(solution([3, 6, -2, -5, 7, 3]))

# best solution

# def solution(inputArray):
#     return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
