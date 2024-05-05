def find_longest_word(word_list):
    longest_word = ''
    longest_size = 0

    for word in word_list:
        if len(word) > longest_size:
            longest_word = word
            longest_size = len(word)

    return longest_word, longest_size

words = ['Python', 'development', 'tutorial', 'longest', 'list', 'words']
longest_word, length_of_longest = find_longest_word(words)
print(f"The longest word is '{longest_word}' and its length is {length_of_longest}.")