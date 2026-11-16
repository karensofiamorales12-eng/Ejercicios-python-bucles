# Ejemplo básico de while

x = 5

while x > 0:
    x -= 1
    print(x)

# Salida:
# 4
# 3
# 2
# 1
# 0

Bucle infinito (solo como ejemplo)
Python
# No ejecutes este código
 
while True:
print("Bucle infinito")

While en una sola línea
Python
x = 5
 
while x > 0: x -= 1; print(x)
 
# Salida:
# 4
# 3
# 2
# 1
# 0

Bucles while anidados
Python
# Permutaciones
 
i = 0
 
while i < 3:
 
j = 0
 
while j < 3:
print(i, j)
j += 1
 
i += 1

Salida:

Plain Text
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
Ejemplo de la sucesión de Fibonacci
Python
a, b = 0, 1
 
while b < 25:
print(b)
a, b = b, a + b
 
# Salida:
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
While solicitando datos al usuario
Python
respuesta = ""
 
while respuesta != "salir":
respuesta = input("Escribe 'salir' para terminar: ")
 
print("Programa finalizado")
 
Contador con while
Python
contador = 1
 
while contador <= 10:
print(contador)
contador += 1
Cuenta regresiva
Python
segundos = 10
 
while segundos > 0:
print(segundos)
segundos -= 1
 
print("¡Tiempo terminado!")
 
Estructura general
Python
while condicion:
# Código a ejecutar
Ejemplo completo
Python
numero = 1
 
while numero <= 5:
print(f"Iteración número {numero}")
numero += 1
 
print("Fin del bucle")

Salida:

Plain Text
Iteración número 1
Iteración número 2
Iteración número 3
Iteración número 4
Iteración número 5
Fin del bucle
Regla fácil de recordar
Python
while condicion:
instrucciones