

def solution(S):


    operations = S.split(" ")

    limit = 2**20 - 1

    stack = []
    for opp in operations:
        if opp.isnumeric():

            num = int(opp)
            if 0 <= num < limit:
                stack.append(int(opp))
            else:
                # can not accept number less than 0 or greater than 2**20-1
                return -1

        elif opp == "DUP":
            stack.append(stack[-1])
        elif opp == "POP":
            stack.pop()
        elif opp == "+":
            last, second_last = stack.pop(), stack.pop()

            if limit - last - second_last < 0:
                return -1
            stack.append(last + second_last)
        elif opp == "-":
            if len(stack) < 2:
                return -1
            last, second_last = (stack.pop()), stack.pop()
            stack.append(last - second_last)
            if stack[-1] < 0:
                return -1


    if len(stack) == 0:
        return -1

    return stack[-1]


print(solution("4 5 6 - 7 +"), "= 8")
print(solution("4 5 6 - 7 + 9"), "= 9")
print(solution("13 DUP 4 POP 5 DUP + DUP + -"), " = 7")
print(solution("1048574 1 +"))
print(solution("0"), " = 0")

# will make error:

print(solution("1048576"), " = -1")
print(solution("-1"), " = -1")
print(solution(""), " = -1")
print(solution("5 6 + -") , ' = -1')
print(solution("3 DUP 5 - -"), " = -1")
print(solution("1048575 1 +") , ' = -1')
print(solution("1048575 DUP +") , ' = -1')


'''
thoughts

we can not start from the back as you need to know if there would be an error on the way

we could do it in a single pass rather than using split but code is clearer
'''

