# Formátovaný string
name = "David"
age = 55

print("Ahoj, já jsem " + name + ". A je mi " + str(age))
print(f"Ahoj, já jsem {name}. A je mi {age}")
print("Ahoj, já jsem {}. A je mi {}".format("David", 55))
# print("Ahoj, já jsem {}. A je mi {}".format(55, "David"))
print("Ahoj, já jsem {}. A je mi {}".format(name, age))
print("Ahoj, já jsem {0}. A je mi {1}".format(name, age))
print("Ahoj, já jsem {my_name}. A je mi {my_age}".format(my_name="Harry", my_age=22))
print("Ahoj, já jsem {my_name}. A je mi {my_age}".format(my_age=22, my_name="Harry"))
