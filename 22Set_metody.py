first_set = {1, 2, 3}
second_set = {2, 3, 4, 5, 6, 7, 8}

# Rozdíl = difference
print(first_set.difference(second_set))

# Odstranění = remove a discard
# first_set.remove(9)
first_set.discard(9)
print(first_set)

# Rozdíl, ale změní first_set
first_set.difference_update(second_set)
print(first_set)
