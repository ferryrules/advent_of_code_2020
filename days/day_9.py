from utils import get_data, answers, print_answers

data = get_data(2020, 9).split('\n')
numbers = []
for num in data:
    numbers.append(int(num))

def something(start_pre, after_pre=-1):
    return numbers[start_pre:after_pre]

start_pre = 0
after_pre = 25
preamble = something(start_pre, after_pre)
count = 0
while count < len(numbers):
    for num in preamble:
        if (numbers[after_pre] - num) in preamble and num != preamble[-1]:
            start_pre += 1
            after_pre += 1
            preamble = something(start_pre, after_pre)
    count += 1

answers['first'] = numbers[after_pre]

# def part_2():
start_index = 0
new_nums = something(start_index)
goal = numbers[after_pre]
while start_index < len(new_nums):
    index = 0
    totes = 0
    list_nums = []
    for num in new_nums:
        if totes == goal:
            answers['second'] = min(list_nums) + max(list_nums)
            # return(list_nums)
            break
        if totes < goal:
            list_nums.append(new_nums[index])
            totes += new_nums[index]
            index += 1
    start_index += 1
    new_nums = something(start_index)

# list = part_2()
# answers['second'] = min(list) + max(list)
print_answers(answers)
