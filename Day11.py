import copy as cp

def count_seated(seat_list):
    num_seated = 0
    for row in seat_list:
        if not isinstance(row, list):
            row = [row]
        num_seated += row.count('#')
    return num_seated

def update_top(top, next):
    copy = cp.deepcopy(top)
    copy[0] = '.' if top[0] == '.' else '#'
    copy[len(top)-1] = '.' if top[len(top)-1] == '.' else '#'

    for i in range(1, len(top) - 1):
        if top[i] == '.':
            continue
        left = top[i - 1]
        right = top[i + 1]
        bottom = next[i]
        bottom_left = next[i - 1]
        bottom_right = next[i + 1]
        adj_pos = [left, right, bottom, bottom_right, bottom_left]
        count = count_seated(adj_pos)
        if top[i] == 'L' and count == 0:
            copy[i] = '#'
        elif top[i] == '#' and count >= 4:
            copy[i] = 'L'

    return copy

def update_bottom(bottom, prev):
    copy = cp.deepcopy(bottom)
    copy[0] = '.' if bottom[0] == '.' else '#'
    copy[len(bottom) - 1] = '.' if bottom[len(bottom) - 1] == '.' else '#'

    for i in range(1, len(bottom) - 1):
        if bottom[i] == '.':
            continue
        left = bottom[i - 1]
        right = bottom[i + 1]
        top = prev[i]
        top_left = prev[i - 1]
        top_right = prev[i + 1]
        adj_pos = [left, right, top, top_right, top_left]
        count = count_seated(adj_pos)
        if bottom[i] == 'L' and count == 0:
            copy[i] = '#'
        elif bottom[i] == '#' and count >= 4:
            copy[i] = 'L'

    return copy

def update_mid(mid, prev, next):
    copy = cp.deepcopy(mid)

    for i in range(len(mid)):
        if mid[i] != '.':
            top = prev[i]
            bottom = next[i]
            left, top_left, bottom_left, right, top_right, bottom_right = 0, 0, 0, 0, 0, 0
            if i != 0:
                left = mid[i - 1]
                top_left = prev[i - 1]
                bottom_left = next[i - 1]
            if i != (len(mid) - 1):
                right = mid[i + 1]
                top_right = prev[i + 1]
                bottom_right = next[i + 1]
            adj_pos = [left, right, top, top_right, top_left, bottom, bottom_right, bottom_left]
            count = count_seated(adj_pos)
            if mid[i] == 'L' and count == 0:
                copy[i] = '#'
            elif mid[i] == '#' and count >= 4:
                copy[i] = 'L'
    return copy

def stabilize_seats(seat_list):
    seat_list = [[char for char in row] for row in seat_list]
    prev_state = seat_list
    curr_state = []

    while curr_state != prev_state:
        prev_state = cp.deepcopy(seat_list)
        curr_state = []
        for i in range(len(seat_list)):
            if i == 0:
                curr_state.append(update_top(seat_list[i], seat_list[i + 1]))
            elif i == (len(seat_list)-1):
                curr_state.append(update_bottom(seat_list[i], seat_list[i - 1]))
            else:
                curr_state.append(update_mid(seat_list[i], seat_list[i-1], seat_list[i+1]))
        seat_list = cp.deepcopy(curr_state)
    return count_seated(curr_state)

def new_update_top(seat_list):
    top = seat_list[0]
    copy = cp.deepcopy(top)
    copy[0] = '.' if top[0] == '.' else '#'
    copy[len(top) - 1] = '.' if top[len(top) - 1] == '.' else '#'
    height = len(seat_list)
    length = len(top)

    for i in range(1, len(copy) - 1):
        sum_occupied = 0
        # left
        j = i - 1
        while j >= 0:
            if top[j] == 'L':
                break
            elif top[j] == '#':
                sum_occupied += 1
                break
            j -= 1
        # right
        j = i + 1
        while j < length:
            if top[j] == 'L':
                break
            elif top[j] == '#':
                sum_occupied += 1
                break
            j += 1
        # bottom
        for j in range(1, height):
            if seat_list[j][i] == 'L':
                break
            elif seat_list[j][i] == '#':
                sum_occupied += 1
                break
        # bottom left
        nxt = i - 1
        for j in range(1, height):
            if nxt < 0:
                break
            if seat_list[j][nxt] == 'L':
                break
            elif seat_list[j][nxt] == '#':
                sum_occupied += 1
                break
            nxt -= 1
        # bottom right
        nxt = i + 1
        for j in range(1, height):
            if nxt >= length:
                break
            if seat_list[j][nxt] == 'L':
                break
            elif seat_list[j][nxt] == '#':
                sum_occupied += 1
                break
            nxt += 1
        if top[i] == 'L' and sum_occupied == 0:
            copy[i] = '#'
        elif top[i] == '#' and sum_occupied >= 5:
            copy[i] = 'L'
    return copy

