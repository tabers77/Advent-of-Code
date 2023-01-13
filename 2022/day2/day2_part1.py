# 1. Choose the winning element
# 2. record if I won or lost


# element that won

# rock = A, X
# paper = B , Y
# scissors = C , Z

# rock < paper = paper ---> letter
# rock > sisors = rock ----> letter
# paper < sisior = sisors ---> letter


with open('day2_input') as file:
    data = file.read()
    data = [i for i in data.split('\n')]

hash_map_one = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
hash_map_two = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}


def logic(a_value, b_value):
    if hash_map_one[a_value] == 'rock' and hash_map_two[b_value] == 'paper':
        return b_value, hash_map_two[b_value]

    elif hash_map_one[a_value] == 'rock' and hash_map_two[b_value] == 'scissors':
        return a_value, hash_map_two[b_value]

    elif hash_map_one[a_value] == 'paper' and hash_map_two[b_value] == 'scissors':
        return b_value, hash_map_two[b_value]

    elif hash_map_one[a_value] == 'paper' and hash_map_two[b_value] == 'scissors':
        return b_value, hash_map_two[b_value]

    elif hash_map_two[b_value] == 'rock' and hash_map_one[a_value] == 'paper':
        return a_value, hash_map_two[b_value]

    elif hash_map_two[b_value] == 'rock' and hash_map_one[a_value] == 'scissors':
        return b_value, hash_map_two[b_value]

    elif hash_map_two[b_value] == 'paper' and hash_map_one[a_value] == 'scissors':
        return a_value, hash_map_two[b_value]

    elif hash_map_two[b_value] == 'paper' and hash_map_one[a_value] == 'scissors':
        return a_value, hash_map_two[b_value]
    else:
        return 'tie', hash_map_two[b_value]


point_map = {'rock': 1, 'paper': 2, 'scissors': 3}


# total score is sum of score of each round
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
def re_write_b_value(a_value, b_value):
    if b_value == 'Z':
        if hash_map_one[a_value] == 'rock':
            return 'Y'
        elif hash_map_one[a_value] == 'paper':
            return 'Z'
        elif hash_map_one[a_value] == 'scissors':
            return 'X'

    elif b_value == 'X':
        if hash_map_one[a_value] == 'rock':
            return 'Z'
        elif hash_map_one[a_value] == 'paper':
            return 'X'
        elif hash_map_one[a_value] == 'scissors':
            return 'Y'
    else:
        if hash_map_one[a_value] == 'rock':
            return 'X'
        elif hash_map_one[a_value] == 'paper':
            return 'Y'
        elif hash_map_one[a_value] == 'scissors':
            return 'Z'


def get_answer(rewrite_b_value=False):
    player1_points = 0

    for pair in data:
        b_value = re_write_b_value(pair[0], pair[2]) if rewrite_b_value else pair[2]
        o = logic(pair[0], b_value)

        if o[0] in hash_map_two.keys():
            player1_points += 6
            player1_points += point_map[o[1]]

        elif o[0] in hash_map_one.keys():
            player1_points += point_map[o[1]]

        else:
            player1_points += 3
            player1_points += point_map[o[1]]

    return player1_points


# -------
# PART 2
# -------
# X means you need to lose,
# Y means you need to end the round in a draw, and
# Z means you need to win.


print(get_answer(rewrite_b_value=True))

# defeat = my material ,
# loose =  my material
