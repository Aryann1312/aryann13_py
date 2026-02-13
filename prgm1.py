nums = [1,2,2,3,3,3]

counts = {}
for n in nums:
    counts[n] = counts.get(n, 0)+1

print(counts)