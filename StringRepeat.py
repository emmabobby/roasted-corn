def repeat_string(s, n):
    if isinstance(n, float):
        return s
    else:
        return s * n

print(repeat_string('hello', 3))  
print(repeat_string('hi', 4.5))   