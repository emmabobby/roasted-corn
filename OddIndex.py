def remove_odd_indices(s):
    return ''.join([char for index, char in enumerate(s) if index % 2 == 0])

sample_data = "Semicolon"
print(remove_odd_indices(sample_data))  