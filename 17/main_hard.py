cmdLine = ''

for line in open("input.txt").readlines():
    if line.startswith("Program:"):
        cmdLine = line.split(":")[1].strip().split(",")


cmdLine = [int(x) for x in cmdLine]


def search(commands, answer):
    if not commands:
        return answer
    for shift in range(0, 8):
        a = (answer << 3) + shift
        b = a % 8
        b = b ^ 1
        c = a >> b
        b = b ^ 5
        b = b ^ c
        if b % 8 == commands[-1]:
            pre_answer = search(commands[:-1], a)
            if pre_answer is None: continue
            return pre_answer

print(search(cmdLine, 0))