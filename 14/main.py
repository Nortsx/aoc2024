import re
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

for i in range(0, 100):
    for robot in robots:
        robot.move(constraintX, constraintY)


midpointX = constraintX // 2
midpointY = constraintY // 2

quadrants = [
    (0,0,midpointX - 1,midpointY - 1), # top left 0
    (midpointX + 1,0,constraintX-1,midpointY-1), # top right 1
    (0,midpointY+1,midpointX -1 ,constraintY - 1), # bottom left 2
    (midpointX + 1,midpointY + 1,constraintX - 1,constraintY - 1) #bottom right 3
]

quadrants_sum = [0,0,0,0]

for robot in robots:
    for idx, quadrant in enumerate(quadrants):
        if quadrant[0] <= robot.positionX <= quadrant[2] and quadrant[1] <= robot.positionY <= quadrant[3]:
            print(robot.positionX, robot.positionY, idx)
            quadrants_sum[idx] += 1


total = 1
for qsum in quadrants_sum:
    total *= qsum

print(total)