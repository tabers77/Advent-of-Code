f = open('input.txt', 'r')
seats = f.read().split('\n')
f.close()

adjust = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

print(len(seats))

def switch_seats():
    new_seats = [['.' for j in range(len(seats[0]))] for i in range(len(seats))]

    for y in range(len(seats)): # 99 rows
        for x in range(len(seats[0])): # x will loop for a seat for every seat on a row 92
            if seats[y][x] == 'L': # check the first space/seat
                has_neighbours = False
                for i in range(8): # for every character I will loop through adjust
                    k = 1
                    while -1 < y + adjust[i][1] * k < len(seats) and -1 < x + adjust[i][0] * k < len(seats[0]):
                        if seats[y + adjust[i][1] * k][x + adjust[i][0] * k] == '#':
                            has_neighbours = True
                            break
                        if seats[y + adjust[i][1] * k][x + adjust[i][0] * k] == 'L':
                            break
                        k += 1
                    if has_neighbours:
                        break
                if not has_neighbours:
                    new_seats[y][x] = '#'
                else:
                    new_seats[y][x] = 'L'

            elif seats[y][x] == '#':
                neighbours_counter = 0
                for i in range(8):
                    k = 1
                    while -1 < y + adjust[i][1] * k < len(seats) and -1 < x + adjust[i][0] * k < len(seats[0]):
                        if seats[y + adjust[i][1] * k][x + adjust[i][0] * k] == '#':
                            neighbours_counter += 1
                            break
                        if seats[y + adjust[i][1] * k][x + adjust[i][0] * k] == 'L':
                            break
                        k += 1

                if neighbours_counter >= 5:
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

# print('\n'.join([''.join(seats[i]) for i in range(len(seats))]))

print(occupied)
