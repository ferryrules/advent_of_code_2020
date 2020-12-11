from utils import get_data, answers, print_answers
import re

data = get_data(2020, 4).split('\n\n')
validish = 0
mega_valid = 0

def is_valid(key, v):
    switch = {
        'byr': v.isnumeric() and 1920 <= int(v) <= 2002,
        'iyr': v.isnumeric() and 2010 <= int(v) <= 2020,
        'eyr': v.isnumeric() and 2020 <= int(v) <= 2030,
        'hgt': (v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193) or (v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76),
        'hcl': v[0] == '#' and len(v) == 7 and not re.findall("[g-z]", v),
        'ecl': v in ('amb blu brn gry grn hzl oth'.split()),
        'pid': len(v) == 9 and v.isnumeric(),
        'cid': False
    }
    return switch[key]

for passport in data:
    passport = passport.replace('\n', ' ').split(' ')
    if len(passport) >= 7:
        p = ('').join(passport)
        if 'cid' not in p or len(passport) == 8:
            validish += 1
            valid_count = 0
            for items in passport:
                key = items.split(':')[0]
                value = items.split(':')[1]
                if is_valid(key, value):
                    valid_count += 1
            if valid_count == 7:
                mega_valid += 1

answers['first'] = validish
answers['second'] = mega_valid

print_answers(answers)
