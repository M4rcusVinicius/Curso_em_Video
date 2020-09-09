"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

"""

f = str(input("Digite uma expressão : "))
if f.count("(") != f.count(")"):
    print("Sua expressão está errada")
else:
    print("Tudo certo !")
