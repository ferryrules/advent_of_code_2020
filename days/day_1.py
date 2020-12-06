from utils import get_data, answers, print_answers

data = get_data(2020, 1)
data = data.split('\n')

for star in data:
    s = int(star)
    index = data.index(star) + 1

    remainder = 2020 - s

    if str(remainder) in data:
        answers['first'] = remainder*s

    while len(data) > index:
        if s + int(data[index]) < 2020:
            remainder = 2020 - (s + int(data[index]))
            if str(remainder) in data:
                answers['second'] = remainder*s*int(data[index])
        index += 1

print_answers(answers)
