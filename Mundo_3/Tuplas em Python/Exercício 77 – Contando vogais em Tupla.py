"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""

p = ("Maçã", "Abacate", "Limão", "Pera", "Melão", "Melancia", "Batata")

for c in p:
    print(f"\n\nA palavra {c} pussui ")
    a = c.count("a")
    e = c.count("e")
    i = c.count("i")
    o = c.count("o")
    u = c.count("u")
    if a > 0:
        print(f"{a} letras 'a'")
    if e > 0:
        print(f"{e} letras 'e'")
    if i > 0:
        print(f"{i} letras 'i'")
    if o > 0:
        print(f"{o} letras 'o'")
    if u > 0:
        print(f"{u} letras 'u'")