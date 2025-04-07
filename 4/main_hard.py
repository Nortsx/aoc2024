words = []

with open('input.txt', 'r') as file:
    for line in file:
        # Remove trailing newline characters and split the line into characters
        row = list(line.strip())
        words.append(row)

def checkMS(words, posX, posY):
    if posX -1 >= 0 and posX +1 < len(words) and posY -1 >= 0 and posY +1 < len(words):
        firstDiagonal = words[posX + 1][posY - 1] + words[posX - 1][posY + 1]
        secondDiagonal = words[posX - 1][posY - 1] + words[posX + 1][posY + 1]
        return (firstDiagonal == 'SM' or firstDiagonal == 'MS') and (secondDiagonal == 'SM' or secondDiagonal == 'MS')
    return False

total_count = 0

for i in range(0, len(words)):
    for j in range(0, len(words[i])):
        if words[i][j] == 'A':
            if checkMS(words, i, j):
                total_count += 1

print(total_count)