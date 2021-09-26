r = open(r"C:\Users\USER\Pictures\Advent\/Day5.txt").read()

inp = r.split("\n")

def row_number(string):
    lower = 0
    upper = 127

    for i in range(7):
        temp = (upper - lower) // 2
        if string[i] == 'F':
            upper = upper - temp - 1
        else:
            lower = lower + temp + 1
    return upper

def col_number(string):
    lower = 0
    upper = 7

    for i in range(3):
        temp = (upper - lower) // 2
        if string[i] == 'L':
            upper = upper - temp - 1
        else:
            lower = lower + temp + 1
    return upper

def seat_number(string):
    return (row_number(string[0:7]) * 8) + col_number(string[7:10])

def parse_seat(ipt):
    res = []

    for i in range(len(ipt)):
        res.append(seat_number(ipt[i]))

    return res

def highest_seat_id(ipt):
    return max(parse_seat(ipt))

def my_seat(ipt):
    seat_lst = parse_seat(ipt)
    seat_lst.sort()

    for i in range(len(seat_lst) - 1):
        if (seat_lst[i] + 1) != seat_lst[i + 1]:
            return seat_lst[i] + 1
# part 1
print(highest_seat_id(inp))

# part 2
print(my_seat(inp))