def is_merge(s, part1, part2):
    for i in s:
        if i == part1[0]:
            if len(part1) > 1:
                part1 = part1[1:]
        elif i == part2[0]:
            if len(part2) > 1:
                part2 = part2[1:]
        else:
            return False
    return True


print(is_merge('codewars', 'code', 'wars'))
