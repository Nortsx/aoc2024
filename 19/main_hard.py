
def check_towel(towels_data, pattern_data):
    if pattern_data == "":
        return 1
    if pattern_data in memo:
        return memo[pattern_data]
    count = 0
    for i in range(len(towels_data)):
        if len(towels_data[i]) > len(pattern_data):
            continue
        if towels_data[i] == pattern_data[:len(towels_data[i])]:
            count += check_towel(towels_data, pattern_data[len(towels_data[i]):])
            memo[pattern_data] = count
    return count

data = [line.strip() for line in open("input.txt").readlines()]
towels = [towel.strip() for towel in data[0].split(',')]
patterns = data[2:]

total = 0
for pattern in patterns:
    memo = {}
    total += check_towel(towels, pattern)

print(total)