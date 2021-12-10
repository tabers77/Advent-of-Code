with open('ex1') as file:

    data = file.readlines()
    data = [i.split() for i in data]

horizontal = 0
depth = 0

for tup in data:
    if tup[0] == 'forward':
        horizontal += int(tup[1])
    elif tup[0] == 'down':
        depth += int(tup[1])
    elif tup[0] == 'up':
        depth -= int(tup[1])

answer = horizontal * depth

print(answer)
