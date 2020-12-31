import re
import itertools

with open('input.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

fields, tickets = [], []

for line in data:
    if 'or' in line:
        fields.append(line)
    elif ',' in line:
        tickets.append(line.split(','))


def get_ranges (a,b,c,d):
    output = []
    for i in range(a,b+1):
        output.append(i)
    for i in range(c,d+1):
        output.append(i)
    return output


def get_error_rate():
    sequences = []
    for row in fields:
        char = re.split('-|or|:', row)
        if char[1] == 'm':
            continue
        sequences.append(get_ranges(int(char[1]), int(char[2]), int(char[3]), int(char[4])))

    sequences_comb = list(itertools.chain.from_iterable(sequences))  # combine separate sequences

    error_rate_count = 0
    for row in tickets[1:]:
        for num in row:
            num = int(num)
            if num not in sequences_comb:
                error_rate_count += num

    return error_rate_count


if '__main__' == __name__:

    print(get_error_rate())
