import re


with open('input.txt', 'r') as file:
    input_text = file.read()


pattern = r'mul\(([0-9]+),([0-9]+)\)'

matches = re.findall(pattern, input_text)

product = 0

for match in matches:
    product += int(match[0])*int(match[1])

print(product)