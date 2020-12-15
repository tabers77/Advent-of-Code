with open('input.txt') as file:
    data = file.readlines()
    data = [int(line.strip()) for line in data]
    data.sort()

# append the max of the last number
data.append(max(data) + 3)

def get_differ():
    # calculate the difference
    jolt1 = 0
    jolt3 = 0

    for i in range(len(data)-1):
        print(data[i+1])
        diff = data[i+1] - data[i]
        if diff == 1:
            jolt1 += 1
        elif diff == 3:
            jolt3 += 1

    jolt1 = jolt1 + 1
    ans = jolt1 * jolt3

    return ans

d = { }

def get_combinations(pos):

    if pos == len(data) - 1:
        return 1

    if pos in d.values():
        return d[pos]

    total = 0

    for i in range(pos+1, len(data)):
        if (data[i] - data[pos]) <= 3:
            total += get_combinations(i)
    d[pos] = total

    return total


print(get_combinations(0))


