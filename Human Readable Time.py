def make_readable(seconds):
    hh = seconds//3600
    mm = (seconds%3600)//60 
    ss = seconds%60

    if len(str(int(hh)))== 1:
        hh = '0' + str(int(hh))
    else:
        hh = str(int(hh))

    if len(str(int(mm)))== 1:
        mm = '0' + str(int(mm))
    else:
        mm = str(int(mm))


    if len(str(int(ss)))== 1:
        ss = '0' + str(int(ss))
    else:
        ss = str(int(ss))
    
    return "{}:{}:{}".format(hh,mm,ss)

print(make_readable(3693))
