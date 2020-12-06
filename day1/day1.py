import itertools

lst = []

while True:
    a = input()
    if not a:
        break
    lst.append(int(a))

combinations = itertools.permutations(lst,2)

# If I don't use sets I will see 2 results 
ans = set(comb[0] * comb[1] for comb in combinations if sum(comb) == 2020)

print(ans)
