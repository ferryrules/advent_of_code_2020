from utils import get_data, answers, print_answers

data = get_data(2020, 2)
data = data.split('\n')

count1 = 0
count2 = 0

for x in data:
    allowed_1st = int(x.split(" ")[0].split("-")[0])
    allowed_2nd = int(x.split(" ")[0].split("-")[1])
    letter_to_check = x.split(" ")[1][0]
    password = x.split(" ")[2]
    if password.count(letter_to_check) >= allowed_1st and password.count(letter_to_check) <= allowed_2nd:
        count1 += 1
    position_check = password[allowed_1st-1] + password[allowed_2nd-1]
    if position_check.count(letter_to_check) == 1:
        count2 += 1

answers['second'] = count2
answers['first'] = count1

print_answers(answers)
