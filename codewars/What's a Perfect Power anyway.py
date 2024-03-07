from math import log

def isPP(n):
    for i in range(2,n):
        #breakpoint()
        if (log(n,i)).is_integer():
            return [i,int(log(n,i))]


print(isPP(4))
