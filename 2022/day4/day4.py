with open('day4_input') as file:
    data = file.read()
    data = [i for i in data.split('\n')]

# [' 18-83', '18-18']
# [' 18-83', '16-18']
# store min , compare
# store mac , compare
n_overlaps = 0
for sample in data:

    count = 0
    sorted_sample = sample.split(',') #sorted(sample.split(','))
    # --------------------------------
    first_min, first_max = int(sorted_sample[0].split('-')[0]), int(sorted_sample[0].split('-')[1])
    second_min, second_max = int(sorted_sample[1].split('-')[0]), int(sorted_sample[1].split('-')[1])

    min_ = min(first_min, second_min)
    max_ = max(first_max, second_max)
    # COND 1
    if first_min <= second_min and first_max >= second_max:
        n_overlaps += 1
    # COND 2
    elif second_min <= first_min and second_max >= first_max:
        n_overlaps += 1

# -------
# PART 2
# -------
n_overlaps = 0
for sample in data:

    count = 0
    sorted_sample = sample.split(',') #sorted(sample.split(','))
    # --------------------------------
    first_min, first_max = int(sorted_sample[0].split('-')[0]), int(sorted_sample[0].split('-')[1])
    second_min, second_max = int(sorted_sample[1].split('-')[0]), int(sorted_sample[1].split('-')[1])

    min_ = min(first_min, second_min)
    max_ = max(first_max, second_max)
    # COND 1
    if first_min <= second_min and first_max >= second_max:
        n_overlaps += 1
    # COND 2
    elif second_min <= first_min and second_max >= first_max:
        n_overlaps += 1

    elif second_min >= first_min and second_min <= first_max :
        n_overlaps += 1

    elif first_min <= second_min and second_min <= first_max:
        n_overlaps += 1
    elif first_min >= second_min and first_min <= second_max:
        n_overlaps += 1

    else:
        print(sorted_sample)

print(n_overlaps)



# 23 - 71
  # 49 -   72

  # 49 -   72
# 23 -   71

