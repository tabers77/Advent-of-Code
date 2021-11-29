with open('input10.txt') as file:
    data = file.readlines()
    data = [int(line.strip()) for line in data]
    data.sort()

# append the max of the last number
data.append(max(data) + 3)

def get_differ():
    # calculate the difference
    jolt1 = 0
    jolt3 = 0

    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        if diff == 1:
            jolt1 += 1
        elif diff == 3:
            jolt3 += 1
            
    jolt1 = jolt1+1
    ans = jolt1 * jolt3
    
    print(f'Jolt 1 diff: {jolt1}')
    print(f'Jolt 3 diff: {jolt3}')
    print(f'Answer: {ans}')


if __name__ == '__main__':
    get_differ()
