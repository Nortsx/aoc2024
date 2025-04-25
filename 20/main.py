from collections import defaultdict

grid = [[elem for elem in line.strip()] for line in open("input.txt").readlines()]
print(grid)

start_pos = (0, 0)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            start_pos = (x, y)
print(start_pos)


def find_path(start_pos, map) -> []:
    dots_path = []
    dots_path.append(start_pos)
    visited = set()
    while True:
        current_pos = dots_path[-1]
        x, y = current_pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < len(map[0]) and 0 <= y + dy < len(map):
                if map[y + dy][x + dx] == '.' and (x + dx, y + dy) not in visited:
                    dots_path.append((x + dx, y + dy))
                    visited.add((x + dx, y + dy))
                elif map[y + dy][x + dx] == 'E':
                    return dots_path

def find_cheat_spots(grid, waypoints) -> {}:
    cheat_spots = defaultdict(int)

    waypoints_dict = {}
    for i in range(len(waypoints)):
        waypoints_dict[waypoints[i]] = i

    for i in range(len(waypoints)):
        wx, wy = waypoints[i]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if grid[wy + dy][wx + dx] == '#':
                if 0 <= wx + 2*dx < len(grid[0]) and 0 <= wy + 2*dy < len(grid):
                    if grid[wy + 2*dy][wx + 2*dx] == '.':
                        if waypoints_dict[(wx + 2*dx, wy + 2*dy)] - i > 0:
                            cheat_spots[waypoints_dict[(wx + 2*dx, wy + 2*dy)] - i - 2] += 1
                    if grid[wy + 2*dy][wx + 2*dx] == 'E':
                        cheat_spots[len(waypoints) - i - 2] += 1
    return cheat_spots

race_track_dots = find_path(start_pos, grid)
spots = find_cheat_spots(grid, race_track_dots)
print(spots)

total = 0
for idx, val in spots.items():
    if idx >= 100:
        total += val

print(total)
