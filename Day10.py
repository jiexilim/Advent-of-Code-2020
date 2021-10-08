
def solve_adapter_chain(adapters_list):
    adapters_list.sort()

    diff_1 = 0
    diff_3 = 0
    prev_jolt = 0
    for i in range(len(adapters_list)):
        if adapters_list[i] - prev_jolt == 1:
            diff_1 += 1
        elif adapters_list[i] - prev_jolt == 3:
            diff_3 += 1
        prev_jolt = adapters_list[i]
    diff_3 += 1

    return diff_1 * diff_3


def count_adapter_ways(adapters_list):
    adapters_list.sort()
    adapters_list.insert(0, 0)

    dic = {}
    dic[adapters_list[0]] = 1
    for i in range(1, len(adapters_list)):
        curr_ways = 0
        curr_adapter = adapters_list[i]
        i -= 1
        prev_adapter = adapters_list[i]
        while (curr_adapter - prev_adapter < 4):
            curr_ways += dic[prev_adapter]
            if i <= 0:
                break
            i -= 1
            prev_adapter = adapters_list[i]
        dic[curr_adapter] = curr_ways
        
    return dic[adapters_list[len(adapters_list)-1]]

if __name__ == '__main__':
    r = open(r"C:\Users\USER\Pictures\Advent-of-Code-2020\/Day10.txt").read()
    inp = r.split("\n")
    inp = [int(x) for x in inp]

    # part 1
    print(solve_adapter_chain(inp))

    # part 2
    print(count_adapter_ways(inp))
