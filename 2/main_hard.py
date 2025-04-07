# def checkIfSafe(input_array) -> bool:
#     used_dampener = False
#     ascending = True
#     if input_array[0] > input_array[len(input_array) - 1]:
#         ascending = False
#     current_element_idx = 0
#     index = 1
#     while index < len(input_array):
#         if input_array[index] > input_array[current_element_idx] and not ascending:
#             if not used_dampener:
#                 index += 1
#                 used_dampener = True
#                 continue
#             return False
#         elif input_array[index] < input_array[current_element_idx] and ascending:
#             if not used_dampener:
#                 current_element_idx = index
#                 index += 1
#                 used_dampener = True
#                 continue
#             return False
#         elif input_array[index] == input_array[current_element_idx]:
#             if not used_dampener:
#                 index += 1
#                 used_dampener = True
#                 continue
#             return False
#         elif abs(input_array[index] - input_array[current_element_idx]) > 3:
#             if not used_dampener:
#                 index += 1
#                 used_dampener = True
#                 continue
#             return False
#
#         current_element_idx += 1
#         index += 1
#     return True

def getIsAscending(inputArray) -> bool:
    asc_score = 0
    desc_score = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] > inputArray[i-1]:
            asc_score += 1
        elif inputArray[i] == inputArray[i - 1]:
            continue
        else:
            desc_score += 1

    return asc_score > desc_score


def checkIfSafe(inputArray):
    ascending = getIsAscending(inputArray)
    removed_element = False

    for i in range(len(inputArray)):
        if not compare_element(i, inputArray, ascending) or not check_interval(i, inputArray):
            if not removed_element:
                removed_element = True
                break
            return False

    if removed_element:
        for i in range(len(inputArray)):
            corrected_array = inputArray[:]
            del corrected_array[i]
            if checkSafe(corrected_array, ascending):
                return True

        return False

    return True

def checkSafe(inputArray, ascending):
    for i in range(len(inputArray)):
        if not compare_element(i, inputArray, ascending) or not check_interval(i, inputArray):
            return False

    return True

def compare_element(index, input_array, isAscending):
    if index == 0:
        if isAscending:
            return input_array[index] < input_array[index + 1]
        else:
            return input_array[index] > input_array[index + 1]
    elif index == len(input_array)-1:
        if isAscending:
            return input_array[index] > input_array[index - 1]
        else:
            return input_array[index] < input_array[index - 1]
    else:
        if isAscending:
            return input_array[index - 1] < input_array[index]
        else:
            return input_array[index - 1] > input_array[index]

def check_interval(index, inputArray):
    if index == 0:
        return abs(inputArray[index] - inputArray[index + 1]) <= 3
    elif index == len(inputArray) - 1:
        return abs(inputArray[index] - inputArray[index - 1]) <= 3
    else:
        return abs(inputArray[index] - inputArray[index + 1]) <= 3 and abs(inputArray[index] - inputArray[index - 1]) <= 3

# between 365 and 444
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
    else:
        print(array)

print(safeReports)
