# break con for
 
for i in range(5):
print(i)
break
Python
# break al encontrar una letra
 
cadena = "Python"
 
for letra in cadena:
 
if letra == "h":
print("Se encontró la h")
break
 
print(letra)
Python
# break al encontrar un número
 
numeros = [10, 20, 30, 40, 50]
 
for numero in numeros:
 
if numero == 30:
print("Número encontrado")
break
 
print(numero)
Python
# break con while
 
x = 5
 
while True:
 
x -= 1
print(x)
 
if x == 0:
break
Python
# break en bucles anidados
 
for i in range(4):
 
for j in range(4):
break
 
print(i, j)
 
Python
# break en el bucle interno
 
for i in range(1, 4):
 
for j in range(1, 6):
 
if j == 3:
break
 
print(i, j)
Python
# Menú con break
 
while True:
 
opcion = input("Escriba salir para terminar: ")
 
if opcion.lower() == "salir":
break
 
print("Continuando...")
Python
# Buscar un elemento en una lista
 
frutas = ["manzana", "pera", "uva", "mango"]
 
for fruta in frutas:
 
if fruta == "uva":
print("Fruta encontrada")
break
Python
# Adivinar un número
 
numero_secreto = 7
 
while True:
 
numero = int(input("Adivina el número: "))
 
if numero == numero_secreto:
print("¡Correcto!")
break
Python
# Estructura general de break
 
for elemento in secuencia:
 
if condicion:
break
Python
while condicion:
 
if condicion_salida:
break