def parse_file_to_2d_array(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]


trailmap = parse_file_to_2d_array('input.txt')

trailheads = []

for y in range(len(trailmap)):
    for x in range(len(trailmap[0])):
        if trailmap[y][x] == '0':
            trailheads.append((x, y))

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_path(trailmap, current_pos, nines_set):
    x, y = current_pos
    if trailmap[y][x] == '9':
        nines_set.add((x, y))
    for dx, dy in directions:
        if 0 <= x + dx < len(trailmap[0]) and 0 <= y + dy < len(trailmap):
            if trailmap[y + dy][x + dx] != '.' and trailmap[y + dy][x + dx] == str(int(trailmap[y][x]) + 1):
                find_path(trailmap, (x + dx, y + dy), nines_set)


paths = 0


for trailhead in trailheads:
    nines_set = set()
    find_path(trailmap, trailhead, nines_set)
    paths += len(nines_set)


print(paths)
