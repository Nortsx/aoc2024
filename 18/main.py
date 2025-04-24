import heapq

data = [line.strip() for line in open("input.txt").readlines()]

size = int(data[0])

grid = [['.' for _ in range(size)] for _ in range(size)]

for i in range(1, 1025):
    x,y = map(int, data[i].split(','))
    print(x, y)
    grid[y][x] = '#'


end_pos = (size - 1 , size - 1)

visited = set()
closest_distance = []

heapq.heappush(closest_distance, (0, 0, 0))
visited.add((0, 0))
while True:
    current_distance, x, y  = heapq.heappop(closest_distance)
    for new_distance, nx, ny in [
        (current_distance + 1, x + 1, y),
        (current_distance + 1, x - 1, y),
        (current_distance + 1, x, y + 1),
        (current_distance + 1, x, y - 1),
    ]:
        if (nx, ny) == end_pos:
            print("DISTANCE")
            print(current_distance)
            break
            break
        if (nx, ny) in visited:
            continue
        if nx < 0 or nx >= size or ny < 0 or ny >= size:
            continue
        if grid[ny][nx] == '#':
            continue
        visited.add((nx, ny))
        heapq.heappush(closest_distance, (new_distance, nx, ny))
