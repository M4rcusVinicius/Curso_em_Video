from datetime import date

ns = int(input('Em que ano você nasceu : '))

hj = date.today().year

idade = hj-ns
tp = 18 - idade
ano = 2020 + tp

print(f'\nVocê tem {idade} anos em 2020')

if tp > 0:
    print(f'Faltam {tp} anos para você se alistar !')
    print(f'O seu alistamento será em {ano}')
elif tp < 0:
    print(f'Você deveria ter se alistado à {tp*-1} anos')
    print(f'Deveria ter sido em {ano}')
else:
    print(f'Parabéns ! Você deve se alistar este ano !!!')


