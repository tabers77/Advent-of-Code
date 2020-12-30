from time import time

with open('input.txt', 'r') as file:
    data= file.read()
    data = [int(n) for n in data.split(',')]

def timer(fn):
    def wrapper(n):
        t1 = time()
        function = fn(n)
        t2 = time()
        print(f'It took {t2 - t1} to run')
        return function
    return wrapper

@timer
def play_memory_game(size):
    mem = {}

    for i in range(len(data)-1):
        num = data[i]
        mem[num] = i

    for i in range(len(data)-1,size-1):
        num = data[i]

        if num not in mem:
            data.append(0)
            mem[num] = i

        else:
            j = mem[num]
            newNum = i - j
            data.append(newNum)
            mem[num] = i

    return data[-1]

@timer
def get_num_spoken(limit=2020):
    d = {}
    unique_count = {}

    for idx, num in enumerate(data):
        idx = idx + 1
        d[idx] = num

    while max(d.keys()) < limit:
        numbers = list(d.values())
        last_num = list(d.values())[-1]

        for number in numbers:
            unique_count[number] = numbers.count(number)

        if unique_count[last_num] == 1:
            d[int(list(d.keys())[-1]) + 1] = 0

        elif last_num == numbers[-2]:
            d[int(list(d.keys())[-1]) + 1] = 1

        else:
            lst = []
            for k, v in d.items():
                if last_num == v:
                    lst.append(k)

            calc_value = lst[-1] - lst[-2]

            d[int(list(d.keys())[-1]) + 1] = calc_value

    ans = list(d.values())[-1]

    return ans

# Comparing how fast the functions are 

print(play_memory_game(30000000))
print(get_num_spoken(30000000))
