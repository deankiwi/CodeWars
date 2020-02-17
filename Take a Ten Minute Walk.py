def isValidWalk(walk):

    if len(walk) !=10 :
        return False

    
    if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
        return True

    else:
        return False

    return False

print(isValidWalk(['n','n']))
