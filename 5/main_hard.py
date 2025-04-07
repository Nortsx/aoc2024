
def checkValidity(array, rules):
    for index in range(len(array)):
        if array[index] in rules:
            for numberAfter in rules[array[index]]:
                for followerIndex in range(len(array)):
                    if array[followerIndex] == numberAfter:
                        if followerIndex < index:
                            return False
    return True


def fixValidity(array, rules):
    index = 0
    while index < len(array):
        if array[index] in rules:
            for numberAfter in rules[array[index]]:
                for followerIndex in range(len(array)):
                    if array[followerIndex] == numberAfter:
                        if followerIndex < index:
                            tmp = array[followerIndex]
                            array[followerIndex] = array[index]
                            array[index] = tmp
                            index = 0
        index += 1

file_path = "input.txt"
with open(file_path, "r") as file:
    data = file.read()


lines = data.strip().split("\n")

# Split the sections
hashmap_lines = []
array_lines = []
delimiter_found = False




for line in lines:
    if ',' in line:
        delimiter_found = True
    if delimiter_found:
        array_lines.append(line)
    else:
        if line != '':
            hashmap_lines.append(line)

# Create the hashmap
rules = {}
for line in hashmap_lines:
    key, value = map(int, line.split("|"))
    if key not in rules:
        rules[key] = []
    rules[key].append(value)

# Create the array of arrays
array_of_arrays = [list(map(int, line.split(','))) for line in array_lines]

correct_sum = 0


for line in array_of_arrays:
    if not checkValidity(line, rules):
        print(line)
        fixValidity(line, rules)
        print(line)
        correct_sum += line[len(line) // 2]

print(correct_sum)