import time


def parse_file_to_2d_array(file_path):
    with open(file_path, 'r') as file:
        # Read all lines, stripping the newline character
        return [list(line.strip()) for line in file.readlines()]

def detectLoop(startPosition, grid) -> bool:
    coords_set = set()
    current_position = startPosition
    current_direction = (0, -1)
    coords_set.add(str(current_position[0]) + ":" + str(current_position[1]) + "dir" + str(current_direction[0]) + "|" + str(current_direction[1]))
    while True:
        new_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
        if new_position[0] < 0 or new_position[0] >= len(grid) or new_position[1] < 0 or new_position[1] >= len(grid[0]):
            return False
        else:
            if grid[new_position[1]][new_position[0]] == ".":
                if (str(new_position[0]) + ":" + str(new_position[1]) + "dir" + str(current_direction[0]) + "|" + str(current_direction[1])) in coords_set:
                    return True
                coords_set.add(str(new_position[0]) + ":" + str(new_position[1])  + "dir" + str(current_direction[0]) + "|" + str(current_direction[1]))
                current_position = new_position
            else:
                current_direction = turn(current_direction)


def turn(current_direction) -> (int, int):
    if current_direction == (0, -1):
        return 1, 0
    elif current_direction == (1, 0):
        return 0, 1
    elif current_direction == (0, 1):
        return -1, 0
    else:
        return 0, -1

# Example usage
file_path = "input.txt"
grid = parse_file_to_2d_array(file_path)

coordsSet = set()

startTime = time.time()*1000.0

currentGuardPosition = (0, 0)
possibleCrates = []
# Print the 2D array
for posY in range(len(grid)):
    for posX in range(len(grid[posY])):
        if grid[posY][posX] == "^":
            currentGuardPosition = (posX, posY)
            grid[posY][posX] = "."
        elif grid[posY][posX] == ".":
            possibleCrates.append((posX, posY))

possibleLoops = 0

for idx, possibleCratePosition in enumerate(possibleCrates):
    if idx % 100 == 0:
        print(idx, "/", len(possibleCrates))
    grid[possibleCratePosition[1]][possibleCratePosition[0]] = "#"
    if detectLoop(currentGuardPosition, grid):
        possibleLoops += 1
    grid[possibleCratePosition[1]][possibleCratePosition[0]] = "."

print(possibleLoops)

delta = time.time()*1000.0 - startTime
print(delta)