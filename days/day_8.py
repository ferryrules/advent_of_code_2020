from utils import get_data, answers, print_answers

data = get_data(2020, 8).split('\n')

index_visited = []
index = 0
acc = 0

while index not in index_visited:
    key = data[index].split(' ')[0]
    value = int(data[index].split(' ')[1])
    index_visited.append(index)
    if key == 'acc':
        acc += value
        index += 1
    elif key == 'nop':
        index += 1
    else:
        index += value

answers['first'] = acc
print_answers(answers)
