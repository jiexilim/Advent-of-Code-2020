def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
    
def extract_colours(bag_list):
    extracted = {}
    for lst in bag_list:
        lst = lst.split(' ')
        i = 0
        colour = ""
        main_colour = ""
        num = 0
        while i < len(lst):
            if i == 0:
                while "bag" not in lst[i] and i < len(lst):
                    main_colour += lst[i]
                    i += 1
                extracted[main_colour] = {}
            if num > 0 and i < len(lst):
                while "bag" not in lst[i] and i < len(lst):
                    colour += lst[i]
                    i += 1
                extracted[main_colour][colour] = num
                colour = ''
                num = 0
            if is_integer(lst[i]):
                num = int(lst[i])
            i += 1
    return extracted

def count_bags_contain_tgt(bag_list, target):
    target = target.replace(' ', '')
    bag_dic = extract_colours(bag_list)
    res = []
    waiting = [target,]
    while waiting:
        target = waiting.pop()
        res.append(target)
        for k, v in bag_dic.items():
            if target in v and (k not in waiting and k not in res):
                waiting.append(k)
    return len(res) - 1

def count_bags_hold(bag_list, target):
    target = target.replace(' ', '')
    bag_dic = extract_colours(bag_list)
    return count_recur(bag_dic, target)

def count_recur(bag_dic, target):
    if target not in bag_dic:
        return 1
    elif bag_dic[target] == {}:
        return 1
    else:
        count = 0
        for k, v in bag_dic[target].items():
            count += (count_recur(bag_dic, k) * v)
            if count_recur(bag_dic, k) > 1:
                count += v
        return count

if __name__ == '__main__':
    r = open(r"C:\Users\USER\Pictures\Advent-of-Code-2020\/Day7.txt").read()
    inp = r.split("\n")
    target = "shiny gold"
    
    # part 1
    print(count_bags_contain_tgt(inp, target))
    
    # part 2
    print(count_bags_hold(inp, target))