from utils import get_data, answers, print_answers

data = get_data(2020, 6).split('\n\n')

yes_answers = 0
for group in data:
    group = group.replace('\n', '')
    unique_yes = set(group)
    yes_answers += len(unique_yes)
answers['first'] = yes_answers

yes_answers = 0
for group in data:
    group = group.replace('\n', ' ').split(' ')
    if len(group) == 1:
        yes_answers += len(group[0])
    else:
        for each_yes in group[0]:
            answered_yes = 0
            for each_q in group:
                if each_yes in each_q:
                    answered_yes += 1
            if answered_yes == len(group):
                yes_answers += 1
answers['second'] = yes_answers

print_answers(answers)
