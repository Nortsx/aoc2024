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


def find_path_iterative(trailmap, start_pos):
    stack = [(start_pos, 0)]
    total_sum = 0

    while stack:
        current_pos, current_sum = stack.pop()
        x, y = current_pos

        if trailmap[y][x] == '9':
            total_sum += current_sum + 1
            continue

        # Add valid neighbors to the stack
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(trailmap[0]) and 0 <= ny < len(trailmap):
                if trailmap[ny][nx] != '.' and trailmap[ny][nx] == str(int(trailmap[y][x]) + 1):
                    stack.append(((nx, ny), current_sum))

    return total_sum


paths = 0

for trailhead in trailheads:
    paths += find_path_iterative(trailmap, trailhead)

print(paths)