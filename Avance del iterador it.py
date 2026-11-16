lista = [5, 6, 3, 2]
it = iter(lista)

print(next(it))
#        [5, 6, 3, 2]
#         ^
#         |
#        it

print(next(it))
#        [5, 6, 3, 2]
#            ^
#            |
#           it

print(next(it))
#        [5, 6, 3, 2]
#               ^
#               |
#              it