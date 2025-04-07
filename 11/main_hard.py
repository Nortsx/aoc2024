import time
from collections import defaultdict

numbersdict = defaultdict(int)

def get_digits(num) -> int:
    result = 0
    while num > 0:
        num = num // 10
        result += 1

    return result


file_path = 'input.txt'
with open(file_path, 'r') as file:
    input = file.read()
    numbers = list(map(int, input.split()))

for number in numbers:
    numbersdict[number] += 1


start_time = time.time()

times_to_blink = 75

for i in range(times_to_blink):
    print(i)
    newdict = defaultdict(int)
    for number in numbersdict.keys():
        if number == 0:
            newdict[1] += numbersdict[number]
        elif get_digits(number) % 2 == 0:
            str_rep = str(number)
            newdict[int(str_rep[:len(str_rep)//2])] += numbersdict[number]
            newdict[int(str_rep[len(str_rep)//2:])] += numbersdict[number]
        else:
            newdict[number*2024] += numbersdict[number]
    numbersdict = newdict

print(sum(numbersdict.values()))

print("Elapsed:", time.time() - start_time, "s")