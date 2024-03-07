def solve(n):
    numbers = [10,20,50,100,200,500]
    amount = 0
    left = n
    
    for i in numbers[::-1]:
       
        if left - i >= 0:
            
            amount += left//i
            left -= (left//i)*i
            
    if left == 0:
        return amount
    return -1

print(solve(550))
