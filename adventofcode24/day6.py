example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

with open("./data/day6.txt", "r") as file:
    text = file.read()


data = text.split("\n")
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
move = moves[dir]

for i in range(len(data)):
    if "^" in data[i]:
        curr = [i, data[i].find("^")]  # y , x
        break

seen = set()
count = 0

print(seen)
print(len(seen))

length = len(data)
width = len(data[0])

while 0 <= curr[0] < length and 0 <= curr[1] < width:
    # print(f"{curr = }")
    if data[curr[0]][curr[1]] == "#":

        curr[0] -= move[0]
        curr[1] -= move[1]
        dir = (dir + 1) % 4
        move = moves[dir]

        # go back, turn right
    else:
        if tuple(curr) not in seen:
            seen.add(tuple(curr))
            count += 1
    curr[0] += move[0]
    curr[1] += move[1]

print(f"{count = }")
