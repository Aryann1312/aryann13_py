#You are given two dictionaries representing marks of students in two tests.and
#Merge them into a single dictionary where the value is a tuple of marks from both tests.

test1 = {"Amit": 70, "Neha": 85}
test2 = {"Amit": 80, "Neha": 90}

result = {name: (test1[name], test2[name]) for name in test1}

print(result)
