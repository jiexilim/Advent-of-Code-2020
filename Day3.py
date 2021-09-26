r = open(r"C:\Users\USER\Pictures\Advent\/Day3.txt").read().strip('\n')

input = r.splitlines()


def tree_encountering(map, y, x):
    y_coor = 0
    x_coor = 0
    tree = 0
    while True:
        y_coor += int(y)
        if y_coor >= len(map):
            break
        x_coor = (x_coor + int(x)) % len(map[y_coor])
        if map[y_coor][x_coor] == '#':
            tree += 1

    return tree


print(tree_encountering(input, 1, 3) * tree_encountering(input, 1, 1)
      * tree_encountering(input, 1, 5) * tree_encountering(input, 1, 7)
      * tree_encountering(input, 2, 1))
