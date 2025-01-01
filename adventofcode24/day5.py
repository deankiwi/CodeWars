from collections import defaultdict
import re


with open("./data/day5.txt") as data:
    orderRules, allTasks = data.read().split("\n\n")
    # print(orderRules.split("\n"))
    order = defaultdict(list)
    patten = r"(\d+)\|(\d+)"

    # print(orderRules)
    for x, y in re.findall(patten, orderRules):
        order[x].append(y)
        # print(x, y)
    # print(order)
    tasks = [i.split(",") for i in allTasks.split("\n")]
    # print(tasks)
total = 0
# print(order)
notOrdered = []
for task in tasks:
    # print(task)
    seen = set()
    failed = False
    for num in task:
        # print(num)
        if num in order:
            for numLaw in order[num]:
                if numLaw in seen:
                    notOrdered.append(task)
                    failed = True
                    break
        if failed:
            break
        seen.add(num)
    else:
        total += int(task[len(task) // 2])

print(f"{total = }")
# print(notOrdered[:])

total = 0

for task in notOrdered:
    failed = True

    while failed:
        tryAgain = False
        seen = set()
        for i, num in enumerate(task):
            # print(num)
            if num in order:
                for numLaw in order[num]:
                    if numLaw in seen:

                        task[i], task[i - 1] = task[i - 1], task[i]

                        tryAgain = True
                        break

            # print('wdwad')
            if tryAgain:
                break
            seen.add(num)
        else:
            total += int(task[len(task) // 2])

            failed = False

print(f"{total = }")
