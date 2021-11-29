def transform_data(s):
    row = [0, 127]
    col = [0, 7]

    for i in range(7):
        if s[i] == 'F':
            row[1] = (row[1]+row[0])//2
        elif s[i] == 'B':
            row[0] = (row[1]+row[0])//2

    for i in range(6,10):
        if s[i] == 'L':
            col[1] = (col[1] + col[0])//2
        elif s[i] == 'R':
            col[0] = (col[1] + col[0])//2

    return (col[1], row[1])


file = open('input.txt', 'r')
data = file.read().split('\n')
file.close()

lst = []

for i in range(len(data)):
    position = transform_data(data[i])
    seatID = position[1] * 8 + position [0]
    lst.append(seatID)

for i in range(min(lst), max(lst)):
    if i not in lst:
        print(i)
