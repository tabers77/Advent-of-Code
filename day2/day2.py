import re
# 1 append to container
container = []
while True:
    i = input()
    if not i:
        break
    container.append(i)

# 2  Count the valids
valid = 0
for i in container:
    i = re.split('-| |:' , i )
    i.pop(3) # here I just drop 
    min_value = int(i[0])
    max_value = int(i[1])
    letter = i[2]
    sample = [i for i in i[3]]

    d = {i:sample.count(i) for i in sample}

    value = 0

    if letter in d.keys():
        value += d[letter]
    else:
        value = 0

    if value >= min_value and value <= max_value:
        valid += 1

print(valid)
