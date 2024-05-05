def replace_with_ones_and_zeros(arr):
        return [0 if x % 2 == 0 else 1 for x in arr]

sample_input = [4, 5, 8, 8, 8, 2, 9]
output = replace_with_ones_and_zeros(sample_input)
print("Output array:",output)