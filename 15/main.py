
file_path = 'input.txt'

with open(file_path, 'r') as file:
    data = file.read()

array_data = data.split("\n\n")[0]
moves_data = data.split("\n\n")[1]



def parse_file_to_2d_dict(data) -> (dict, (int, int)):
    array_coords = data.split("\n")
    result = {}
    start_pos = (0, 0)
    for y, line in enumerate(array_coords):
        for x, val in enumerate(line):
            if val == 'O' or val == '#':
                result[(x, y)] = val
            elif val == '@':
                start_pos = (x, y)
    return result, start_pos

def parse_movements(data) -> list:
    movements_line = data.replace("\n", "")
    return movements_line


crates_boxes_dict, start_pos = parse_file_to_2d_dict(array_data)
movements = parse_movements(moves_data)

directions = {
    '<' : (-1, 0),
    '^' : (0, -1),
    '>' : (1, 0),
    'v' : (0, 1),
}

current_pos = start_pos
for move in movements:
    direction = directions[move]
    new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    if new_pos not in crates_boxes_dict:
        current_pos = new_pos
    elif crates_boxes_dict[new_pos] == '#':
        continue
    elif crates_boxes_dict[new_pos] == 'O':
        stack = [(current_pos, '@'), (new_pos, 'O')]
        while True:
            stack_pos = stack[-1][0]
            new_stack_pos = (stack_pos[0] + direction[0], stack_pos[1] + direction[1])
            if new_stack_pos not in crates_boxes_dict:
                break
            elif crates_boxes_dict[new_stack_pos] == '#':
                stack = []
                break
            elif crates_boxes_dict[new_stack_pos] == 'O':
                stack.append((new_stack_pos, 'O'))
        while len(stack) > 0:
            entity = stack.pop()
            if entity[1] == 'O':
                del crates_boxes_dict[entity[0]]
                crates_boxes_dict[(entity[0][0] + direction[0], entity[0][1] + direction[1])] = entity[1]
            else:
                current_pos = (entity[0][0] + direction[0], entity[0][1] + direction[1])
    print(move)

gps_coords = 0
for key in crates_boxes_dict:
    print(key)
    if crates_boxes_dict[key] == 'O':
        gps_coords += (key[0] + 100 * key[1])

print(gps_coords)