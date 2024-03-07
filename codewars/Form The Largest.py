def max_number(n):
    return int(''.join(sorted(str(n), reverse = True)))



print(max_number('213'))
