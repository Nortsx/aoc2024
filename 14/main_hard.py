import re
from collections import defaultdict


def build_map_and_save_to_file(posdict, maxX, maxY, filename):
    dots = [['.' for _ in range(maxX)] for _ in range(maxY)]

    for pos in posdict:
        dots[pos[1]][pos[0]] = '*'
    with open(filename, 'w') as file:
        for row in dots:
            file.write(''.join(row) + '\n')
class Robot:
    positionX = 0
    positionY = 0
    velocityX = 0
    velocityY = 0

    def __init__(self, positionX, positionY, velocityX, velocityY):
        self.positionX = positionX
        self.positionY = positionY
        self.velocityX = velocityX
        self.velocityY = velocityY

    def move(self, constraintX, constraintY):
        self.positionX += self.velocityX
        self.positionY += self.velocityY

        if self.positionX >= constraintX:
            self.positionX = self.positionX - constraintX
        if self.positionX < 0:
            self.positionX = constraintX + self.positionX

        if self.positionY >= constraintY:
            self.positionY = self.positionY - constraintY
        if self.positionY < 0:
            self.positionY = constraintY + self.positionY


file_path = 'input.txt'
robots = []

constraintX = 101
constraintY = 103

with open(file_path, 'r') as file:
    for line in file.readlines():
        line = line.strip()
        match = re.match(r'p=(\d+),(\d+)\sv=(-*\d+),(-*\d+)', line)
        if match:
            posX = int(match.group(1))
            posY = int(match.group(2))
            velX = int(match.group(3))
            velY = int(match.group(4))
            robots.append(Robot(posX, posY, velX, velY))

def isTrunk(pos, posDict):
    for i in range(3):
        for j in range(3):
            if (pos[0] + i, pos[1] + j) not in posDict:
                return False
    return True

for i in range(0, 100000):
    posDict = defaultdict(int)
    for robot in robots:
        posDict[(robot.positionX, robot.positionY)] += 1
        robot.move(constraintX, constraintY)
    for pos in posDict:
        if isTrunk(pos, posDict):
            print(i)
            build_map_and_save_to_file(posDict, constraintX, constraintY, 'maps/map_{}.txt'.format(i))
            break

# 1000 is too low 100000 is too high
