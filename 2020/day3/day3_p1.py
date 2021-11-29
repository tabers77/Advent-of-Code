container = []

while True:
    a = input()
    if not a:
        break
    container.append(a)

counter = 0

for i in range(1,len(container)):
    """
    1. Loop through the container
    2. 
    """

    if container[i][(i*3)%len(container[0])]=='#':
        counter += 1

print(counter)
