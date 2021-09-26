with open(r"C:\Users\USER\Pictures\Advent\/Day1.txt", "r") as f:
    lst = []

    for x in f:
        line = x.strip()
        lst.append(x)
    for i in range(len(lst)):
        first_num = int(lst[i])
        for j in range(i, len(lst)):
            sec_num = int(lst[j])
            for k in range(j, len(lst)):
                third_num = int(lst[k])
                if (first_num + sec_num + third_num) == 2020:
                    print(first_num * sec_num * third_num)
                    break
