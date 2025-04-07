with open('input.txt', 'r') as file:
    input_data = file.read()

free_space_pos = []
file_chunks = []

current_file_id = 0
total_pos = 0
for idx, char in enumerate(input_data):
    if idx % 2 == 0:
        file_chunks.append((total_pos, int(char), current_file_id))
        current_file_id += 1
    else:
        free_space_pos.append((total_pos, int(char)))
    total_pos += int(char)


for file_chunk_idx in range(len(file_chunks)-1, 0, -1):
    file_pos = file_chunks[file_chunk_idx][0]
    file_length = file_chunks[file_chunk_idx][1]
    free_space_removal_index = -1
    for idx, free_space in enumerate(free_space_pos):
        if free_space[1] >= file_length and free_space[0] < file_pos:
            file_chunks[file_chunk_idx] = (free_space[0], file_length, file_chunks[file_chunk_idx][2])
            free_space_pos[idx] = (free_space[0] + file_length, free_space[1] - file_length)
            if free_space_pos[idx][1] == 0:
                free_space_removal_index = idx
            break
    if free_space_removal_index != -1:
        del free_space_pos[free_space_removal_index]

file_chunks.sort(key=lambda x: x[0])

resulting_string = []

for idx, file_chunk in enumerate(file_chunks):
    for i in range(file_chunk[1]):
        resulting_string.append(file_chunk[2])
    if idx < len(file_chunks) - 1:
        padding = file_chunks[idx + 1][0] - (file_chunks[idx][0] + file_chunks[idx][1])
        resulting_string.extend(['.']*padding)

checksum = 0

for idx, char in enumerate(resulting_string):
    if char != '.':
        checksum += idx*char

print(checksum)