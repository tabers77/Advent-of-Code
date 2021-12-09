with open('day1_input_ex1') as file:

    data = file.read()
    data = [i for i in data.split()]


# ****** code 1 ******
count = 0
for i in range(len(data)-1):
    n1 = int(data[i])
    n2 = int(data[i+1])
    r = n2 - n1

    if r > 0:
        count += 1

# ****** code 2 ******
r = [int(data[i+1])-int(data[i]) for i in range(len(data)-1)]
r2 = len([i for i in r if i > 0])
