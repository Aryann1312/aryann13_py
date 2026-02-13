words = ["cat", "dog", "elephant", "bat"]

length_dict = {}

for word in words:
    length = len(word)
    if length in length_dict:
        length_dict[length].append(word)
    else:
        length_dict[length] = [word]

print(length_dict)