f = open('input.txt', 'r')
data = f.read().split('\n')
f.close()

bags = {}

for i in range(len(data)):
    bag, contains = data[i].split(' bags contain ') 
    if ', ' not in contains: # else I split 
        # If contains is equals to other bags put the bag with no values
        if contains == 'no other bags.': # If there are no other bags I will return 0 
            bags[bag] = {}
            continue
        else:
            contains = [contains] # I just put contains on a list 
    else:
        contains = contains.split(', ')

    content = {}
    for k in range(len(contains)):
        contains[k] = contains[k].split(' ') # I split every element 
        content[' '.join(contains[k][1:-1])] = int(contains[k][0]) # first character as value 
    bags[bag] = content

counter = 0
def rec_function (looking_in, multiplier = 1):
    global counter # use global when we want toa assign a variable to an outer scope since we have counter outside the function
    for bag in bags[looking_in].keys():
        counter += bags[looking_in][bag]*multiplier

        rec_function (bag, multiplier*bags[looking_in][bag])

rec_function ('shiny gold')

if __name__ == '__main__':
    print(counter)
