def score(dice):
    score = 0
    for i in range(1,7):
        numi = dice.count(i)
        if numi >= 3:
            score += greedthree(i)

            if numi >= 4:
                score += greedone(i) * (numi - 3)
        elif numi >= 1:
            
            score += greedone(i) * numi
    return score
            
def greedthree(n):
    if n == 1:
        return 1000
    if n == 6:
        return 600
    if n == 5:
        return 500
    if n == 4:
        return 400
    if n ==3:
        return 300
    if n == 2:
        return 200

def greedone(n):
    if n == 1:
        return 100
    if n == 5:
        return 50
    else:
        return 0


print(score([4, 4, 4, 3, 3]))
