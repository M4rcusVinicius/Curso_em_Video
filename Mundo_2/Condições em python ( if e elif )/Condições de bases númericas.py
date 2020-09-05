num = int(input('Digite um numero inteiro : '))
print('''Escolha uma das base para a converção : 
       |1| Converter para Binário
       |2| Converter para Octal
       |3| Converter para Hexadecimal''')

opção = int(input('Sua opção : '))

if opção == 1:
    print(f'\033[37m{num} em \033[32mBinánio\033[37m'
          f' é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'\033[37m{num} em \033[34mOctal\033[37m'
          f' é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'\033[37m{num} em \033[35mHexadecimal\033[37m'
          f' é igual a {hex(num)[2:]}')