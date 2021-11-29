file = open('input.txt','r')
container = file.read()
file.close()

container = [i.replace('\n',' ') for i in container.split('\n\n')]

import re

def validation_values(d):
    count = 0
    # con1
    if 'byr' in d.keys():
        if int(d['byr']) >= 1920 and int(d['byr']) <= 2002:
            count += 1
    # con2
    if 'iyr' in d.keys():
        if int(d['iyr']) >= 2010 and int(d['iyr']) <= 2020:
            count += 1
    # con3
    if 'eyr' in d.keys():
        if int(d['eyr']) >= 2020 and int(d['eyr']) <= 2030:
            count += 1
    # con4
    if 'hgt' in d.keys():
        if 'cm' in d['hgt']:
            if int(d['hgt'].strip('cm')) >= 150 and int(d['hgt'].strip('cm')) <= 193:
                count += 1

        elif 'in' in d['hgt']:
            if int(d['hgt'].strip('in')) >= 59 and int(d['hgt'].strip('in')) <= 76:
                count += 1
    # con5
    if 'hcl' in d.keys():
        if '#' in d['hcl'] and len(d['hcl']) == 7:
            set1 = False
            for i in d['hcl']:
                if i in '01234567890abcdef':
                    set1 = True
            if set1:
                count += 1
    # con6
    if 'ecl' in d.keys():
        ecl = 'amb blu brn gry grn hzl oth'.split()
        for i in ecl:
            if i in d['ecl']:
                count += 1
    # # con7
    if 'pid' in d.keys():
        if len(d['pid']) == 9:
            count += 1

    if count == 7:
        return True
    else:
        return False


lst = ['ecl','pid', 'byr','iyr','eyr','hgt','hcl']

counter = 0
for passport in container:
    a = re.split(':| ', passport)
    res_dct = {a[i]: a[i + 1] for i in range(0, len(a), 2)}

    valid = True
    for i in lst:
        if i not in passport:
            valid = False
    if valid and validation_values(res_dct):
        counter+=1
print(counter)
