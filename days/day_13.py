from utils import get_data, answers, print_answers
import math

data = get_data(2020, 13).split('\n')

buses = data[1].split(',')
time_stamp = int(data[0])

bus = 0
minutes = 0
count = 0

for b in buses:
    if b != 'x':
        x = math.ceil(time_stamp/int(b)) * int(b)
        if count == 0:
            minutes = x - time_stamp
            bus = int(b)
            count += 1
        if (x - time_stamp) < minutes:
            minutes = x - time_stamp
            bus = int(b)

answers['first'] = bus * minutes

print_answers(answers)
