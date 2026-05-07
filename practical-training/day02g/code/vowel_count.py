def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

test_strings = [
    "Hello World",
    "Python is Awesome",
    "AEIOUaeiou",
    "bcdfghjkl"
]

for s in test_strings:
    print(f"'{s}' 包含元音字母数量: {count_vowels(s)}")
