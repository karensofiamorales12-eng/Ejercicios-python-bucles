# Explicando slice (rebanado)

texto = "Python"
print("Texto original:", texto)
print("Invertido:", texto[::-1])

print()

# Estructura general
# secuencia[inicio:fin:paso]

nums = [1, 2, 3, 4, 5]

print("Lista original:", nums)
print("Lista invertida:", nums[::-1])

print()

print("Cada dos elementos:")
print(nums[::2])

print()

print("Primeros tres elementos:")
print(nums[:3])

print()

print("Desde la posición 2 hasta el final:")
print(nums[2:])

print()

print("Desde la posición 1 hasta la 4:")
print(nums[1:4])

print()

print("De atrás hacia adelante saltando de 2 en 2:")
print(nums[::-2])
