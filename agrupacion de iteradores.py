lista = [5, 6, 7]

it1 = iter(lista)
it2 = iter(lista)

print(next(it1))  # 5
print(next(it1))  # 6
print(next(it1))  # 7
print(next(it2))  # 5