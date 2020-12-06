from utils import get_data, answers, print_answers

data = get_data(2020, 6).split('\n\n')

print(data)

yes_answers = 0
for group in data:
    group = group.replace('\n', '')
    unique_yes = set(group)
    yes_answers += len(unique_yes)
print(yes_answers)
