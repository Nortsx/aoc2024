def parse_file_to_2d_array(file_path):
    with open(file_path, 'r') as file:
        # Read all lines, stripping the newline character
        return [list(line.strip()) for line in file.readlines()]

# Example usage
file_path = "input.txt"
grid = parse_file_to_2d_array(file_path)

coordsSet = set()
currentDirection = (0, -1)
currentPosition = (0, 0)
# Print the 2D array
for posY in range(len(grid)):
    for posX in range(len(grid[posY])):
        if grid[posY][posX] == "^":
            coordsSet.add(str(posX)+":"+str(posY))
            currentPosition = (posX, posY)
            grid[posY][posX] = "."

while True:
    newPosition = (currentPosition[0] + currentDirection[0], currentPosition[1] + currentDirection[1])
    if newPosition[0] < 0 or newPosition[0] >= len(grid) or newPosition[1] < 0 or newPosition[1] >= len(grid[0]):
        print(len(coordsSet))
        break
    else:
        if grid[newPosition[1]][newPosition[0]] == ".":
            coordsSet.add(str(newPosition[0])+":"+str(newPosition[1]))
            currentPosition = newPosition
        else:
            if currentDirection == (0, -1):
                currentDirection = (1, 0)
            elif currentDirection == (1, 0):
                currentDirection = (0, 1)
            elif currentDirection == (0, 1):
                currentDirection = (-1, 0)
            else:
                currentDirection = (0, -1)


