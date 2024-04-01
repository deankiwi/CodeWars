

def solution(N):
    # print(str(bin(N))[2:])
    # Implement your solution here
    max = 0
    count = 0
    start = False
    for i in str(bin(N))[2:]:
        # print(i)
        if i == "1" and not start:
            # print('start')

            start = True

        elif i == "1" and start:
            # print('stop')
            if count > max:
                max = count
            count = 0
        if i == "0" and start:
            # print('count')

            count += 1
    return max


print(solution(1041))  # 5
print(solution(6))  # 0
print(solution(328))  # 0
print(solution(1610612737))  # 28
print(solution(805306373))  # 25

