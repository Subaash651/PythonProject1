lst        = [1, 2, 3, 2, 4, 1, 5, 3]
seen       = []
duplicates = []

for item in lst:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    else:
        seen.append(item)

print("Duplicates:", duplicates)