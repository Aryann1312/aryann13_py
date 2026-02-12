#Given a list of words (strings), 
#create a dictionary storing word frequencies and return only those words whose frequency is greater than 1.

words = ["python", "java", "python", "c", "java"]
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

result = {word: count for word, count in freq.items() if count > 1}

print(result)
