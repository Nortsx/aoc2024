

registerA = 0
registerB = 0
registerC = 0

commandLine = ''
output = []

def extractOperand(operand, opcode):
    if opcode in [1,3]:
        return int(operand)

    if operand <= 3:
        return operand
    elif operand == 4:
        return registerA
    elif operand == 5:
        return registerB
    elif operand == 6:
        return registerC


for line in open("input.txt").readlines():
    if line.startswith("Register A:"):
        registerA = int(line.split(":")[1].strip())
    if line.startswith("Register B:"):
        registerB = int(line.split(":")[1].strip())
    if line.startswith("Register C:"):
        registerC = int(line.split(":")[1].strip())
    if line.startswith("Program:"):
        commandLine = line.split(":")[1].strip().split(",")


position = 0
while position < len(commandLine):
    command = commandLine[position].strip()
    operand = commandLine[position + 1]

    opcode = int(command)
    operandValue = extractOperand(int(operand), opcode)

    if opcode == 0:
        registerA = int(registerA / pow(2,operandValue))
    elif opcode == 1:
        registerB = registerB ^ operandValue
    elif opcode == 2:
        registerB = operandValue % 8
    elif opcode == 3:
        if registerA != 0:
            position = operandValue
            continue
    elif opcode == 4:
        registerB = registerB ^ registerC
    elif opcode == 5:
        output.append(operandValue % 8)
    elif opcode == 6:
        registerB = int(registerA / pow(2,operandValue))
    elif opcode == 7:
        registerC = int(registerA / pow(2,operandValue))

    position += 2

print(registerA)
print(registerB)
print(registerC)

print(','.join(map(str, output)))