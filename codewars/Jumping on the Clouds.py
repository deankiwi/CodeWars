def jumpingOnClouds(c):
    location = 0
    steps = 0
    length = len(c)-1
    
    while True:
        if c[location+2] ==0:
            steps += 1
            location +=2
            if location + 2 > length:
                breakpoint()
                if location == length:
                    return steps
                else:
                    return steps +1
        else:
            location +=1
            steps += 1
        
        


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
