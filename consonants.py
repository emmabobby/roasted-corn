def count_vowels_and_consonants(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0

    for letter in word:
        if letter.lower() in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return {'vowels': vowel_count, 'consonants': consonant_count}

word = "aabc"
result = count_vowels_and_consonants(word)
print("consonants:", result['consonants'])
print("vowels:", result['vowels'])