with open('day6_input') as f:
    data = f.read()
    data = [i for i in data]

a = 0
converged = False
res = 0
count = 0
while not converged:

    b = a + 3
    c = b + 1
    c1 = data[a:b]
    if b == 3:
        add = data[b:c][0]
        c1.append(add)
    # check
    if b == 3:
        if len(set(c1)) != 4:
            a = b
        else:
            res = c
            converged = True
    else:
        if len(set(c1)) != 3:
            a = b
        else:
            res = c
            converged = True
    count+=1

print(res)
print(count)


# for i in data:
#     print(i)


