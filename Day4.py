r = open(r"C:\Users\USER\Pictures\Advent\/Day4.txt").read()

input = r.split("\n\n")


def passport_processing(inp):
    passports = []
    correct = 0

    for entry in inp:
        entry = entry.split()
        passport = {}

        for info in entry:
            key, value = info.split(':')
            passport[key] = value
        passports.append(passport)

    for passport in passports:
        if ('byr' in passport) and ('iyr' in passport) \
                and ('eyr' in passport) and ('hgt' in passport) \
                and ('hcl' in passport) and ('ecl' in passport) \
                and ('pid' in passport):
            correct += 1
    return correct


print(passport_processing(input))


# part 2

def byr_checker(val):
    if (len(val) == 4) and (val.isdigit()):
        return (int(val) >= 1920) and (int(val) <= 2002)
    return False


def iyr_checker(val):
    if (len(val) == 4) and (val.isdigit()):
        return (int(val) >= 2010) and (int(val) <= 2020)
    return False


def eyr_checker(val):
    if (len(val) == 4) and (val.isdigit()):
        return (int(val) >= 2020) and (int(val) <= 2030)
    return False


def hgt_checker(val):
    num = val[:-2]
    type = val[-2:]
    if num.isdigit():
        if type == "cm":
            return (int(num) >= 150) and (int(num) <= 193)
        elif type == "in":
            return (int(num) >= 59) and (int(num) <= 76)
    return False


def hcl_checker(val):
    if val[0] == '#':
        return val[1:].isalnum() and (len(val[1:]) == 6)
    return False


def ecl_checker(val):
    checked = False
    color_lst = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for color in color_lst:
        if val == color:
            checked = True
            break
    return checked


def pid_checker(val):
    return val.isdigit() and (len(val) == 9)


def passport_processing_imp(inp):
    passports = []
    correct = 0

    for entry in inp:
        entry = entry.split()
        passport = {}

        for info in entry:
            key, value = info.split(':')
            passport[key] = value
        passports.append(passport)

    for passport in passports:
        if ('byr' in passport) and ('iyr' in passport) \
                and ('eyr' in passport) and ('hgt' in passport) \
                and ('hcl' in passport) and ('ecl' in passport) \
                and ('pid' in passport):
            byr = byr_checker(passport['byr'])
            iyr = iyr_checker(passport['iyr'])
            eyr = eyr_checker(passport['eyr'])
            hgt = hgt_checker(passport['hgt'])
            hcl = hcl_checker(passport['hcl'])
            ecl = ecl_checker(passport['ecl'])
            pid = pid_checker(passport['pid'])
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                correct += 1
    return correct


print(passport_processing_imp(input))
