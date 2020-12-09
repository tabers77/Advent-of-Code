# 1 divide spaces
file = open('input.txt', 'r')
data = [i.replace(' ','').replace('\n','') for i in file.read().split('\n\n')]
data = [i for i in data]

# 2 count uniques and sum
ans = [len(set(i)) for i in data]
#print(data)
print(sum(ans))
