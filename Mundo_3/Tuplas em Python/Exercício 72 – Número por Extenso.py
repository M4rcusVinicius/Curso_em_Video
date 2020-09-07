"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

"""
print("\n"*50)

c = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", 
     "sete",    "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
n = int(input("Digite um número : "))
print(f"O número {n} por extenso é {c[n]}")

if 0 > n > 20:
    print("número não cadastrado")