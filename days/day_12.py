from utils import get_data, answers, print_answers

data = get_data(2020, 12).split('\n')
# Degrees based on R
shiz = {
 'N': {90: 'E', 180: 'S', 270: 'W', 'coor': 0},
 'E': {90: 'S', 180: 'W', 270: 'N', 'coor': 0},
 'S': {90: 'W', 180: 'N', 270: 'E', 'coor': 0},
 'W': {90: 'N', 180: 'E', 270: 'S', 'coor': 0}
 }

facing = 'E'
for x in data:
    direction = x[0]
    move = int(x[1:])
    if direction == 'F':
        shiz[facing]['coor'] += move
    elif direction == 'R':
        facing = shiz[facing][move]
    elif direction == 'L':
        r = 360 - move
        facing = shiz[facing][r]
    else:
        shiz[direction]['coor'] += move

results = abs(shiz['N']['coor'] - shiz['S']['coor']) + abs(shiz['E']['coor'] - shiz['W']['coor'])
answers['first'] = results

shiz = {
 'N': {90: 'E', 180: 'S', 270: 'W', 'coor': 0},
 'E': {90: 'S', 180: 'W', 270: 'N', 'coor': 0},
 'S': {90: 'W', 180: 'N', 270: 'E', 'coor': 0},
 'W': {90: 'N', 180: 'E', 270: 'S', 'coor': 0}
 }

way = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
way2 = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
for x in data:
    direction = x[0]
    move = int(x[1:])

    if direction == 'F':
        for k in way.keys():
            shiz[k]['coor'] += (way[k] * move)

    elif direction == 'R':
        for k in way.keys():
            i = shiz[k][move]
            way2[i] = way[k]
        way = way2
        way2 = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    elif direction == 'L':
        rx = 360 - move
        for k in way.keys():
            i = shiz[k][rx]
            way2[i] = way[k]
        way = way2
        way2 = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    elif way[direction] > 0:
        way[direction] += move

    else:
        if direction == 'S':
            if (way['N'] - move) < 0:
                way['S'] = abs(way['N'] - move)
                way['N'] = 0
            else:
                way['N'] = way['N'] - move

        if direction == 'N':
            if (way['S'] - move) < 0:
                way['N'] = abs(way['S'] - move)
                way['S'] = 0
            else:
                way['S'] = way['S'] - move

        if direction == 'W':
            if (way['E'] - move) < 0:
                way['W'] = abs(way['E'] - move)
                way['E'] = 0
            else:
                way['E'] = way['E'] - move

        if direction == 'E':
            if (way['W'] - move) < 0:
                way['E'] = abs(way['W'] - move)
                way['W'] = 0
            else:
                way['W'] = way['W'] - move

results = abs(shiz['N']['coor'] - shiz['S']['coor']) + abs(shiz['E']['coor'] - shiz['W']['coor'])
answers['second'] = results


print_answers(answers)
