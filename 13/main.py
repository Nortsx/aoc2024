import re

def parse_button(data):
    blocks = data.strip().split("\n\n")

    results = []

    for block in blocks:
        entry = {}
        lines = block.split("\n")

        for line in lines:
            match = re.match(r"(Button [AB]|Prize): X[+=](\d+), Y[+=](\d+)", line)
            if match:
                key = match.group(1)
                x = int(match.group(2))
                y = int(match.group(3))
                entry[key] = {'X': x, 'Y': y}

        results.append(entry)

    return results

file_path = 'input.txt'
with open(file_path, 'r') as file:
    data = parse_button(file.read())


total = 0

for entry in data:
    minSum = -1
    for mulA in range(0, 100):
        for mulB in range(0, 100):
            if mulA % 10000 == 0 and mulB % 10000 == 0:
                print(mulA, mulB)
            if mulA*entry['Button A']['X'] + mulB*entry['Button B']['X'] == entry['Prize']['X'] and mulA*entry['Button A']['Y'] + mulB*entry['Button B']['Y'] == entry['Prize']['Y']:
                if minSum == -1:
                    minSum = mulA*3 + mulB
                else:
                    minSum = min(minSum, mulA*3 + mulB)
    if minSum > 0:
        total += minSum

print(total)