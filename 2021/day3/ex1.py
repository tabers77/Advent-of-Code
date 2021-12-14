from collections import Counter

def open_file(path):

    with open(path) as file:
        data = file.readlines()
        data = [i.strip() for i in data]

    return data


def binaryToDecimal(binary):

    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return decimal


def wrapper_func(data):

    d = {}
    for i in range(len(data[0])):
        for x in data:
            d.setdefault(i, []).append(int(x[i]))
    d = {k: Counter(v) for k, v in d.items()}

    d1 = {}
    d2 = {}
    for row_n, v1 in d.items():
        for k2, v2 in v1.items():
            if v2 == max(v1.values()):
                d1[row_n] = k2
            elif v2 == min(v1.values()):
                d2[row_n] = k2
    dicts = [d1, d2]
    gamma_epsilon = list()
    for current_dict in dicts:
        binary_n = [str(i) for i in current_dict.values()]
        binary_n = int("".join(binary_n))
        gamma_epsilon.append(binaryToDecimal(binary_n))

    return gamma_epsilon[0] * gamma_epsilon[1]


data_sample = open_file('data_file')

print(wrapper_func(data_sample))