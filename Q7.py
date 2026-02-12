attendance = {
    "Ravi": ["P", "A", "P"],
    "Neha": ["P", "P", "P"]
}

present_days = {}

for name in attendance:
    count = 0
    for day in attendance[name]:
        if day == "P":
            count = count + 1
    present_days[name] = count

print(present_days)