# Práce se stringem
name = "testovaci"
# 012345678
print(name[0])  # t
print(name[2])  # s

# [start:stop]
print(name[0:4])  # test
print(name[2:5])  # sto

# [start:stop:krok]
print(name[0:7:2])  # tsoa
print(name[0:7:3])  # tta

# kombinace
print(name[1:])  # estovaci
print(name[:6])  # testov
print(name[::1])  # testovaci

print(name[-1])  # i
print(name[-2])  # c
print(name[-3])  # a

print(name[::-1])  # icavotset
print(name[::-2])  # iaost
