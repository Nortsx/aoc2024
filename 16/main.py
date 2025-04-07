import heapq

grid = [list(line.strip()) for line in open("input.txt").readlines()]

rows = len(grid)
cols = len(grid[0])


for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "S":
            start = (row, col)
        elif grid[row][col] == "E":
            end = (row, col)

racePos = [(0, start[0], start[1], 0, 1)]
seen = {(start[0], start[1], 0, 1)}
while racePos:
    cost, pos_y, pos_x, direction_y, direction_x = heapq.heappop(racePos)
    seen.add((pos_y, pos_x, direction_y, direction_x))
    if pos_y == end[0] and pos_x == end[1]:
        print(cost)
        break
    for newcost, newpos_y, newpos_x, newdirection_y, newdirection_x in [
        (cost + 1, pos_y + direction_y, pos_x + direction_x, direction_y, direction_x),
        (cost + 1000, pos_y, pos_x, direction_x, -direction_y),
        (cost + 1000, pos_y, pos_x, -direction_x, direction_y),
    ]:
        if grid[newpos_y][newpos_x] == '#':
            continue
        if (newpos_y, newpos_x, newdirection_y, newdirection_x) in seen:
            continue
        else:
            heapq.heappush(racePos, (newcost, newpos_y, newpos_x, newdirection_y, newdirection_x))