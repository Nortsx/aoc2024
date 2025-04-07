
words = []

with open('input.txt', 'r') as file:
    for line in file:
        # Remove trailing newline characters and split the line into characters
        row = list(line.strip())
        words.append(row)

def count_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])  # Get grid dimensions
    word_length = len(word)
    directions = [
        (0, 1),    # Horizontal right
        (0, -1),   # Horizontal left
        (1, 0),    # Vertical down
        (-1, 0),   # Vertical up
        (1, 1),    # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),   # Diagonal down-left
        (-1, 1)    # Diagonal up-right
    ]

    def is_valid(x, y, dx, dy):
        """Check if the word can fit in this direction."""
        return 0 <= x + dx * (word_length - 1) < rows and 0 <= y + dy * (word_length - 1) < cols

    def match(x, y, dx, dy):
        """Check if the word matches in this direction."""
        for i in range(word_length):
            if grid[x + i * dx][y + i * dy] != word[i]:
                return False
        return True

    count = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_valid(x, y, dx, dy) and match(x, y, dx, dy):
                    count += 1

    return count

# Count occurrences of "XMAS"
result = count_xmas(words)

# Print the result
print(f"Total occurrences of 'XMAS': {result}")