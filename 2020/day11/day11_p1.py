f = open('input.txt', 'r')
seats = f.read().split('\n')
f.close()

adjust = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]


def switch_seats():
    """
    :return: all new seats
    """
    # create blank spaces

    new_seats = [['.' for j in range(len(seats[0]))] for i in range(len(seats))]

    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == 'L':
                has_neighbours = False
                for i in range(8):
                    if -1 < y + adjust[i][1] < len(seats) and -1 < x + adjust[i][0] < len(seats[0]) and \
                            seats[y + adjust[i][1]][x + adjust[i][0]] == '#':
                        has_neighbours = True
                        break
                if not has_neighbours:
                    new_seats[y][x] = '#'
                else:
                    new_seats[y][x] = 'L'
            elif seats[y][x] == '#':
                neighbours_counter = 0
                for i in range(8):
                    if -1 < y + adjust[i][1] < len(seats) and -1 < x + adjust[i][0] < len(seats[0]) and \
                            seats[y + adjust[i][1]][x + adjust[i][0]] == '#':
                        neighbours_counter += 1
                if neighbours_counter >= 4:
                    new_seats[y][x] = 'L'
                else:
                    new_seats[y][x] = '#'
    return new_seats


while True:
    new_seats = switch_seats()
    if seats == new_seats:
        break

    seats = new_seats

occupied = 0
for y in range(len(seats)):
    for x in range(len(seats[0])):
        if seats[y][x] == '#':
            occupied += 1

print(occupied)
