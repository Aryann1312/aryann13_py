word = "apple"

char_count = {}

for ch in word:
    if ch in char_count:
        char_count[ch] = char_count[ch] + 1
    else:
        char_count[ch] = 1

print(char_count)