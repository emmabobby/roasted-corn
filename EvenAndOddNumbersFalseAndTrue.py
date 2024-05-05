def replace_with_booleans(arr):

    return [False if x % 2 == 0 else True for x in arr]

sample_input = [4, 5, 8, 8, 8, 2, 9]
output = replace_with_booleans(sample_input)

print("Output array:", output)