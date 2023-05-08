# Metody a list
to_do = [
    "nakrmit kočku",
    "vyvenčit psa",
    "udělat svačinu",
    "absolvovat lékařskou prohlídku"
]

# In place
to_do2 = to_do.sort()  # None, protože sort nevrací hodnotu

# Obě dvě proměnné směřují v paměti na stejný list
to_do2 = to_do
# tato změna se promítne v to_do i v to_do2
to_do2[0] = "nový úkol"

# Takto se zkopíruje to_do do to_do3 a jsou zcela oddělené
to_do3 = to_do.copy()
# Tato změna se promítne jen v to_do3
to_do3[0] = "NOVÝ ÚKOL"

# Obrácený výpis položek
to_do.reverse()

print(to_do)
