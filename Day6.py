r = open(r"C:\Users\USER\Pictures\Advent\/Day6.txt").read()

inp = r.split("\n\n")

def num_yes_question(ipt):
    dic = {}

    for i in range(len(ipt)):
        lst = []
        for ques in ipt[i]:
            if ques not in lst and ques != '\n':
                lst.append(ques)
        dic[str(i)] = len(lst)

    total = 0
    for k, v in dic.items():
        total += v

    return total

def num_everyone_yes(ipt):
    dic = {}

    for i in range(len(ipt)):
        group = (ipt[i]).split('\n')
        yes_ques = set(group[0])
        for person in group[1:]:
            yes_ques &= set(person)
        dic[str(i)] = len(yes_ques)
    values = dic.values()
    return sum(values)

# part 1
print(num_yes_question(inp))

# part 2
print(num_everyone_yes(inp))

