codes = []

file_path = "input.txt"

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()  # Remove any surrounding whitespace
        if line.isdigit():  # Check if the line is an integer
            codes.append(int(line))


def mix(secret, new):
    return new ^ secret

def prune(secret) -> int:
    return secret % 16777216

sum = 0
for code in codes:
    secret_num = code
    for i in range(2000):
        res = secret_num*64
        secret_num = prune(mix(secret_num, res))
        res = secret_num // 32
        secret_num = prune(mix(secret_num, res))
        res = secret_num * 2048
        secret_num = prune(mix(secret_num, res))
    sum += secret_num

print(sum)
