# Separador de miles

num = 1234567

print(f"{num:,}")

# Salida:
# 1,234,567

# Para usar punto como separador (estilo europeo)

print(f"{num:,}".replace(",", "."))

# Salida:
# 1.234.567