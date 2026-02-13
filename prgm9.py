students = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]

averages = {}

for name, marks in students:
    avg = sum(marks) / len(marks)
    averages[name.lower()] = round(avg, 2)

print(averages)