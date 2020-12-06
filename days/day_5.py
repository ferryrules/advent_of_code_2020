from utils import get_data, answers, print_answers
from operator import itemgetter

data = get_data(2020, 5).split('\n')

find_highest = []
for ticket in data:
    count = 10
    find_row = list(range(0, 128))
    find_col = list(range(0, 8))
    for t in ticket:
        if count > 0:
            r_ind = int(len(find_row)/2)
            c_ind = int(len(find_col)/2)
            if t == 'F':
                find_row = find_row[:r_ind]
            if t == 'B':
                find_row = find_row[r_ind:]
            if t == 'L':
                find_col = find_col[:c_ind]
            if t == 'R':
                find_col = find_col[c_ind:]
            count -= 1
    find_highest.append(find_row[0]*8+find_col[0])

def find_missing(lst):
    start = lst[0]
    end = lst[-1]
    return sorted(set(range(start, end + 1)).difference(lst))

my_seat = find_missing(sorted(find_highest))

answers['first'] = max(find_highest)
answers['second'] = my_seat[0]
print_answers(answers)
