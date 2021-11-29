with open('input.txt') as f:
    data = f.readlines()
data = [i.strip() for i in data]


def get_distance():
    """
    :return: Manhattan distance with rotations based on input
    """
    weight_y = 1
    weight_x = 10

    x, y = 0, 0
    #ship_dir = (0, 1)

    for i in data:
        command = i[0]
        unit = int(i[1:])

        if command == 'N':
            weight_y += unit
        elif command == 'S':
            weight_y -= unit
        elif command == 'W':
            weight_x -= unit
        elif command == 'E':
            weight_x += unit

        elif command == 'L':
            # Here I will turn the ship 90 degrees
            turns = unit // 90
            for i in range(turns):
                weight_y, weight_x = weight_x, weight_y # we rotate
                weight_x *= -1
        elif command == 'R':
            turns = unit // 90
            for i in range(turns):
                weight_y, weight_x = weight_x, weight_y # we rotate
                weight_y *= -1
        elif command == 'F':
            y += unit * weight_y
            x += unit * weight_x

    manhattan_distance = abs(x) + abs(y)
    return manhattan_distance


if __name__ == '__main__':
    print(get_distance())
