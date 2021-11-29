with open('input.txt') as file:
    data = file.readlines()
    data = [row.strip() for row in data]

def get_binary(num: int):
    bits = []
    while num != 0:
        bits.append(str(num%2))
        num = num // 2
    bits.reverse()
    s = ''.join(bits)

    while len(s) !=36 :
        s = '0' + s
    return s


def to_decimal(b):

    while b[0] == '0':
        b = b[1:]

    dec = 0
    for i in range(len(b)):
        j = len(b) - i - 1
        dec += int(b[j]) * (2**i)

    return dec


def get_m_total(data):
    d = {}
    mask = ''
    for line in data:
        line = line.split(' = ')
        if 'mask' in line[0]:
            mask = line[1]
        else:
            loc = line[0][4:-1]
            value = int(line[1])
            value_binary = list(get_binary(value))
            for i in range(len(mask)):
                if mask[i] != 'X':
                    value_binary[i] = mask[i]
            masked_str = ''
            masked_str = masked_str.join(value_binary)
            masked_num = to_decimal(masked_str)
            d[loc] = masked_num
    ans = 0

    for i in d.values():
        ans += i
    return ans


if __name__ == '__main__':
    print(get_m_total(data))
