lst = [3, 2, 1, 4, 7, 8, 9, 10]

full_set   = set(range(1, len(lst) + 2))
actual_set = set(lst)

missing = full_set - actual_set
print("Missing Number:", list(missing))
