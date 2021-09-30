import copy

def parse_comm_step(inp):
    res = {}
    for i in range(len(inp)):
        comm_step = inp[i].split(' ')
        comm_step[1] = int(comm_step[1])
        res[i] = comm_step
    return res

def comm_tracking(inp):
    parsed = inp
    if isinstance(inp, list):
        parsed = parse_comm_step(inp)
    track = []
    acc = 0
    next_step = 0
    i = 0
    while next_step not in track and next_step < len(parsed):
        track.append(next_step)
        comm, step = parsed[next_step]
        if comm == 'nop':
            next_step += 1
        elif comm == 'acc':
            acc += step
            next_step += 1
        elif comm == 'jmp':
            next_step += step
    return acc, next_step

def fix_inf_loop(inp):
    parsed = parse_comm_step(inp)

    for ind in parsed:
        comm, step = parsed[ind]
        if comm == 'jmp':
            copy_dic = copy.deepcopy(parsed)
            copy_dic[ind][0] = 'nop'
            acc, terminate_step = comm_tracking(copy_dic)
            if terminate_step == len(parsed):
                return acc
        elif comm == 'nop':
            copy_dic = copy.deepcopy(parsed)
            copy_dic[ind][0] = 'jmp'
            acc, terminate_step = comm_tracking(copy_dic)
            if terminate_step == len(parsed):
                return acc
    
if __name__ == '__main__':
    r = open(r"C:\Users\USER\Pictures\Advent-of-Code-2020\/Day8.txt").read()
    inp = r.split("\n")
    
    # part 1
    print(comm_tracking(inp)[0])
    
    # part 2
    print(fix_inf_loop(inp))