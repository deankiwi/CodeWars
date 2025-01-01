raw = "125 17"
raw = "41078 18 7 0 4785508 535256 8154 447"
nums = raw.split(" ")
print(nums)


def helper(num: str, depth, memo=None):
    if memo is None:
        memo = {}


    if (num, depth) in memo:
        return memo[(num, depth)]


    if depth == 0:
        result = 1
    elif num == "0":
        result = helper("1", depth - 1, memo)
    elif len(num) % 2 == 0:
        stone1 = num[: len(num) // 2]
        stone2 = num[len(num) // 2 :]
        stone2 = str(int(stone2))  
        result = helper(stone1, depth - 1, memo) + helper(stone2, depth - 1, memo)
    else:
        result = helper(str(int(num) * 2024), depth - 1, memo)

    # Store the result in the memo dictionary
    memo[(num, depth)] = result

    return result


total = 0
for num in nums:
    total += helper(num, 75)


print(f"{total = }")
