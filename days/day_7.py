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

print_answers(answers)
