import string

with open('day3_input') as file:
    data = file.read()
    data = [i for i in data.split('\n')]

word_bank = string.ascii_lowercase

lower_case_points = {word_bank[i]: i + 1 for i in range(len(word_bank))}
upper_case_points = {word_bank[i].upper(): i + 27 for i in range(len(word_bank))}

# device string
# convert to set
# fin common letter
# get points from hashmap

total_points = 0

for rs in data:
    mid = int(len(rs) / 2)

    lower = set(rs[:mid])
    upper = set(rs[mid:])

    common_letter = list(lower & upper)[0]

    try:
        total_points += upper_case_points[common_letter]
    except KeyError:
        total_points += lower_case_points[common_letter]

# print(total_points)

# --------
# PART 2
# --------

total_points2 = 0
lst = list()
a = 0
for i in range(int(len(data) / 3)):
    a = max(a, i)
    b = a + 3
    samp = data[a:b]
    common_char = list(set(samp[0]) & set(samp[1]) & set(samp[2]))[0]
    try:
        total_points2 += upper_case_points[common_char]
    except KeyError:
        total_points2 += lower_case_points[common_char]

    a = a + 3

print(total_points2)
