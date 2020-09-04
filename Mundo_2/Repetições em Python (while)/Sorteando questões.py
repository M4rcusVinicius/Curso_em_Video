from random import choice

primeira = int(input("Digite a primeira questão : "))
ultima = int(input("Digite a ultima questão : "))
lista = ["a)", "b)", "c)", "d)", "e)"]

for c in range(primeira, ultima + 1):
    print(f"Questão {c} : {choice(lista)}")

