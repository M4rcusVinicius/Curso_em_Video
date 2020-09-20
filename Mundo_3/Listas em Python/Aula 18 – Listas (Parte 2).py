teste = list()
teste.append("Marcus")
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = "Maria"
teste[1] = 22

galera.append(teste)
print(galera)

galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append( int(input('Idade: ')))
    galera.append( dado [:])
    dado.clear()
for p in galera:
    if p[i] >= 21:
        print(f'{p[@]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade. 2