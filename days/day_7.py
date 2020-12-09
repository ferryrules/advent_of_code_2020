from utils import get_data, answers, print_answers

data = get_data(2020, 7).split('\n')

holds_my_bag_colors = []
def get_the_color(bag):
    main_color = bag.split('bags')[0].strip()
    holds_my_bag_colors.append(main_color)

for bag in data:
    if 'shiny gold' in bag and bag.index('shiny gold') != 0:
        get_the_color(bag)

for color in holds_my_bag_colors:
    for bag in data:
        if color in bag and bag.index(color) != 0:
            get_the_color(bag)

answers['first'] = len(set(holds_my_bag_colors))

all_bags = {}
def parse_line(line):
    line = line.strip('.')
    bag, contents = line.split(' bags contain ')
    contents = contents.replace(' bags', '').replace(' bag', '').split(', ')
    if contents[0] == 'no other':
        contents = {}
    contents = {' '.join(i.split()[1:]): int(i.split()[0]) for i in contents}
    all_bags[bag] = contents

for line in data:
    parse_line(line)

def num_inner_bags(color):
    contents = all_bags[color]
    if contents == {}:
        return 0
    return sum(count * (1 + num_inner_bags(bag)) for bag, count in contents.items())

answers['second'] = num_inner_bags('shiny gold')

print_answers(answers)
