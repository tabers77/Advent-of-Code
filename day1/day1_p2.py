import itertools

with open('input.txt') as file:
    file = file.readlines()
    data = [int(num) for num in file]


combinations = itertools.permutations(data,3)

ans = set(comb[0] * comb[1] * comb[2] for comb in combinations if sum(comb) == 2020)

print(ans)

