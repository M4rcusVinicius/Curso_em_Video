"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

"""
from random import randint

valores = []
impares = []
pares = []

"""
while True:
    valores.append(int(input('Digite um Valor : ')))
    if input('Continuar : ') in "Nn":
        break
"""
print("\n\n" + "="*50 + "\n")
for a in range(0, 10):
    sorteio = randint(-10, 20)
    valores.append(sorteio)

for c in valores:
    if c % 2 == 0:
        pares.append(c)
        print(f"Numero {c:3} --> Par")
    else:
        impares.append(c)
        print(f"Numero {c:3} --> Impar")
print("\n" + "="*50 + "\n")
print(f"Numeros impares : {impares}")
print(f"Numeros pares : {pares}")
print("\n" + "="*50 + "\n")