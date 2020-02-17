'''def find_it(seq):
    for i in seq:
        if seq.count(i)%2: return i'''

def find_it(seq):
    for i in seq:
        count = 0
        for j in seq:
            if j == i:
                count +=1
        if count%2:
            return i

x = find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
