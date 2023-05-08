to_do = [
    "nakrmit kočku",
    "vyvenčit psa",
    "udělat svačinu",
    "absolvovat lékařskou prohlídku",
    "utřít prach",
    "vymalovat pokoj",
    "koupit nový telefon"
]
# a, b, c, d, e, f, g = to_do

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)

a, *rest, g = to_do

print(a)
print(rest)
print(g)

print(to_do)
