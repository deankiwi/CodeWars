def solution(inputString):
    length = len(inputString)
    if len(inputString) <= 1:
        return True

    print(
        inputString[: (length // 2)], inputString[: length // 2 - 1 + length % 2 : -1]
    )

    if inputString[: (length // 2)] == inputString[: length // 2 - 1 + length % 2 : -1]:
        return True
    return False


# best solution - got it very wrong, should have just flipped the string and compared it to the original rather than look for the middle of the string
def solution(inputString):
    return inputString == inputString[::-1]





