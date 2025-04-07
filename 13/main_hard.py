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


def calculate(button_ax, button_ay, button_bx, button_by, goal_x, goal_y):
    mul_b = ((button_ay * goal_x) - (button_ax * goal_y)) // (button_ay*button_bx - button_ax*button_by)
    mul_a = (goal_x - button_bx * mul_b) // button_ax

    if button_ax * mul_a + button_bx * mul_b == goal_x and button_ay * mul_a + button_by * mul_b == goal_y:
        return mul_a*3 + mul_b
    else:
        return -1


total = 0

for entry in data:
    goal_x = 10000000000000 + entry['Prize']['X']
    goal_y = 10000000000000 + entry['Prize']['Y']
    sum = calculate(entry['Button A']['X'], entry['Button A']['Y'], entry['Button B']['X'], entry['Button B']['Y'], goal_x, goal_y)

    if sum > 0:
        total += sum

print(total)

