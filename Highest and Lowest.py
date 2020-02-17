def high_and_low(numbers):
    numlist = [int(x) for x in numbers.split(' ')]
    return str(min(numlist)) + ' ' + str(max(numlist))


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
