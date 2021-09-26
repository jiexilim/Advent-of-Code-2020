# part 1
with open(r"C:\Users\USER\Pictures\Advent\/Day2.txt", "r") as f:
    correct = 0
    for x in f:
        split = x.split()
        policy = split[0].split("-")
        num1 = int(policy[0])
        num2 = int(policy[1])
        alphabet = split[1][0]
        pw = split[2]
        count_occ = pw.count(alphabet)
        if (count_occ >= num1) and (count_occ <= num2):
            correct += 1
    print(correct)

# part 2
with open(r"C:\Users\USER\Pictures\Advent\/Day2.txt", "r") as f:
    correct = 0
    for x in f:
        split = x.split()
        if "-" not in split[0]:
            print(split[0])
        policy = split[0].split("-")
        num1 = int(policy[0])
        num2 = int(policy[1])
        alphabet = split[1][0]
        pw = split[2]
        first_pos = pw[num1 - 1]
        sec_pos = pw[num2 - 1]
        if (alphabet == first_pos) and (alphabet != sec_pos):
            correct += 1
        if (alphabet != first_pos) and (alphabet == sec_pos):
            correct += 1
    print(correct)

