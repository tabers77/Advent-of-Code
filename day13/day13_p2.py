with open('input.txt') as file:
    data = file.readlines()
    data = [i.strip() for i in data]
    data[1] = data[1].split(',')

def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1

def get_earlist_time():
    ids = []
    f_product = 1
    for i in range(len(data[1])):
        block = data[1][i]
        if block != 'x':# skip the x as usual
            k = int(block)# block as int
            i = i % k
            ids.append(((k-i)%k,k))
            f_product *= k
    total = 0
    for i, k in ids:
        p_product = f_product // k
        inverse = modInverse(p_product,k)
        assert (inverse * p_product) % k == 1
        term = inverse * p_product * i
        total += term
    return total % f_product


if __name__ == '__main__':
    print(get_earlist_time())

####Resources####
#Chinese Remainder Theorem: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
#Modular Inverse: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
