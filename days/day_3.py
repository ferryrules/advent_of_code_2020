from utils import get_data, answers, print_answers

data = get_data(2020, 3)
data = data.split('\n')

def trees_in_path(right, down):
    trees = 0
    row = down
    move_right = right
    while len(data) > row:
        if len(data[row]) <= move_right:
            move_right = abs(len(data[row]) - move_right)
        if data[row][move_right] == "#":
            trees += 1
        row += down
        move_right += right
    return trees

a = trees_in_path(1, 1)
b = trees_in_path(3, 1)
c = trees_in_path(5, 1)
d = trees_in_path(7, 1)
e = trees_in_path(1, 2)

answers['first'] = b
answers['second'] = a*b*c*d*e

print_answers(answers)
