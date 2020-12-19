with open('input.txt') as file:
    data = file.readlines()
    data = [i.strip() for i in data]


def get_time():
    minimum = 1000000000000000
    low_id = 0
    dep_time = int(data[0])
    buses = [int(i) for i in data[1].split(',') if i != 'x']
    for bus_id in buses:
        id_multiple = dep_time // bus_id # divide the departure time in chunks of bus id

        diff = bus_id * (id_multiple + 1 ) - dep_time
        if diff < minimum:
            minimum = diff
            low_id = bus_id

    return low_id * minimum

if __name__ == '__main__':
    print(get_time())
