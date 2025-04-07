def checkIfSafe(input_array) -> bool:
    ascending = True
    if input_array[0] > input_array[1]:
        ascending = False

    for i in range(1, len(input_array)):
        if input_array[i] > input_array[i - 1] and not ascending:
            return False
        elif input_array[i] < input_array[i - 1] and ascending:
            return False
        elif input_array[i] == input_array[i - 1]:
            return False
        elif abs(input_array[i] - input_array[i - 1]) > 3:
            return False

    return True


# Read the file
with open('input.txt', 'r') as file:  # Replace 'filename.txt' with the actual filename
    lines = file.readlines()

# Parse each line into an array
parsed_arrays = [list(map(int, line.strip().split())) for line in lines]

safeReports = 0
# Print the arrays
for array in parsed_arrays:
    if checkIfSafe(array):
        safeReports += 1

print(safeReports)
