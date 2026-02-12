text = "programming"

unique_chars = []
for ch in text:
    if ch not in unique_chars:
        unique_chars.append(ch)

result = tuple(unique_chars)
print(result)