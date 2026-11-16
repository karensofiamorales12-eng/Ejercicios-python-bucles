# continue con for

cadena = "Python"

for letra in cadena:

if letra == "P":
continue

print(letra)
# Salida:
# y
# t
# h
# o
# n
Python
# continue con números pares

for numero in range(1, 11):

if numero % 2 == 0:
continue

print(numero)

# Salida:
# 1
# 3
# 5
# 7
# 9
Python
# continue con while

x = 5

while x > 0:

x -= 1

if x == 3:
continue

print(x)

# Salida:
# 4
# 2
# 1
# 0

Python
# Saltar una letra específica

texto = "PROGRAMACION"

for letra in texto:

if letra == "A":
continue

print(letra)
Python
# Saltar múltiplos de 3

for numero in range(1, 16):

if numero % 3 == 0:
continue

print(numero)

Python
# continue en bucles anidados

for i in range(1, 4):

for j in range(1, 6):

if j == 3:
continue

print(i, j)
Python
# Filtrar nombres vacíos

nombres = ["Ana", "", "Luis", "", "Carlos"]

for nombre in nombres:

if nombre == "":
continue

print(nombre)
Python
# Estructura general de continue

for elemento in secuencia:

if condicion:
continue
print(elemento)
Python
# Estructura general con while
while condicion:
if condicion_salto:
continue
print("Ejecutar código")
Python
# Diferencia práctica entre break y continue
for numero in range(1, 6):
if numero == 3:
continue
print(numero)
# Salida:
# 1
# 2
# 4
# 5
Python
for numero in range(1, 6):

if numero == 3:
break

print(numero)

# Salida:
# 1
# 2