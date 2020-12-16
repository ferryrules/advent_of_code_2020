from utils import get_data, answers, print_answers

data = get_data(2020, 8).split('\n')

def program(data):
    index_visited = []
    index = 0
    acc = 0
    while index not in index_visited:
        if index == len(data):
            answers['second'] = acc
            return True
        else:
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
    return False

def break_loop(data):
    index = 0
    while index < len(data):
        key = data[index].split(' ')[0]
        if key == 'jmp':
            data[index] = data[index].replace('jmp', 'nop')
            if program(data):
                return None
            data[index] = data[index].replace('nop', 'jmp')
        elif key == 'nop':
            data[index] = data[index].replace('nop', 'jmp')
            if program(data):
                return None
            data[index] = data[index].replace('jmp', 'nop')
        index += 1

break_loop(data)
print_answers(answers)
