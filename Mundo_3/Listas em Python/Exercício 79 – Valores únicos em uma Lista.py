"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

"""

from random import randint
print("")

a = []

for c in range(0, 10):
    v = randint(0, 9)
    if v in a:
        print(f"The number {v} already been added")
    else:
        print(f"The number {v} successfully added")
        a.append(v)

a.sort()

print(f"Numbers in ascending order: ", end = "")
for c in range(0, len(a)):
    if c == 0:
        print(a[c], end = "")
    else:
        print(f", {a[c]}", end = "")