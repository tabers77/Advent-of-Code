f = open('input.txt', 'r')
data = f.read().split('\n')
f.close()

bags = {}

for i in range(len(data)):
    bag, contains = data[i].split(' bags contain ')

    if ', ' not in contains:
        # If contains is equals to other bags put the bag with no values
        if contains == 'no other bags.':
            bags[bag] = {}
            continue
        else:
            contains = [contains]
    else:
        contains = contains.split(', ')

    content = {}
    for k in range(len(contains)):
        contains[k] = contains[k].split(' ')
        content[' '.join(contains[k][1:-1])] = int(contains[k][0])
    bags[bag] = content


def this_in_this(looking_for, looking_in):
    if looking_for in bags[looking_in].keys():
        return True

    for bag in bags[looking_in].keys():
        if this_in_this(looking_for, bag):
            return True

counter = 0

# if shiny gold in bags
for i in bags.keys():
    if this_in_this('shiny gold', i):
        counter += 1


if __name__ == '__main__':
    print(counter)
