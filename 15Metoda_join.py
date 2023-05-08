# Metody a list
to_do = [
    "nakrmit kočku",
    "vyvenčit psa",
    "udělat svačinu",
    "absolvovat lékařskou prohlídku"
]

to_do.sort()
# # ['absolvovat lékařskou prohlídku', 'nakrmit kočku', 'udělat svačinu', 'vyvenčit psa']
to_do.reverse()
# # ['vyvenčit psa', 'udělat svačinu', 'nakrmit kočku', 'absolvovat lékařskou prohlídku']
print(to_do[::-1])
# # ['absolvovat lékařskou prohlídku', 'nakrmit kočku', 'udělat svačinu', 'vyvenčit psa']

print(list(range(100)))

pozdrav = " ".join(["ahoj", "já", "jsem", "David"])
print(pozdrav)
