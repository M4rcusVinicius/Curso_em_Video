"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

"""
print("\n" * 5)
valores = (int(input("Digite um número : ")),
           int(input("Digite um número : ")),
           int(input("Digite um número : ")),
           int(input("Digite um número : ")),
           int(input("Digite um número : ")))

if 3 in valores:
    print(f"O número 9 apareceu {valores.count(9)} vezes")

if 3 in valores:
    print(f"O número 3 apareceu na {valores.index(3)+1}° posição ")

for c in valores:
    if c % 2 == 0:
        print(c, end = " --> ")

print("São números pares")