"""
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

"""

print("\n" * 10 + "Sequência de Fibonacci")

n = int(input("Quantos números você gostaria de saber : "))
f1 = 0
f2 = 1
print("""
==> {f1}
==> {f2} 
""")
c = 3

while c <= n:
    f3 = f1 = f2
    f1 = f2 = f3

print("fim")

