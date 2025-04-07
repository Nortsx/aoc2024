import time

file_path = 'input.txt'
with open(file_path, 'r') as file:
    input = file.read()
    numbers = list(map(int, input.split()))

def get_digits(num) -> int:
    result = 0
    while num > 0:
        num = num // 10
        result += 1

    return result

start_time = time.time()

times_to_blink = 25

for i in range(times_to_blink):
    new_numbers = []
    for number in numbers:
        if number == 0:
            new_numbers.append(1)
        elif get_digits(number) % 2 == 0:
            str_rep = str(number)
            new_numbers.append(int(str_rep[:len(str_rep)//2]))
            new_numbers.append(int(str_rep[len(str_rep)//2:]))
        else:
            new_numbers.append(number*2024)
    numbers = new_numbers

print(len(numbers))

print("Elapsed:", time.time() - start_time, "s")