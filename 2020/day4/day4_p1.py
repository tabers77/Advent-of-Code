file = open('input.txt','r')
container = file.read()
file.close()

container = [i.replace('\n',' ') for i in container.split('\n\n')]

lst = ['ecl','pid', 'byr','iyr','eyr','hgt','hcl']

counter = 0

for passport in container:
    valid = True
    for i in lst:
        if i not in passport:
            valid = False
    if valid:
        counter+=1

print(counter)
