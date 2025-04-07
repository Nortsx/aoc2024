from collections import defaultdict

def parse_file_to_2d_array(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]


def get_antinode_position(first, second) -> []:
    diff_x = second[0] - first[0]
    diff_y = second[1] - first[1]

    return [(first[0] - diff_x, first[1] - diff_y), (second[0] + diff_x, second[1] + diff_y)]


grid = parse_file_to_2d_array('input.txt')
antennae = defaultdict(list)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != '.':
            antennae[grid[y][x]].append((x, y))

unique_antinodes = set()

for key in antennae:
    for i in range(len(antennae[key])):
        for j in range(i+1, len(antennae[key])):
            positions = get_antinode_position(antennae[key][i], antennae[key][j])
            for position in positions:
                if 0 <= position[0] < len(grid[0]) and 0 <= position[1] < len(grid):
                    unique_antinodes.add(position)

print(len(unique_antinodes))