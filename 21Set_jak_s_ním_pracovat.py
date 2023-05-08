first_set = {1, 2, 2, 2, 3, 8, 5, 5, 5}
# print(first_set) # {1, 2, 3, 5, 8}
# print(first_set[0])

# Vypsání pomocí cyklu
for x in first_set:
    print(x)

print(3 in first_set)  # True

print(len(first_set))  # 5

old_set = first_set.copy()  # kopírování setu

first_set.add(100)
print(first_set)
print(old_set)
