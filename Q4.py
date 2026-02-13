students = [("Amit", [70, 80, 90]), ("Neha", [85, 90, 95])]

average_scores = {}

for name, marks in students:
    total = 0
    for m in marks:
        total = total + m
    average = total // len(marks)
    average_scores[name] = average

print(average_scores)