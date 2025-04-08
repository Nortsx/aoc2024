import heapq
import sys
from collections import defaultdict, deque

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
lowest_cost = defaultdict(lambda: sys.maxsize * 2)
lowest_cost[(start[0], start[1], 0, 1)] = 0
backtrack = defaultdict(lambda: set())
best_cost = sys.maxsize * 2
finishes = set()

while racePos:
    cost, pos_y, pos_x, direction_y, direction_x = heapq.heappop(racePos)
    if pos_y == end[0] and pos_x == end[1]:
        if cost > best_cost:
            break
        best_cost = cost
        finishes.add((pos_y, pos_x, direction_y, direction_x))
    for newcost, newpos_y, newpos_x, newdirection_y, newdirection_x in [
        (cost + 1, pos_y + direction_y, pos_x + direction_x, direction_y, direction_x),
        (cost + 1000, pos_y, pos_x, direction_x, -direction_y),
        (cost + 1000, pos_y, pos_x, -direction_x, direction_y),
    ]:
        if grid[newpos_y][newpos_x] == '#':
            continue
        else:
            if newcost > lowest_cost[(newpos_y, newpos_x, newdirection_y, newdirection_x)]:
                continue
            if newcost < lowest_cost.get((newpos_y, newpos_x, newdirection_y, newdirection_x)):
                lowest_cost[(newpos_y, newpos_x, newdirection_y, newdirection_x)] = newcost
            backtrack[(newpos_y, newpos_x, newdirection_y, newdirection_x)].add((pos_y, pos_x, direction_y, direction_x))
            heapq.heappush(racePos, (newcost, newpos_y, newpos_x, newdirection_y, newdirection_x))

states = deque(finishes)
seen = set(finishes)

while states:
    state = states.popleft()
    for last in backtrack[state]:
        if last in seen: continue
        seen.add(last)
        states.append(last)

print(len({(r,c) for r,c,_,_ in seen}))
