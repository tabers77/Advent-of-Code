# part 2

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
            locBin = list(to_binary(loc))

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
