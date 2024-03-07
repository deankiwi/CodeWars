

def solution(inputString):
    output = ""
    stack = []
    for i in range(len(inputString)):
        # print(inputString, stack, output, inputString[i])
        if "(" == inputString[i]:
            stack.append("")
        elif ")" == inputString[i]:
            stack.append(stack.pop()[::-1])
            if len(stack) > 1:
                stack[-2] += stack[-1]
                stack.pop()
            else:
                output += stack.pop()
        else:
            if stack:
                stack[-1] += inputString[i]
            else:
                output += inputString[i]
    return output


# print(solution("a(bc)de"))  # "acbde"
print(solution("foo(bar(baz))blim"))


# best solution - using recursion, very clean and simple

# def solution(s):
#     for i in range(len(s)):
#         if s[i] == "(":
#             start = i
#         if s[i] == ")":
#             end = i
#             return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
#     return s

