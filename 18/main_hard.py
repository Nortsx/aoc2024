from queue import Queue

def getGrid(size):
    return [['.' for _ in range(size)] for _ in range(size)]

def fillGrid(grid, data):
    for i in range(len(data)):
        x,y = map(int, data[i].split(','))
        grid[y][x] = '#'
    return grid

def checkReachability(grid, start_pos, end_pos):
    visited = set()
    q = Queue()
    visited.add(start_pos)
    q.put(start_pos)

    while not q.empty():
        x,y = q.get()
        for nx, ny in [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]:
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid):
                continue
            if grid[ny][nx] == '#':
                continue
            if (nx, ny) == end_pos:
                return True
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            q.put((nx, ny))

    return False

data = [line.strip() for line in open("input.txt").readlines()]

size = int(data[0])

tiles = data[1:]
dataSize = len(tiles)
end_pos = (size - 1, size - 1)

for i in range(1024, dataSize):
    grid = getGrid(size)
    grid = fillGrid(grid, tiles[1:i])

    result = checkReachability(grid, (0,0), end_pos)
    if not result:
        print(tiles[i - 1])
        break
