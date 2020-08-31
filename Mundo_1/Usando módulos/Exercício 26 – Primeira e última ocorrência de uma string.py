"""
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

"""

n = str(input("Digite uma frase : ")).strip().lower()
print(f"A letra a aparece {n.count('a')} vezes")
print(f"A letra a aparece pela primeira vez na posição {n.find('a')+1}")
print(f"A letra a aparece pela ultima vez na posição {n.rfind('a')+1}")
