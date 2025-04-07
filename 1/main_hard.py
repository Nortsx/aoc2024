def parse_input(input_text):
    # Split the input.txt text into lines
    lines = input_text.strip().split("\n")

    # Initialize the arrays
    left = []
    right = []

    # Process each line
    for line in lines:
        # Split the line into two numbers
        num1, num2 = map(int, line.split())
        # Append the numbers to respective arrays
        left.append(num1)
        right.append(num2)

    return left, right

with open('input.txt', 'r') as file:
    input_text = file.read()

# Parse the input.txt
left, right = parse_input(input_text)

left.sort()

distance = 0
saved_element = 0
for idx, element in enumerate(left):
    multiplier = 0
    for i in range(0, len(right)):
        if element == right[i]:
            multiplier += 1

    distance += multiplier*element

# Output the results
print("Left:", distance)