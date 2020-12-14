with open('input.txt','r') as f:
    data = f.readlines()
    data = [int(i.strip()) for i in data]

split = 25
def get_preamble_num():
    for i in range(split , len(data)): # start from the 25
        preamble = data[i-split:i] # here we print chunks of 25
        #print(preamble)
        num = data[i] # all numbers starting from 25
        found = False

        for j in range(split-1): # starting from 24
            for k in range(j+1,split):
                if preamble[j] + preamble[k] == num:
                    found = True
                    break
            if found:
                break
        if found == True:
            continue
        return num

print(get_preamble_num())
