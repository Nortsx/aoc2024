from collections import defaultdict

def parse_file_to_2d_array(file_path):
    with open(file_path, 'r') as file:
        # Read all lines, stripping the newline character
        return [list(line.strip()) for line in file.readlines()]


grid = parse_file_to_2d_array('input.txt')


def get_antinode_positions(first, second, boundariesX, boundariesY) -> []:
    diff_x = second[0] - first[0]
    diff_y = second[1] - first[1]

    result = []
    position_first = (first[0], first[1])
    position_second = (second[0], second[1])
    result.append(position_first)
    result.append(position_second)
    while True:
        position_first = (position_first[0] - diff_x, position_first[1] - diff_y)
        if 0 <= position_first[0] < boundariesX and 0 <= position_first[1] < boundariesY:
            result.append(position_first)
        else:
            break

    while True:
        position_second = (position_second[0] + diff_x, position_second[1] + diff_y)
        if 0 <= position_second[0] < boundariesX and 0 <= position_second[1] < boundariesY:
            result.append(position_second)
        else:
            break

    return result


antennae = defaultdict(list)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != '.':
            antennae[grid[y][x]].append((x, y))

unique_antinodes = set()

for key in antennae:
    for i in range(len(antennae[key])):
        for j in range(i+1, len(antennae[key])):
            positions = get_antinode_positions(antennae[key][i], antennae[key][j], len(grid[0]), len(grid))
            for position in positions:
                unique_antinodes.add(position)
                grid[position[1]][position[0]] = "#"


print(len(unique_antinodes))