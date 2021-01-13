#PART 2
import re

# 1 Read the file
with open('input.txt') as file:
    file = file.readlines()
    data = [char.strip('\n') for char in file]

# 2  Count the valids
valids = 0
for i in data:
    i = re.split('-| |:', i )
    i.pop(3) 
    a = int(i[0]) - 1 # normalize
    b = int(i[1]) - 1 # normalize
    letter_to_check = i[2]
    sample = [i for i in i[3]]

    if sample[a] == letter_to_check and sample[b] != letter_to_check:
        valids += 1
    if sample[b] == letter_to_check and sample[a] != letter_to_check:
        valids += 1

print(valids)

