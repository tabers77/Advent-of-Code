with open('day1_input_ex1') as file:

    data = file.read()
    data = [int(i) for i in data.split()]

window_size = 3

lst = [sum(data[i: i + window_size]) for i in range(0, len(data))]

lst2 = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
ans = len([i for i in lst2 if i > 0])

print(ans)