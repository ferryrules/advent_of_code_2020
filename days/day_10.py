from utils import get_data, answers, print_answers

data = get_data(2020, 10).split('\n')
adapters = [0] + list(sorted(map(int, data)))
adapters.append(max(adapters) + 3)

jolts = {'1': 0, '3': 0}
index = 1
while index < len(adapters):
    difference = adapters[index] - adapters[index-1]
    jolts[str(difference)] += 1
    index += 1

answers['first'] = jolts['1'] * jolts['3']

ways = [1]
for i, adapter in enumerate(adapters):
    if i == 0:
        continue
    ways.append(0)
    x = i - 1
    while x >= 0 and adapter - adapters[x] <= 3:
        ways[i] += ways[x]
        x -= 1
answers['second'] = ways[-1]

print_answers(answers)
