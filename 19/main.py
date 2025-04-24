def check_towel(towels_data, pattern_data):
    if pattern_data == "":
        return True
    for i in range(len(towels_data)):
        if len(towels_data[i]) > len(pattern_data):
            continue
        if towels_data[i] == pattern_data[0:len(towels_data[i])]:
            if check_towel(towels_data, pattern_data[len(towels_data[i]):]):
                return True
    return False


data = [line.strip() for line in open("input.txt").readlines()]
towels = [towel.strip() for towel in data[0].split(',')]
patterns = data[2:]

counter = 0
for pattern in patterns:
    if check_towel(towels, pattern):
        counter += 1

print(counter)
