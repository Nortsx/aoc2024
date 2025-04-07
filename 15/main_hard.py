def generate_extended_map(old_map_file_path, new_map_file_path):
    with open(old_map_file_path, 'r') as old_map_file:
        data = old_map_file.read()
    map = data.split('\n\n')[0]
    moves = data.split('\n\n')[1]
    newmap = []

    maplines = map.split('\n')
    for line in maplines:
        new_line = []
        for symbol in line:
            if symbol == '#' or symbol == '.':
                new_line.append(symbol)
                new_line.append(symbol)
            elif symbol == 'O':
                new_line.append('[')
                new_line.append(']')
            elif symbol == '@':
                new_line.append(symbol)
                new_line.append('.')
        newmap.append(''.join(new_line)+"\n")
    with open(new_map_file_path, 'w') as new_map_file_path:
        new_map_file_path.write("".join(newmap) + "\n" + moves)


old_input = 'input.txt'
new_input = 'hard_input.txt'

generate_extended_map(old_input, new_input)

with open(new_input, 'r') as file:
    data = file.read()

array_data = data.split("\n\n")[0]
moves_data = data.split("\n\n")[1]

def parse_file_to_2d_dict(data) -> (dict, (int, int)):
    array_coords = data.split("\n")
    result = {}
    start_pos = (0, 0)
    for y, line in enumerate(array_coords):
        for x, val in enumerate(line):
            if val in ['[', ']', '#']:
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
    '<': (-1, 0),
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
}

offsets = {'[': 1, ']': -1}

def stack_boxes_horizontally(crates_boxes_dict, current_pos, new_pos, direction) -> (int, int):
    stack = [(current_pos, '@'), (new_pos, crates_boxes_dict[new_pos])]
    while True:
        stack_pos = stack[-1][0]
        new_stack_pos = (stack_pos[0] + direction[0], stack_pos[1] + direction[1])
        if new_stack_pos not in crates_boxes_dict:
            break
        elif crates_boxes_dict[new_stack_pos] == '#':
            stack = []
            break
        elif crates_boxes_dict[new_stack_pos] in ['[',']']:
            stack.append((new_stack_pos, crates_boxes_dict[new_stack_pos]))
    while len(stack) > 0:
        entity = stack.pop()
        if entity[1] in ['[',']']:
            del crates_boxes_dict[entity[0]]
            crates_boxes_dict[(entity[0][0] + direction[0], entity[0][1] + direction[1])] = entity[1]
        else:
            current_pos = (entity[0][0] + direction[0], entity[0][1] + direction[1])

    return current_pos

def stack_boxes_vertically(crates_boxes_dict, current_pos, new_pos, direction) -> (int, int):
    stack = [set()]
    current_offset = offsets[crates_boxes_dict[new_pos]]
    second_part = (new_pos[0] + current_offset, new_pos[1])
    stack[-1].add(new_pos)
    stack[-1].add(second_part)
    while len(stack[-1]) > 0:
        stack_set = stack[-1]
        stack.append(set())
        for crate_part in stack_set:
            new_stack_pos = (crate_part[0] + direction[0], crate_part[1] + direction[1])
            if new_stack_pos not in crates_boxes_dict:
                continue
            elif crates_boxes_dict[new_stack_pos] == '#':
                return current_pos
            else:
                stack[-1].add(new_stack_pos)
                current_offset = offsets[crates_boxes_dict[new_stack_pos]]
                second_part = (new_stack_pos[0] + current_offset, new_stack_pos[1])
                stack[-1].add(second_part)

    while len(stack) > 0:
        elements = stack.pop()
        for element_pos in elements:
            tmp = crates_boxes_dict[element_pos]
            del crates_boxes_dict[element_pos]
            new_elem_pos = (element_pos[0] + direction[0], element_pos[1] + direction[1])
            crates_boxes_dict[new_elem_pos] = tmp

    return current_pos[0] + direction[0], current_pos[1] + direction[1]


current_pos = start_pos
for move in movements:
    direction = directions[move]
    new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    if new_pos not in crates_boxes_dict:
        current_pos = new_pos
    elif crates_boxes_dict[new_pos] == '#':
        continue
    elif crates_boxes_dict[new_pos] in ['[',']']:
        if move in ['<','>']:
            current_pos = stack_boxes_horizontally(crates_boxes_dict, current_pos, new_pos, direction)
        else:
            current_pos = stack_boxes_vertically(crates_boxes_dict, current_pos, new_pos, direction)



gps_coords = 0
for key in crates_boxes_dict:
    print(key)
    if crates_boxes_dict[key] == '[':
        gps_coords += (key[0] + 100 * key[1])

print(gps_coords)