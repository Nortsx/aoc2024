import string
from functools import cache
inputs = [entry.strip() for entry in open("input.txt").readlines()]
print(inputs)

keypad = {}

keypad_positions_mapping = {}

keypad_positions_mapping[(2,3)] = 'A'
keypad_positions_mapping[(1,3)] = '0'
keypad_positions_mapping[(0,3)] = 'X'

keypad_positions_mapping[(0,2)] = '1'
keypad_positions_mapping[(1,2)] = '2'
keypad_positions_mapping[(2,2)] = '3'

keypad_positions_mapping[(0,1)] = '4'
keypad_positions_mapping[(1,1)] = '5'
keypad_positions_mapping[(2,1)] = '6'

keypad_positions_mapping[(0,0)] = '7'
keypad_positions_mapping[(1,0)] = '8'
keypad_positions_mapping[(2,0)] = '9'

keypad['A'] = (2,3)
keypad['0'] = (1,3)
keypad['X'] = (0,3)

keypad['1'] = (0,2)
keypad['2'] = (1,2)
keypad['3'] = (2,2)

keypad['4'] = (0,1)
keypad['5'] = (1,1)
keypad['6'] = (2,1)

keypad['7'] = (0,0)
keypad['8'] = (1,0)
keypad['9'] = (2,0)


cp = {}
cp['A'] = (2,0)
cp['^'] = (1,0)
cp['X'] = (0,0)

cp['<'] = (0,1)
cp['v'] = (1,1)
cp['>'] = (2,1)

def getDifference(a, b):
    return (a[0] - b[0], a[1] - b[1])

def calculate_path_for_horizontal_difference(difference):
    output = ''
    if difference > 0:
        for i in range(difference):
            output += '>'
    elif difference < 0:
        for i in range(-difference):
            output += '<'

    return output

def calculate_path_for_vertical_difference(difference):
    output = ''
    if difference > 0:
        for i in range(difference):
            output += 'v'
    elif difference < 0:
        for i in range(-difference):
            output += '^'

    return output


def calculate_short_path_for_keypad(entry, keypad) -> string:
    currentSymbol = 'A'
    currentPosition = keypad[currentSymbol]
    output = ''
    for sign in entry:
        difference = getDifference(keypad[sign], currentPosition)
        if currentSymbol in ['7', '4', '1'] and sign in ['0', 'A']:
            output += calculate_path_for_horizontal_difference(difference[0])
            output += calculate_path_for_vertical_difference(difference[1])
        else:
            output += calculate_path_for_vertical_difference(difference[1])
            output += calculate_path_for_horizontal_difference(difference[0])
        output += 'A'
        currentSymbol = sign
        currentPosition = keypad[sign]

    return output

def get_all_shortest_keypad_paths(entry, keypad, number_paths) -> []:
    finalSet = []
    currentSymbol = 'A'
    currentPosition = keypad[currentSymbol]
    for idx, symbol in enumerate(entry):
        max_length = len(number_paths[idx])
        results = []
        get_possible_paths_of_length(keypad, symbol, currentPosition, '', max_length, results)
        finalSet.append(results)
        currentPosition = keypad[symbol]
    return finalSet

def get_possible_paths_of_length(keypad, symbolToReach, currentPosition, currentLine, maxLength, positions):
    if len(currentLine) == maxLength:
        if keypad_positions_mapping[currentPosition] == symbolToReach:
            positions.append(currentLine)
        return
    possible_directions = ['>', '<', 'v', '^']
    possible_directions_shift = [(1,0), (-1,0), (0,1), (0,-1)]
    for idx, direction in enumerate(possible_directions):
        newPos = (currentPosition[0] + possible_directions_shift[idx][0], currentPosition[1] + possible_directions_shift[idx][1])
        if 0 <= newPos[0] < 3 and 0 <= newPos[1] < 4 and newPos != keypad['X']:
            get_possible_paths_of_length(keypad, symbolToReach, newPos, currentLine + direction, maxLength, positions)

def calculate_path_for_cp(entry):
    currentSymbol = entry[0]
    currentPosition = cp[currentSymbol]
    output = ''

    for i in range(1, len(entry)):
        sign = entry[i]
        difference = getDifference(cp[sign], currentPosition)
        if currentSymbol in ['A', '^'] and sign in ['<']:
            output += calculate_path_for_vertical_difference(difference[1])
            output += calculate_path_for_horizontal_difference(difference[0])
        else:
            output += calculate_path_for_horizontal_difference(difference[0])
            output += calculate_path_for_vertical_difference(difference[1])
        output += 'A'
        currentSymbol = sign
        currentPosition = cp[sign]

    return output


@cache
def get_amount_of_symbols_for_depth(route, current_depth, max_depth):
    path = calculate_path_for_cp(route)
    if current_depth == max_depth:
        return len(path)

    res = 0
    for i in range(0, len(path)):
        if i == 0:
            entry = 'A' + path[i]
        else:
            entry = path[i-1:i+1]
        res += get_amount_of_symbols_for_depth(entry, current_depth + 1, max_depth)

    return res

def combine_paths(provided_paths, current_path, idx, results):
    if idx == len(provided_paths):
        results.append(current_path)
        return
    for path in provided_paths[idx]:
        combine_paths(paths, current_path + path + 'A', idx + 1, results)

total = 0
number_of_robots = 2
for code in inputs:
    first_pad_path = calculate_short_path_for_keypad(code, keypad)
    print(first_pad_path)
    paths = first_pad_path.split('A')
    paths = paths[:-1]
    print(paths)
    paths = get_all_shortest_keypad_paths(code, keypad, paths)
    combined_paths = []
    combine_paths(paths, '', 0, combined_paths)
    print(combined_paths)
    current_total = 100000000000000000000000
    for path_variant in combined_paths:
        current_pad = path_variant
        print(get_amount_of_symbols_for_depth(path_variant, 0, 1))
#         for i in range(number_of_robots):
#             current_pad = calculate_path_for_cp(current_pad)
#             print(len(current_pad))
#             print(i)
#         parsed_integer = int(code[:-1])
#         if current_total > parsed_integer * len(current_pad):
#             current_total = parsed_integer * len(current_pad)
#     total += current_total
# print(total)
