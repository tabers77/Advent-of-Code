def open_file(path):

    with open(path) as file:
        data = file.readlines()
        data = [i.split() for i in data]

    return data


def get_answer(data, exercise_n):

    horizontal = 0
    depth = 0
    aim = 0

    for tup in data:

        if tup[0] == 'forward':
            horizontal += int(tup[1])
            if aim != 0:
                depth += int(tup[1]) * aim if exercise_n == 2 else 0

        elif tup[0] == 'down':
            depth += int(tup[1]) if exercise_n == 1 else 0
            aim += int(tup[1])

        elif tup[0] == 'up':
            depth -= int(tup[1]) if exercise_n == 1 else 0
            aim -= int(tup[1])

    answer = horizontal * depth

    return answer


data = open_file('ex1')

ans = get_answer(data=data, exercise_n=2)

print(ans)









