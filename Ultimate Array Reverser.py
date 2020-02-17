def reverse(a):
    x = ''.join(a)
    xback = x[::-1]
    xbacklist =[]
    for i in a:
        xbacklist.append(xback[0:len(i)])
        xback = xback[len(i):]
    print(xbacklist)
    

reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"])
