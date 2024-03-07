def find_divisors(num):
    div_list = []
    for i in range(1,num//2+1):
        if not num%i:
            div_list.append(i)
    div_list.append(num)
    return div_list

def squ_roots(num):
    x = num
    y= (x+1) // 2
    while y < x:
        x = y
        y = (x + num // x) // 2
    return x

def list_squared(m,n):
    squlist = []
    for i in range(m,n+1):
        div = find_divisors(i)
        divsqu = [x**2 for x in div]
        sumsqu = sum(divsqu)
        #print(i)
        #print(divsqu)
        #print(sumsqu)
        #print(squ_roots(sumsqu)**2)
        if squ_roots(sumsqu)**2 == sumsqu:
            squlist.append([i,sumsqu])
    return squlist

print(list_squared(1,250))
