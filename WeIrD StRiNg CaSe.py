def to_weird_case(string):
    new = ''
    for i , j in zip(string[::2],string[1::2]):
        new += i.upper()+j.lower()
    
    if len(string)%2:
        new += string[-1].upper()

    return new
    


to_weird_case('this is a testa')
