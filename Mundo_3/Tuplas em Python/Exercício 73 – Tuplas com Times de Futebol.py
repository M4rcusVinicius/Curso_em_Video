"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.

"""

Times = ("Sao Paulo", "Internacional", "Cruzeiro", "Santos", "Flamengo",
         "Corinthians", "Gremio", "Atletico Mineiro", "Palmeira", "Fluminense", "Vasco da Gama", "Botafogo", "Atletico Paranaense", "Goias", "Coritiba", "Vitoria", "Sport", "Bahia", "Guarani", "Portuguesa", "Chapecoense")

print(f"\n\nTop 5 colocados :")
for c in Times:
    print(f"{c}, ", end = "")
print("")

print(f"\n4 ultimos colocados :")
for c in range(21,17):
    print(f"{Times[c]}, ", end = "")
print("")

print(f"Ordem alfabetica : {sorted(Times)}")
print("")

print(f"O Chapecoense esta na {Times.index('Chapecoense') + 1} posisao ")
print("")
