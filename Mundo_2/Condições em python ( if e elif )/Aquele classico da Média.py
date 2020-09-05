n1 = float(input('Primeita nota : '))
n2 = float(input('Segunda nota : '))

n = float((n1 + n2)/2)

print(f'A sua média foi {n}')

if n >= 7:
    print('\033[32mParabéns! Você foi aprovado.')
elif 5 <= n < 7:
    print('\033[33mFoi por pouco! Você está de rec.')
elif n < 7:
    print('\033[31mQ pena! Você foi reprovado.')