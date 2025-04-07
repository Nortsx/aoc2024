import re


with open('input.txt', 'r') as file:
    input_text = file.read()


pattern = r'(mul\(([0-9]+),([0-9]+)\))|(do\(\))|(don\'t\(\))'

matches = re.findall(pattern, input_text)

product = 0

allowedToMul = True

for match in matches:

    filtered = list(filter(None, match))
    if len(filtered) == 1:
        if filtered[0] == 'do()':
            allowedToMul = True
        else:
            allowedToMul = False
    else:
        if allowedToMul:
            product += int(match[1]) * int(match[2])

print(product)