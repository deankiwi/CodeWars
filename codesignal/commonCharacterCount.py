def solution(s1, s2):
    count = 0
    for letter in s1:
        if letter in s2:
            s2 = s2.replace(letter, "", 1)
            count += 1
    return count


print(solution("aabcc", "adcaa"))  # 3

# best solution - here they work out all unique letters in s1 and then count the minimum of each letter in s1 and s2, and store in a list, then return simple sum of the list

# def solution(s1, s2):
#     com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
#     return sum(com)
