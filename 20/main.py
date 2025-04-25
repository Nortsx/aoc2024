from collections import defaultdict

grid = [[elem for elem in line.strip()] for line in open("input.txt").readlines()]
print(grid)

start_pos = (0, 0)
end_post = (0, 0)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            start_pos = (x, y)
        if grid[y][x] == 'E':
            end_pos = (x, y)
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

race_track_dots = find_path(start_pos, grid)
race_track_dots.append(end_pos)

cheats = defaultdict(int)

for first_cheat_index in range(len(race_track_dots)):
    for potential_cheat_index in range(first_cheat_index + 1, len(race_track_dots)):
        earlier_dot = race_track_dots[first_cheat_index]
        later_dot = race_track_dots[potential_cheat_index]
        if (earlier_dot[1] == later_dot[1] and abs(earlier_dot[0] - later_dot[0]) == 2) or (earlier_dot[0] == later_dot[0] and abs(earlier_dot[1] - later_dot[1]) == 2):
            if potential_cheat_index - first_cheat_index - 2 > 0:
                cheats[potential_cheat_index - first_cheat_index - 2] += 1
print(cheats)

total = 0
for idx, val in cheats.items():
    if idx >= 100:
        total += val

print(total)
