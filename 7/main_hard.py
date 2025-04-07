def concatenate(a, b) -> int:
    return int(str(a) + str(b))


def combine_numbers(array,index, prev_sum, sum_to_compare):
    if index == len(array):
        return prev_sum == sum_to_compare
    else:
        return (combine_numbers(array, index+1, prev_sum+array[index], sum_to_compare)
        or combine_numbers(array, index+1, prev_sum*array[index], sum_to_compare)
        or combine_numbers(array, index+1, concatenate(prev_sum,array[index]), sum_to_compare))


with open('input.txt', 'r') as file:
    input_data = file.read()

result = 0
for line in input_data.strip().split("\n"):
    before_colon, after_colon = line.split(":")
    product = int(before_colon.strip())
    values = list(map(int, after_colon.strip().split()))
    if combine_numbers(values, 1, values[0], product):
        result += product

print(result)