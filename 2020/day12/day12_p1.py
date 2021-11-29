
with open('input.txt') as f:
    data = f.readlines()
data = [i.strip() for i in data]

directions = [
    (0,1), # north
    (1,0), # east
    (0,-1), # south
    (-1,0), # west
]

def get_distance():
    """
    :return: Manhattan distance based on input
    """
    x, y = 0, 0
    ship_dir = (0, 1)

    for i in data:
        command = i[0]
        unit = int(i[1:])

        if command == 'N':
            y -= unit
        elif command == 'S':
            y += unit
        elif command == 'W':
            x -= unit
        elif command == 'E':
            x += unit
        elif command == 'L':
            # Here I will turn the ship 90 degrees
            turns = unit // 90
            ind = directions.index(ship_dir)
            ship_dir = directions[(ind - turns) % 4]
        elif command == 'R':
            turns = unit // 90
            ind = directions.index(ship_dir)
            ship_dir = directions[(ind + turns) % 4]
        elif command == 'F':
            x += unit * ship_dir[1]
            y += unit * ship_dir[0]

    manhattan_distance = abs(x) + abs(y)
    return manhattan_distance


if __name__ == '__main__':
    print(get_distance())






