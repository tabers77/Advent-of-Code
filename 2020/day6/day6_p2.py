f = open('input.txt', 'r')
data = [i.replace(' ', '').split('\n') for i in f.read().split('\n\n')]

counter = 0
print(data)

for block in data:
    for i in range(len(block[0])): # the length of the first character
        set1 = True
        for j in range(len(block)): # the length of the whole block
            #print(f'par1: {block[0][i]}')
            #print(f'par2: {block[j]}')
            if not block[0][i] in block[j]:
                set1 = False
        if set1:
            counter += 1
            #print(counter)

if __name__ == '__main__':
    print(counter)



