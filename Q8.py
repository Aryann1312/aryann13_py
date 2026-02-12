#Given a string, create a dictionary where each character is a key and the value is a tuple of indices at which the character appears.

s = "banana"
result = {}

for index, ch in enumerate(s):
    result.setdefault(ch, []).append(index)

# Convert lists to tuples
result = {k: tuple(v) for k, v in result.items()}

print(result)
