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

def get_addresses(s):
    if 'X' not in s:
        return s

    addresses = ''
    xi = s.index('X')
    s0 = s[:xi] + '0' + s[xi+1:]
    s1 = s[:xi] + '1' + s[xi+1:]

    addresses += get_addresses(s0) + ','
    addresses += get_addresses(s1)

    return addresses

def address_mask_total():
    mem = {}
    mask = ''

    for line in data:
        line = line.split(' = ')

        if 'mask' in line[0]:
            mask = line[1]

        else:
            val = int(line[1])

            loc = int(line[0][4:-1])
            locBin = list(get_binary(loc))

            # apply mask
            for i in range(len(mask)):
                if mask[i] != '0':
                    locBin[i] = mask[i]

            maskedLoc = ''
            maskedLoc = maskedLoc.join(locBin)
            addresses = get_addresses(maskedLoc).split(',')

            for address in addresses:
                mem[address] = val

    total = 0
    for i in mem.values():
        total += i
    return total


print(address_mask_total())
