from utils import get_data, answers, print_answers

data = get_data(2020, 10).split('\n')
adapters = []

for item in data:
    adapters.append(int(item))

adapters = sorted(adapters)
device = max(adapters) + 3
adapters.append(device)

jolts = {'1': 0, '3': 0}
jolts[str(adapters[0])] = adapters[0]

index = 1
while index < len(adapters):
    difference = adapters[index] - adapters[index-1]
    jolts[str(difference)] += 1
    index += 1

answers['first'] = jolts['1'] * jolts['3']
print_answers(answers)
