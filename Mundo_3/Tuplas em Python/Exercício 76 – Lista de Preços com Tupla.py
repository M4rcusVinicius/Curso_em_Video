"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""
from random import randint

Obj = ("Maçã      ", f"R$ {randint(10, 99)},{randint(10, 99)}", 
       "Abacate   ", f"R$ {randint(10, 99)},{randint(10, 99)}", 
       "Limão     ", f"R$ {randint(10, 99)},{randint(10, 99)}", 
       "Pera      ", f"R$ {randint(10, 99)},{randint(10, 99)}", 
       "Melão     ", f"R$ {randint(10, 99)},{randint(10, 99)}", 
       "Melancia  ", f"R$ {randint(10, 99)},{randint(10, 99)}", 
       "Batata    ", f"R$ {randint(10, 99)},{randint(10, 99)}", 
       "Beterraba ", f"R$ {randint(10, 99)},{randint(10, 99)}", )

Obj = ("Maçã",      "R$ 45,81", 
       "Abacate",   "R$ 94,83", 
       "Limão",     "R$ 98,73", 
       "Pera",      "R$ 29,84",)

for c in range(0, len(Obj), 2):
    print(f"{Obj[c]:10}" + Obj[c+1])