def palindrome(string):
    word = ""
    count = len(string) - 1

    while count >= 0:
        word += string[count]
        count -= 1
    return word == string