def new_update_bottom(seat_list):
    bottom = seat_list[len(seat_list)-1]
    height = len(seat_list)
    length = len(bottom)
    copy = cp.deepcopy(bottom)
    copy[0] = '.' if bottom[0] == '.' else '#'
    copy[len(bottom) - 1] = '.' if bottom[len(bottom) - 1] == '.' else '#'

    for i in range(1, len(copy)-1):
        sum_occupied = 0
        # left
        j = i - 1
        while j >= 0:
            if bottom[j] == 'L':
                break
            elif bottom[j] == '#':
                sum_occupied += 1
                break
            j -= 1
        # right
        j = i + 1
        while j < length:
            if bottom[j] == 'L':
                break
            elif bottom[j] == '#':
                sum_occupied += 1
                break
            j += 1
        # top
        j = height - 2
        while j >= 0:
            if seat_list[j][i] == 'L':
                break
            elif seat_list[j][i] == '#':
                sum_occupied += 1
                break
            j -= 1
        # top left
        nxt = i - 1
        j = height - 2
        while j >= 0:
            if nxt < 0:
                break
            if seat_list[j][nxt] == 'L':
                break
            elif seat_list[j][nxt] == '#':
                sum_occupied += 1
                break
            nxt -= 1
            j -= 1
        # top right
        nxt = i + 1
        j = height - 2
        while j >= 0:
            if nxt >= length:
                break
            if seat_list[j][nxt] == 'L':
                break
            elif seat_list[j][nxt] == '#':
                sum_occupied += 1
                break
            nxt += 1
            j -= 1
        if bottom[i] == 'L' and sum_occupied == 0:
            copy[i] = '#'
        elif bottom[i] == '#' and sum_occupied >= 5:
            copy[i] = 'L'

    return copy

def new_update_mid(row_i, seat_list):
    mid = seat_list[row_i]
    height = len(seat_list)
    length = len(mid)
    copy = cp.deepcopy(mid)

    for i in range(len(copy)):
        sum_occupied = 0
        # left
        j = i - 1
        while j >= 0:
            if mid[j] == 'L':
                break
            elif mid[j] == '#':
                sum_occupied += 1
                break
            j -= 1
        # right
        j = i + 1
        while j < length:
            if mid[j] == 'L':
                break
            elif mid[j] == '#':
                sum_occupied += 1
                break
            j += 1
        # top
        j = row_i - 1
        while j >= 0:
            if seat_list[j][i] == 'L':
                break
            elif seat_list[j][i] == '#':
                sum_occupied += 1
                break
            j -= 1
        # top left
        nxt = i - 1
        j = row_i - 1
        while j >= 0:
            if nxt < 0:
                break
            if seat_list[j][nxt] == 'L':
                break
            elif seat_list[j][nxt] == '#':
                sum_occupied += 1
                break
            nxt -= 1
            j -= 1
        # top right
        nxt = i + 1
        j = row_i - 1
        while j >= 0:
            if nxt >= length:
                break
            if seat_list[j][nxt] == 'L':
                break
            elif seat_list[j][nxt] == '#':
                sum_occupied += 1
                break
            nxt += 1
            j -= 1

        # bottom
        for j in range(row_i + 1, height):
            if seat_list[j][i] == 'L':
                break
            elif seat_list[j][i] == '#':
                sum_occupied += 1
                break
        # bottom left
        nxt = i - 1
        for j in range(row_i + 1, height):
            if nxt < 0:
                break
            if seat_list[j][nxt] == 'L':
                break
            elif seat_list[j][nxt] == '#':
                sum_occupied += 1
                break
            nxt -= 1
        # bottom right
        nxt = i + 1
        for j in range(row_i + 1, height):
            if nxt >= length:
                break
            if seat_list[j][nxt] == 'L':
                break
            elif seat_list[j][nxt] == '#':
                sum_occupied += 1
                break
            nxt += 1
        if mid[i] == 'L' and sum_occupied == 0:
            copy[i] = '#'
        elif mid[i] == '#' and sum_occupied >= 5:
            copy[i] = 'L'
            
    return copy

def new_stabilize_seats(seat_list):
    seat_list = [[char for char in row] for row in seat_list]
    prev_state = seat_list
    curr_state = []

    while curr_state != prev_state:
        prev_state = cp.deepcopy(seat_list)
        curr_state = []
        for i in range(len(seat_list)):
            if i == 0:
                curr_state.append(new_update_top(seat_list))
            elif i == (len(seat_list)-1):
                curr_state.append(new_update_bottom(seat_list))
            else:
                curr_state.append(new_update_mid(i, seat_list))
        seat_list = cp.deepcopy(curr_state)
    return count_seated(curr_state)

if __name__ == '__main__':
    r = open(r"C:\Users\USER\Pictures\Advent-of-Code-2020\/Day11.txt").read()
    inp = r.split("\n")

    # part 1
    stable = stabilize_seats(inp)
    print(stable)

    # part 2
    new_stable = new_stabilize_seats(inp)
    print(new_stable)
