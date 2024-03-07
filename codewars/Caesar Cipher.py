import string

def caesar(message, shift):
    alpa = string.ascii_lowercase
    alpalen = len(alpa)
    newmessage = ''
    nums = '123456789'

    for i in message:
        if i in alpa:
            newmessage += alpa[(alpa.find(i)+shift)%alpalen]
        elif i in nums:
            shift += int(i)
            newmessage += i
        else:
            newmessage +=i

    
    return newmessage


print(caesar('he2l9lo wo1rld',3))
