def max_rot(n):
    nstr = str(n)
    numbers = [n]
    
    for i in range(len(nstr)-1):
        nstr = nstr[:i]+nstr[i+1:] + nstr[i]
        numbers.append(int(nstr))
    print(numbers)
    nstr = str(n)
    numbers = [n]
    for i in range(len(nstr)):
        nstr = nstr[:i]+nstr[i+1:] + nstr[i]
        numbers.append(int(nstr))
    print(numbers)
    return max(numbers)

max_rot(56789)
