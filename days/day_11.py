from utils import get_data, answers, print_answers

data = get_data(2020, 11).split('\n')

def surrounding_seats(data, row, seat):
    full = 0
    if (row + 1) < len(data):
        if data[row+1][seat] == "#":
            full += 1
        if (seat + 1) < len(data[row]):
            if data[row+1][seat+1] == "#":
                full += 1
        if (seat - 1) >= 0:
            if data[row+1][seat-1] == "#":
                full += 1
    if (row - 1) >= 0:
        if data[row-1][seat] == "#":
            full += 1
        if (seat + 1) < len(data[row]):
            if data[row-1][seat+1] == "#":
                full += 1
        if (seat - 1) >= 0:
            if data[row-1][seat-1] == "#":
                full += 1
    if (seat + 1) < len(data[row]):
        if data[row][seat+1] == "#":
            full += 1
    if (seat - 1) >= 0:
        if data[row][seat-1] == "#":
            full += 1
    return full

def something(data):
    new_data = []
    for i, row in enumerate(data):
        new_data.append('')
        tb = (i == 0) or (i == (len(data) - 1))
        for x, seat in enumerate(row):
            lr = (x == 0) or (x == (len(data[i]) - 1))
            ss = surrounding_seats(data, i, x)
            if data[i][x] == '.':
                new_data[i] += '.'
            elif tb and lr:
                new_data[i] += '#'
            elif data[i][x] == 'L' and ss == 0:
                new_data[i] += '#'
            elif data[i][x] == '#' and ss >= 4:
                new_data[i] += 'L'
            else:
                new_data[i] += data[i][x]
    return new_data

shiz = something(data)
shiz2 = something(shiz)

while shiz != shiz2:
    shiz = shiz2
    shiz2 = something(shiz)

count = 0
for row in shiz2:
    count += row.count('#')

print(count)
