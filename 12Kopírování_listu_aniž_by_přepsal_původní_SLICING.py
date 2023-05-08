# Slicing
my_name = "testovaci"
# print(my_name[:5:2])
# my_name[0] = "m"

to_do = [
    "nakrmit kočku",
    "vyvenčit psa",
    "udělat svačinu",
    "vyměnit žárovku",
    "dojít nakoupit"
]

# print(to_do[::1])

# list je mutable
# to_do[0] = "nový úkol"
# print(to_do)

# pozor
# to_do2 = to_do
# to_do2[0] = "super nový úkol"
# print(to_do)
# print(to_do2)

# zkopírování listu do nového
to_do3 = to_do[:]
to_do3[0] = "něco udělej"
print(to_do)
print(to_do3)
