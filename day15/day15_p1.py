with open('input.txt', 'r') as file:
    data = file.read()
    data = [int(n) for n in data.split(',') ]

def get_num_spoken(limit = 2020):
    d = {}
    for idx, num in enumerate(data):
        idx = idx + 1
        d[idx] = num
    unique_count = {}

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


if __name__ == '__main__':
    print(get_num_spoken())
