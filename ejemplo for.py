# Iterando una cadena al revés

texto = "Python"

for i in texto[::-1]:
    print(i)

# Salida:
# n
# o
# h
# t
# y
# P


# Iterando una cadena tomando un elemento sí y otro no

texto = "Python"

for i in texto[::2]:
    print(i)

# Salida:
# P
# t
# o