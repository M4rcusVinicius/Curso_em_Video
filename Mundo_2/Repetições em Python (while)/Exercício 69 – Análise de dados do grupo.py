"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.

"""
mais_dezoito = n_homens = n_mulheres = 0
print("\n"*50)

while True:
    print("="*50)
    nome = str(input("Qual o seu nome  : ")).strip()
    idade = int(input("Qual a sua idade : "))
    sexo = str(input("Qual o seu sexo  : ")).strip().lower()[0]
    if idade > 18:
        mais_dezoito +=1
    while sexo not in "mh":
        print("\033[31mErro no cadastro do sexo !\033[m")
        sexo = str(input("Digite |H| ou |M| : ")).strip().lower()[0]
    continuar = str(input("Você deseja continuar : ")).strip().lower()[0]
    if sexo == "h":
        n_homens += 1
    elif sexo == "m":
        if idade < 18:
            n_mulheres +=1
    while continuar not in "sn":
        continuar = str(input("Digite |S| ou |N|: ")).strip().lower()[0]
    print("="*50 + "\n")
    if continuar == "n":
        break
print(f"{mais_dezoito} pessoas tem mais de 18 anos")
print(f"{n_homens} homens foram cadastrados")
print(f"{n_mulheres} mulheres tem menos de 18 anos")

