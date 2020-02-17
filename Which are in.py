def in_array(array1, array2):
    sendback = []
    for i in array2:
        for j in array1:
            if j in i:
                sendback.append(j)
    sendback = list(set(sendback))
    sendback.sort()
    return sendback

a1 = ["arp", "live", "strong","arp","cod","cody"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong","codyling"]
print(in_array(a1,a2))
