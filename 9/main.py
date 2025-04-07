with open('input.txt', 'r') as file:
    input_data = file.read()


free_space_pos = []
resulting_string = []
current_file_id = 0
for idx, char in enumerate(input_data):
    if idx % 2 == 0:
        for i in range(int(char)):
            resulting_string.append(str(current_file_id))
        current_file_id += 1
    else:
        for i in range(int(char)):
            resulting_string.append('.')
            free_space_pos.append(len(resulting_string)-1)

rightmost_occupied = len(resulting_string) - 1

while rightmost_occupied > free_space_pos[0]:
    if resulting_string[rightmost_occupied] != '.':
        position_to_move_to = free_space_pos.pop(0)
        tmp = resulting_string[rightmost_occupied]
        resulting_string[rightmost_occupied] = '.'
        resulting_string[position_to_move_to] = tmp
    rightmost_occupied -= 1


print(resulting_string)
checksum = 0

for idx,char in enumerate(resulting_string):
    if char == '.':
        break
    checksum += idx*int(char)

print(checksum)