container = []

while True:
    a = input()
    if not a:
        break
    container.append(a)

out1 = 0
out2 = 0
out3 = 0
out4 = 0
out5 = 0

for i in range(1,len(container)):

    if container[i][(i*1)%len(container[0])]=='#':
        out1 += 1

    if container[i][(i * 3) % len(container[0])] == '#':
        out2 += 1

    if container[i][(i * 5) % len(container[0])] == '#':
        out3 += 1

    if container[i][(i * 7) % len(container[0])] == '#':
        out4 += 1

    if i % 2 != 0:
        if container[i][(i * 1) % len(container[0])] == '#':
            out5 += 1

agg = out1 * out2 * out3 * out4 * out5

print(agg)
