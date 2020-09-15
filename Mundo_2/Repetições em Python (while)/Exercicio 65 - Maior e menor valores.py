n = int(input("Digite um número : "))
qtd = 4
total = n
max = 0
min = n
c = 1
resp = ''
c1 = 0
while resp != 'n':

    while c != qtd:
        n = int(input("Digite um número : "))
        c += 1
        if n > max:
            max = n
        if n < min:
            min = n
        total += n

    print(f'O maior valor lido foi {max}')
    print(f'O menor valor lido foi {min}')
    print(f'A media entre todos é {total / c} \n\n')

    resp = input('Você gostaria de continuar respondendo ?'
                 'Digite |N| para não e |S| para sim : ').lower().strip()
    qtd += int(input('Voce gostaria de digitar mais quantos números : '))
