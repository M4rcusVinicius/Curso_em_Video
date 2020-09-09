"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,mostre:
A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

"""

valores = []

while True:
    valores.append(int(input('Digite um Valor : ')))
    if input('Continuar : ') in "Nn":
        break
valores.sort(reverse=True)
print(f"Você digitou {len(valores)} elementos")
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print("O valor cinco está na lista")
