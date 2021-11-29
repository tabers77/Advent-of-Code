with open('input.txt','r') as f:
    data = f.readlines()
    data = [i.strip() for i in data]

def acummulator():
    # Define parameters:
    acc = 0
    line = 0
    lst = []
    while line not in lst:
        lst.append(line)
        current = data[line] #first character
        current = current.split() # list to divide the 2 parameters
        # Define param and num
        param = current[0]
        num = current[1]
        if '+' in num:
            num = int(num[1:]) # remove the plus sign
        else:
            num = int(num) # observe that the negative number will in fact be treated as negative
        if param == 'acc':
            acc += num
            line +=1 # I increment the line to choose second character and so on
        elif param == 'jmp':
            line += num # I will jump the number of characters that there is in number
        elif param == 'nop':
            line += 1 # I just go to the next line
    return acc


if __name__ == '__main__':
    answer = acummulator()
    print(answer)
