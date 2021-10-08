
def not_valid(preamble_lst, num):
    for n in preamble_lst:
        diff = num - n
        if diff != n and diff in preamble_lst:
            return False
    return True
def XMAS_attacking_1(num_list, n_pre):
    n_pre = int(n_pre)
    num_list = [int(x) for x in num_list]
    for i in range(len(num_list) - n_pre):
        preamble_lst = num_list[i: i + n_pre]
        curr = num_list[i + n_pre]
        if not_valid(preamble_lst, curr):
            return curr

def XMAS_attacking_2(num_list, invalid_num):
    invalid_num = int(invalid_num)
    num_list = [int(x) for x in num_list]
    contiguous_set = []
    summ = 0
    for i in range(len(num_list)):
        summ += num_list[i]
        contiguous_set.append(num_list[i])
        if summ == invalid_num:
            minn = min(contiguous_set)
            maxx = max(contiguous_set)
            return minn + maxx
        while summ > invalid_num:
            summ -= contiguous_set[0]
            del contiguous_set[0]
            if summ == invalid_num:
                minn = min(contiguous_set)
                maxx = max(contiguous_set)
                return minn + maxx

if __name__ == '__main__':
    r = open(r"C:\Users\USER\Pictures\Advent-of-Code-2020\/Day9.txt").read()
    inp = r.split("\n")

    # part 1
    ans_p1 = XMAS_attacking_1(inp, 25)
    print(ans_p1)

    # part 2
    print(XMAS_attacking_2(inp, ans_p1))
