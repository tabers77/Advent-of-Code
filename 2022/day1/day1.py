with open('day1_input') as file:
    data = file.read()
    data = [i for i in data.split('\n')]

m = []
tot = 0

for i in data:
    if i != '':
        tot += int(i)
    else:
        m.append(tot)
        tot = 0
        continue

sorted_list = sorted(m, reverse=True)
print(sum(sorted_list[:3]))


