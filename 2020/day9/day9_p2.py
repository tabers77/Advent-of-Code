with open('input.txt','r') as f:
    data = f.readlines()
    data = [int(i.strip()) for i in data]


def get_preamble_num(split = 25):
    for i in range(split , len(data)): # start from the 25
        preamble = data[i-split:i] # here we print chunks of 25

        num = data[i] # all numbers staring from 25
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

def get_bad_number():
    bad_num = get_preamble_num()
    found = False
    for i in range(len(data) -1):
        nums = [data[i]]
        for j in range(i + 1, len(data)):
            nums.append(data[j])
            if sum(nums) == bad_num:
                found = True
                break
            elif sum(nums) > bad_num:
                break
        if found == True:
            break
    return min(nums) + max(nums)

print(get_bad_number())
